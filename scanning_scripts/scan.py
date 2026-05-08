TOP = 32.12
MICROSCOPE_THICKNESS = 2.1

BOTTOM = 34.02
# BOTTOM = TOP+MICROSCOPE_THICKNESS+0.1
strain = MICROSCOPE_THICKNESS * 0.2
wait_time = 1.9
run_time = 0.1
a = TOP + strain
b = BOTTOM
c = (b-a)/4
n=0
# while n < 5:
#     pos base_y 32+0.5*n
#     staticscan ncddetectors
#     n= n+1
#

setSubdirectory("testdir/test1")