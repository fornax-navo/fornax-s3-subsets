"""
test parameters for a sampling of full-depth gPhoton 2-generated GALEX images
in gzip-compressed format. same underlying data as the galex_rice case.

please note that this is specifically intended to be a really terrible case
for subsetting! it should be no better -- usually worse -- than just
downloading the whole file.
"""

CUT_SHAPES = ((40, 40), (200, 200))
CUT_COUNTS = (1, 20)
BUCKET = "nishapur"
AUTHENTICATE_S3 = True
HDU_IX = 0
# there currently appears to be an undesirable behavior in fsspec that
# causes it to re-download and decompress the entire file once per each
# line -- so a 40x40 cut will in general result in downloading and
# decompressing a file 40 times. I have marked it out for now -- each case
# takes ~20 minutes so is impractical to run.

# there is also apparently a bug in the "greedy" benchmark wrapper for astropy
# wrt gzipped files that causes it to crash out. may fix at some point, may
# not -- this is not really an interesting case; we know it's bad.
LOADERS = (
    "astropy", "astropy_s3", "fitsio"
)
TEST_FILES = (
    'e06818/e06818-fd-full.fits.gz',
    'e43718/e43718-nd-full.fits.gz',
    'e07415/e07415-fd-full.fits.gz',
    'e33791/e33791-nd-full.fits.gz',
    'e33568/e33568-nd-full.fits.gz',
    'e09208/e09208-nd-full.fits.gz',
    'e26141/e26141-nd-full.fits.gz',
    'e15231/e15231-nd-full.fits.gz',
    'e18451/e18451-fd-full.fits.gz',
    'e16031/e16031-nd-full.fits.gz',
    'e28416/e28416-nd-full.fits.gz',
    'e03797/e03797-nd-full.fits.gz',
    'e46167/e46167-nd-full.fits.gz',
    'e21371/e21371-fd-full.fits.gz',
    'e07770/e07770-nd-full.fits.gz',
    'e29633/e29633-fd-full.fits.gz',
    'e41228/e41228-nd-full.fits.gz',
    'e24342/e24342-nd-full.fits.gz',
    'e29544/e29544-fd-full.fits.gz',
    'e00938/e00938-fd-full.fits.gz',
    'e28374/e28374-nd-full.fits.gz',
    'e04338/e04338-nd-full.fits.gz',
    'e07053/e07053-nd-full.fits.gz',
    'e19760/e19760-fd-full.fits.gz',
    'e07451/e07451-fd-full.fits.gz',
    'e09909/e09909-nd-full.fits.gz',
    'e13999/e13999-fd-full.fits.gz',
    'e42100/e42100-nd-full.fits.gz',
    'e06748/e06748-fd-full.fits.gz',
    'e40591/e40591-nd-full.fits.gz',
    'e43013/e43013-nd-full.fits.gz',
    'e44795/e44795-nd-full.fits.gz',
    'e26760/e26760-fd-full.fits.gz',
    'e22053/e22053-nd-full.fits.gz',
    'e14313/e14313-fd-full.fits.gz',
    'e35028/e35028-nd-full.fits.gz',
    'e05027/e05027-fd-full.fits.gz',
    'e31636/e31636-fd-full.fits.gz',
    'e35387/e35387-nd-full.fits.gz',
    'e10602/e10602-nd-full.fits.gz',
    'e20916/e20916-nd-full.fits.gz',
    'e25577/e25577-nd-full.fits.gz',
    'e09353/e09353-fd-full.fits.gz',
    'e28978/e28978-fd-full.fits.gz',
    'e11428/e11428-nd-full.fits.gz',
    'e14019/e14019-fd-full.fits.gz',
    'e17201/e17201-fd-full.fits.gz',
    'e13734/e13734-nd-full.fits.gz',
    'e21486/e21486-fd-full.fits.gz',
    'e20036/e20036-nd-full.fits.gz',
    'e30689/e30689-fd-full.fits.gz',
    'e12509/e12509-fd-full.fits.gz',
    'e37319/e37319-nd-full.fits.gz',
    'e28245/e28245-fd-full.fits.gz',
    'e08323/e08323-nd-full.fits.gz',
    'e01747/e01747-nd-full.fits.gz',
    'e04348/e04348-nd-full.fits.gz',
    'e34827/e34827-nd-full.fits.gz',
    'e06038/e06038-fd-full.fits.gz',
    'e16418/e16418-nd-full.fits.gz',
    'e05265/e05265-fd-full.fits.gz',
    'e04139/e04139-nd-full.fits.gz',
    'e10930/e10930-nd-full.fits.gz',
    'e23532/e23532-nd-full.fits.gz',
    'e26676/e26676-nd-full.fits.gz',
    'e25925/e25925-nd-full.fits.gz',
    'e43597/e43597-nd-full.fits.gz',
    'e15645/e15645-nd-full.fits.gz',
    'e29245/e29245-fd-full.fits.gz',
    'e30590/e30590-fd-full.fits.gz',
    'e40404/e40404-nd-full.fits.gz',
    'e26678/e26678-nd-full.fits.gz',
    'e01411/e01411-fd-full.fits.gz',
    'e13712/e13712-nd-full.fits.gz',
    'e10743/e10743-nd-full.fits.gz',
    'e08553/e08553-nd-full.fits.gz',
    'e34196/e34196-nd-full.fits.gz',
    'e28692/e28692-fd-full.fits.gz',
    'e25728/e25728-nd-full.fits.gz',
    'e37169/e37169-nd-full.fits.gz',
    'e04469/e04469-fd-full.fits.gz',
    'e05160/e05160-fd-full.fits.gz',
    'e14829/e14829-fd-full.fits.gz',
    'e28618/e28618-nd-full.fits.gz',
    'e15308/e15308-nd-full.fits.gz',
    'e25707/e25707-fd-full.fits.gz',
    'e09880/e09880-nd-full.fits.gz',
    'e08265/e08265-nd-full.fits.gz',
    'e21588/e21588-nd-full.fits.gz',
    'e01827/e01827-fd-full.fits.gz',
    'e35170/e35170-nd-full.fits.gz',
    'e20155/e20155-fd-full.fits.gz',
    'e35030/e35030-nd-full.fits.gz',
    'e22848/e22848-fd-full.fits.gz',
    'e10853/e10853-nd-full.fits.gz',
    'e03477/e03477-fd-full.fits.gz',
    'e07704/e07704-fd-full.fits.gz',
    'e05698/e05698-nd-full.fits.gz',
    'e23645/e23645-fd-full.fits.gz',
    'e09371/e09371-nd-full.fits.gz'
)
