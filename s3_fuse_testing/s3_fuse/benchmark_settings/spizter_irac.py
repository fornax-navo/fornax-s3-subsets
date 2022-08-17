"""
test parameters for a selection of average-sized SPITZER IRAC mosaics.
single f32 image HDU, uncompressed. 9-12 MB.
"""
CUT_SHAPES = ((40, 40), (200, 200))
CUT_COUNTS = (1, 5, 20)
BUCKET = "nishapur"
AUTHENTICATE_S3 = True
HDU_IX = 1
LOADERS = (
    "astropy", "fitsio",  "astropy_s3_section", "astropy_s3", "greedy_astropy"
)
TEST_FILES = (
    "spitzer/irac/SPITZER_I1_61016064_0000_1_E12340652_maic.fits",
    "spitzer/irac/SPITZER_I2_61015552_0000_1_E12340647_maic.fits",
    "spitzer/irac/SPITZER_I1_61015808_0000_1_E12340633_maic.fits",
    "spitzer/irac/SPITZER_I1_53027584_0000_2_E10384449_maic.fits",
    "spitzer/irac/SPITZER_I2_58031104_0000_1_E12039060_maic.fits",
    "spitzer/irac/SPITZER_I2_61016832_0000_1_E12340696_maic.fits",
    "spitzer/irac/SPITZER_I4_4501248_0000_6_E8385697_maic.fits",
    "spitzer/irac/SPITZER_I1_53026304_0000_2_E10384450_maic.fits",
    "spitzer/irac/SPITZER_I2_58590720_0000_1_E11258271_maic.fits",
    "spitzer/irac/SPITZER_I2_58029824_0000_1_E12039034_maic.fits",
    "spitzer/irac/SPITZER_I1_58031104_0000_1_E12039088_maic.fits",
    "spitzer/irac/SPITZER_I3_4502016_0000_6_E8382852_maic.fits",
    "spitzer/irac/SPITZER_I4_4500992_0000_6_E8445651_maic.fits",
    "spitzer/irac/SPITZER_I2_61009664_0000_1_E12586849_maic.fits",
    "spitzer/irac/SPITZER_I1_61012736_0000_1_E12340225_maic.fits",
    "spitzer/irac/SPITZER_I2_49711616_0000_2_E10718222_maic.fits",
    "spitzer/irac/SPITZER_I2_53026304_0000_2_E10388411_maic.fits",
    "spitzer/irac/SPITZER_I1_49715200_0000_2_E10710430_maic.fits",
    "spitzer/irac/SPITZER_I2_61011968_0000_1_E12589125_maic.fits",
    "spitzer/irac/SPITZER_I2_49713152_0000_2_E10718390_maic.fits",
    "spitzer/irac/SPITZER_I2_4500480_0000_6_E8381418_maic.fits",
    "spitzer/irac/SPITZER_I1_49714432_0000_2_E10710357_maic.fits",
    "spitzer/irac/SPITZER_I1_58030848_0000_1_E12039090_maic.fits",
    "spitzer/irac/SPITZER_I1_61008128_0000_1_E12583867_maic.fits",
    "spitzer/irac/SPITZER_I2_61007360_0000_1_E12583069_maic.fits",
    "spitzer/irac/SPITZER_I1_53025536_0000_2_E10384414_maic.fits",
    "spitzer/irac/SPITZER_I1_61014016_0000_1_E12340485_maic.fits",
    "spitzer/irac/SPITZER_I4_4502272_0000_6_E8445332_maic.fits",
    "spitzer/irac/SPITZER_I2_53025536_0000_2_E10388358_maic.fits",
    "spitzer/irac/SPITZER_I1_53024000_0000_2_E10384371_maic.fits",
    "spitzer/irac/SPITZER_I1_61013248_0000_1_E12340357_maic.fits",
    "spitzer/irac/SPITZER_I2_58027520_0000_1_E12038802_maic.fits",
    "spitzer/irac/SPITZER_I1_49715456_0000_2_E10710346_maic.fits",
    "spitzer/irac/SPITZER_I1_61008896_0000_1_E12585784_maic.fits",
    "spitzer/irac/SPITZER_I2_61009152_0000_1_E12585987_maic.fits",
    "spitzer/irac/SPITZER_I1_61014016_0000_1_E12340485_maic.fits",
    "spitzer/irac/SPITZER_I2_50580224_0000_2_E10632779_maic.fits",
    "spitzer/irac/SPITZER_I2_58029312_0000_1_E12039047_maic.fits",
    "spitzer/irac/SPITZER_I1_61013760_0000_1_E12340475_maic.fits",
    "spitzer/irac/SPITZER_I2_53025280_0000_2_E10388364_maic.fits",
    "spitzer/irac/SPITZER_I2_49713152_0000_2_E10718390_maic.fits",
    "spitzer/irac/SPITZER_I1_61010944_0000_1_E12587703_maic.fits",
    "spitzer/irac/SPITZER_I2_49712384_0000_2_E10718251_maic.fits",
    "spitzer/irac/SPITZER_I2_53028352_0000_2_E10388321_maic.fits",
    "spitzer/irac/SPITZER_I1_61010176_0000_1_E12586871_maic.fits",
    "spitzer/irac/SPITZER_I1_53028352_0000_2_E10384507_maic.fits",
    "spitzer/irac/SPITZER_I2_58029824_0000_1_E12039034_maic.fits",
    "spitzer/irac/SPITZER_I2_53027072_0000_2_E10388392_maic.fits",
    "spitzer/irac/SPITZER_I1_53028096_0000_2_E10384473_maic.fits",
    "spitzer/irac/SPITZER_I1_4500992_0000_6_E8445366_maic.fits",
    "spitzer/irac/SPITZER_I1_4500736_0000_6_E8380933_maic.fits",
    "spitzer/irac/SPITZER_I3_4501760_0000_6_E8382518_maic.fits",
    "spitzer/irac/SPITZER_I1_58589952_0000_1_E11257214_maic.fits",
    "spitzer/irac/SPITZER_I2_61010432_0000_1_E12587814_maic.fits",
    "spitzer/irac/SPITZER_I2_49715200_0000_2_E10718388_maic.fits",
    "spitzer/irac/SPITZER_I4_4501760_0000_6_E8382524_maic.fits",
    "spitzer/irac/SPITZER_I1_58028800_0000_1_E12038977_maic.fits",
    "spitzer/irac/SPITZER_I1_53024512_0000_2_E10384354_maic.fits",
    "spitzer/irac/SPITZER_I2_61015040_0000_1_E12340592_maic.fits",
    "spitzer/irac/SPITZER_I2_61014272_0000_1_E12340423_maic.fits",
    "spitzer/irac/SPITZER_I1_61014016_0000_1_E12340485_maic.fits",
    "spitzer/irac/SPITZER_I3_4502272_0000_6_E8445267_maic.fits",
    "spitzer/irac/SPITZER_I4_4502016_0000_6_E8382845_maic.fits",
    "spitzer/irac/SPITZER_I1_53028352_0000_2_E10384507_maic.fits",
    "spitzer/irac/SPITZER_I2_58030848_0000_1_E12039091_maic.fits",
    "spitzer/irac/SPITZER_I4_4500992_0000_6_E8445651_maic.fits",
    "spitzer/irac/SPITZER_I1_4501504_0000_6_E8380383_maic.fits",
    "spitzer/irac/SPITZER_I2_61010688_0000_1_E12588228_maic.fits",
    "spitzer/irac/SPITZER_I2_53024256_0000_2_E10388262_maic.fits",
    "spitzer/irac/SPITZER_I1_61016576_0000_1_E12340686_maic.fits",
    "spitzer/irac/SPITZER_I2_49714944_0000_2_E10718513_maic.fits",
    "spitzer/irac/SPITZER_I1_61016832_0000_1_E12340679_maic.fits",
    "spitzer/irac/SPITZER_I1_53026816_0000_2_E10384470_maic.fits",
    "spitzer/irac/SPITZER_I2_61014272_0000_1_E12340423_maic.fits",
    "spitzer/irac/SPITZER_I2_49714176_0000_2_E10718317_maic.fits",
    "spitzer/irac/SPITZER_I2_58026752_0000_1_E12038804_maic.fits",
    "spitzer/irac/SPITZER_I2_53028352_0000_2_E10388321_maic.fits",
    "spitzer/irac/SPITZER_I1_58030592_0000_1_E12039073_maic.fits",
    "spitzer/irac/SPITZER_I2_61015040_0000_1_E12340592_maic.fits",
    "spitzer/irac/SPITZER_I2_53024512_0000_2_E10388365_maic.fits",
    "spitzer/irac/SPITZER_I1_4501248_0000_6_E8385822_maic.fits",
    "spitzer/irac/SPITZER_I2_49713408_0000_2_E10718261_maic.fits",
    "spitzer/irac/SPITZER_I1_53025024_0000_2_E10384437_maic.fits",
    "spitzer/irac/SPITZER_I1_61016576_0000_1_E12340686_maic.fits",
    "spitzer/irac/SPITZER_I2_53025024_0000_2_E10388397_maic.fits",
    "spitzer/irac/SPITZER_I1_53028096_0000_2_E10384473_maic.fits",
    "spitzer/irac/SPITZER_I1_4500480_0000_6_E8381415_maic.fits",
    "spitzer/irac/SPITZER_I1_61014272_0000_1_E12340464_maic.fits",
    "spitzer/irac/SPITZER_I4_4500736_0000_6_E8380930_maic.fits",
    "spitzer/irac/SPITZER_I1_49712640_0000_2_E10710274_maic.fits",
    "spitzer/irac/SPITZER_I2_58028800_0000_1_E12038970_maic.fits",
    "spitzer/irac/SPITZER_I1_61011968_0000_1_E12589120_maic.fits",
    "spitzer/irac/SPITZER_I2_49713664_0000_2_E10718304_maic.fits",
    "spitzer/irac/SPITZER_I1_61014272_0000_1_E12340464_maic.fits",
    "spitzer/irac/SPITZER_I1_49716224_0000_2_E10710389_maic.fits",
    "spitzer/irac/SPITZER_I1_49713152_0000_2_E10710507_maic.fits",
    "spitzer/irac/SPITZER_I1_58030336_0000_1_E12038987_maic.fits",
    "spitzer/irac/SPITZER_I2_53026560_0000_2_E10388242_maic.fits",
    "spitzer/irac/SPITZER_I1_58028032_0000_1_E12038750_maic.fits",
    "spitzer/irac/SPITZER_I1_49715456_0000_2_E10710346_maic.fits",
)
