"""
galex-specific utilities.
some are vendored from gPhoton 2.
others require a gPhoton 2 installation in the environment.
"""
import random
import warnings
from types import MappingProxyType

import numpy as np
from gPhoton.aspect import TABLE_PATHS
from gPhoton.reference import eclipse_to_paths
from more_itertools import chunked
from pyarrow import parquet


def get_galex_version_path(eclipse, band, depth, obj, version, data_root):
    """
    get file path for the GALEX data object with specified eclipse, band,
    depth, object type, and compression version, relative to data_root.
    this is a semistandardized convention loosely based on gPhoton conventions
    (which don't include multiple compression types!)
    """
    paths = eclipse_to_paths(eclipse, data_root, depth)
    return {
        "rice": paths[band][obj].replace(".fits.gz", "_rice.fits"),
        "none": paths[band][obj].replace(".gz", ""),
        "gz": paths[band][obj],
    }[version]


def pick_galex_eclipses(count=5, eclipse_type="mislike"):
    """randomly select a set of GALEX eclipses matching some criteria"""
    # this is the set of actually-available eclipses. it should be adjusted to
    # contain actually-available eclipses in your bucket of choice, or whatever
    # restricted subset you would like.
    with open("extant_eclipses.txt") as file:
        extant_eclipses = set(map(int, file.readlines()))

    # typically larger files, ~10000 x 10000 pixels per frame
    if eclipse_type == "complex":
        columns, predicates, refs = ["legs"], [">"], [1]
    # typically smaller files, ~3000x3000 pixels per frame
    elif eclipse_type == "mislike":
        columns, predicates, refs = (
            ["legs", "obstype"],
            ["=", "in"],
            [0, ["MIS", "DIS", "GII"]],
        )
    # anything!
    else:
        columns, predicates, refs = [], [], []
    eclipse_slice = parquet_generic_search(
        columns, predicates, refs, table_path=TABLE_PATHS["metadata"]
    )
    sliced_eclipses = set(eclipse_slice["eclipse"].to_pylist())
    eclipses_of_interest = extant_eclipses.intersection(sliced_eclipses)
    actual_count = min(count, len(eclipses_of_interest))
    if actual_count < count:
        warnings.warn("only {len(eclipses_of_interest)} available")
    return random.sample(tuple(eclipses_of_interest), k=actual_count)


def parquet_generic_search(columns, predicates, refs, table_path):
    filters = [
        (column, predicate, ref)
        for column, predicate, ref in zip(columns, predicates, refs)
    ]
    return parquet.read_table(table_path, filters=filters)


def galex_chunker(eclipses, targets, bands, chunksize=40):
    eclipse_chunks = chunked(eclipses, int(chunksize / len(bands)))
    eclipse_targets = {
        eclipse: tuple(filter(lambda t: eclipse in t["galex"], targets))
        for eclipse in eclipses
    }
    return eclipse_chunks, eclipse_targets


def galex_chunk_kwargs(eclipse, band, data_root, loader, _bands):
    return {
        "path": eclipse_to_paths(eclipse, data_root, None, "rice")[band][
            "image"
        ],
        "get_wcs": True,
        "loader": loader,
        "hdu_indices": (1, 2, 3),
        "band": band,
    }


def counts2mag(cps, band):
    scale = 18.82 if band == "FUV" else 20.08
    # This threw a warning if the countrate was negative which happens when
    #  the background is brighter than the source. Suppress.
    with np.errstate(invalid="ignore"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mag = -2.5 * np.log10(cps) + scale
    return mag


GALEX_CUT_CONSTANTS = MappingProxyType(
    {
        'chunker': galex_chunker,
        'kwarg_assembler': galex_chunk_kwargs,
        'hdu_indices': (1, 2, 3),
        'exptime_field': 'EXPT_0'
    }
)
