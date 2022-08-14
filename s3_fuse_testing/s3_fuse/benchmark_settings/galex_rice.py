"""
test parameters for a sampling of full-depth gPhoton 2-generated GALEX images
in RICE-compressed format. same underlying data as the galex_gzip case.
"""
CUT_SHAPES = ((40, 40), (200, 200), )
CUT_COUNTS = (1, 5, 20)
BUCKET = "nishapur"
AUTHENTICATE_S3 = True
HDU_IX = 1
# note that CompImageHDU does not expose a .section attribute -- it wouldn't
# particularly matter anyway.
LOADERS = (
    "fitsio", "fitsio_preload_hdu", "astropy", "astropy_s3", "greedy_astropy"
)
TEST_FILES = (
    'e06818/e06818-fd-full-rice.fits',
    'e43718/e43718-nd-full-rice.fits',
    'e07415/e07415-fd-full-rice.fits',
    'e33791/e33791-nd-full-rice.fits',
    'e33568/e33568-nd-full-rice.fits',
    'e09208/e09208-nd-full-rice.fits',
    'e26141/e26141-nd-full-rice.fits',
    'e15231/e15231-nd-full-rice.fits',
    'e18451/e18451-fd-full-rice.fits',
    'e16031/e16031-nd-full-rice.fits',
    'e28416/e28416-nd-full-rice.fits',
    'e03797/e03797-nd-full-rice.fits',
    'e46167/e46167-nd-full-rice.fits',
    'e21371/e21371-fd-full-rice.fits',
    'e07770/e07770-nd-full-rice.fits',
    'e29633/e29633-fd-full-rice.fits',
    'e41228/e41228-nd-full-rice.fits',
    'e24342/e24342-nd-full-rice.fits',
    'e29544/e29544-fd-full-rice.fits',
    'e00938/e00938-fd-full-rice.fits',
    'e28374/e28374-nd-full-rice.fits',
    'e04338/e04338-nd-full-rice.fits',
    'e07053/e07053-nd-full-rice.fits',
    'e19760/e19760-fd-full-rice.fits',
    'e07451/e07451-fd-full-rice.fits',
    'e09909/e09909-nd-full-rice.fits',
    'e13999/e13999-fd-full-rice.fits',
    'e42100/e42100-nd-full-rice.fits',
    'e06748/e06748-fd-full-rice.fits',
    'e40591/e40591-nd-full-rice.fits',
    'e43013/e43013-nd-full-rice.fits',
    'e44795/e44795-nd-full-rice.fits',
    'e26760/e26760-fd-full-rice.fits',
    'e22053/e22053-nd-full-rice.fits',
    'e14313/e14313-fd-full-rice.fits',
    'e35028/e35028-nd-full-rice.fits',
    'e05027/e05027-fd-full-rice.fits',
    'e31636/e31636-fd-full-rice.fits',
    'e35387/e35387-nd-full-rice.fits',
    'e10602/e10602-nd-full-rice.fits',
    'e20916/e20916-nd-full-rice.fits',
    'e25577/e25577-nd-full-rice.fits',
    'e09353/e09353-fd-full-rice.fits',
    'e28978/e28978-fd-full-rice.fits',
    'e11428/e11428-nd-full-rice.fits',
    'e14019/e14019-fd-full-rice.fits',
    'e17201/e17201-fd-full-rice.fits',
    'e13734/e13734-nd-full-rice.fits',
    'e21486/e21486-fd-full-rice.fits',
    'e20036/e20036-nd-full-rice.fits',
    'e30689/e30689-fd-full-rice.fits',
    'e12509/e12509-fd-full-rice.fits',
    'e37319/e37319-nd-full-rice.fits',
    'e28245/e28245-fd-full-rice.fits',
    'e08323/e08323-nd-full-rice.fits',
    'e01747/e01747-nd-full-rice.fits',
    'e04348/e04348-nd-full-rice.fits',
    'e34827/e34827-nd-full-rice.fits',
    'e06038/e06038-fd-full-rice.fits',
    'e16418/e16418-nd-full-rice.fits',
    'e05265/e05265-fd-full-rice.fits',
    'e04139/e04139-nd-full-rice.fits',
    'e10930/e10930-nd-full-rice.fits',
    'e23532/e23532-nd-full-rice.fits',
    'e26676/e26676-nd-full-rice.fits',
    'e25925/e25925-nd-full-rice.fits',
    'e43597/e43597-nd-full-rice.fits',
    'e15645/e15645-nd-full-rice.fits',
    'e29245/e29245-fd-full-rice.fits',
    'e30590/e30590-fd-full-rice.fits',
    'e40404/e40404-nd-full-rice.fits',
    'e26678/e26678-nd-full-rice.fits',
    'e01411/e01411-fd-full-rice.fits',
    'e13712/e13712-nd-full-rice.fits',
    'e10743/e10743-nd-full-rice.fits',
    'e08553/e08553-nd-full-rice.fits',
    'e34196/e34196-nd-full-rice.fits',
    'e28692/e28692-fd-full-rice.fits',
    'e25728/e25728-nd-full-rice.fits',
    'e37169/e37169-nd-full-rice.fits',
    'e04469/e04469-fd-full-rice.fits',
    'e05160/e05160-fd-full-rice.fits',
    'e14829/e14829-fd-full-rice.fits',
    'e28618/e28618-nd-full-rice.fits',
    'e15308/e15308-nd-full-rice.fits',
    'e25707/e25707-fd-full-rice.fits',
    'e09880/e09880-nd-full-rice.fits',
    'e08265/e08265-nd-full-rice.fits',
    'e21588/e21588-nd-full-rice.fits',
    'e01827/e01827-fd-full-rice.fits',
    'e35170/e35170-nd-full-rice.fits',
    'e20155/e20155-fd-full-rice.fits',
    'e35030/e35030-nd-full-rice.fits',
    'e22848/e22848-fd-full-rice.fits',
    'e10853/e10853-nd-full-rice.fits',
    'e03477/e03477-fd-full-rice.fits',
    'e07704/e07704-fd-full-rice.fits',
    'e05698/e05698-nd-full-rice.fits',
    'e23645/e23645-fd-full-rice.fits',
    'e09371/e09371-nd-full-rice.fits'
)