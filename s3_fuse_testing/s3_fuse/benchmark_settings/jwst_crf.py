"""
test parameters for a series of JWST CRF images. these are ~200 MB
uncompressed files, but they're mostly so big because they have a bunch of
backplanes. the individual extensions are ~2000x2000 32-bit floating-point
arrays.

TODO: except for the last extension, which is maybe compressed ASDF data?
 looking into it.
"""
CUT_SHAPES = ((40, 40), (200, 200), (200, 10), (10, 200))
CUT_COUNTS = (1, 5, 20)
BUCKET = "nishapur"
AUTHENTICATE_S3 = True
HDU_IX = 1
LOADERS = (
    "astropy", "astropy_s3_section", "astropy_s3", "fitsio", "greedy_astropy"
)
TEST_FILES = (
    'jwst/jw02733001001/jw02733001001_02101_00001_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00001_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00001_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00001_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00002_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00002_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00002_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00002_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00002_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00003_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00003_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00003_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00003_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00004_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00004_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00004_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00004_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00004_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00005_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00005_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00005_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00005_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00005_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00006_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00006_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00006_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00006_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00006_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00007_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00007_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00007_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00007_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00008_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00008_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00008_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02101_00008_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00001_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00001_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00001_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00001_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00001_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00002_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00002_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00002_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00002_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00002_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00003_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00003_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00003_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00003_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00003_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00004_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00004_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00004_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00004_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00004_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00005_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00005_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00005_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00005_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00005_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00006_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00006_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00006_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00006_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00006_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00007_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00007_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00007_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00007_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00008_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00008_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00008_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00008_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02103_00008_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00001_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00001_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00001_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00001_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00001_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00002_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00002_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00002_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00002_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00002_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00003_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00003_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00003_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00003_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00004_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00004_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00004_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00004_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00005_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00005_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00005_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00005_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00006_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00006_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00006_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00006_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00006_nrcblong_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00007_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00007_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00007_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00007_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00008_nrcb1_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00008_nrcb2_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00008_nrcb3_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00008_nrcb4_o001_crf.fits',
    'jwst/jw02733001001/jw02733001001_02105_00008_nrcblong_o001_crf.fits'
)
