#setTitle("Water_Test_2min")
#from gdaserver import ncddetectors

#trig = 10.0 ; # %
print "script running"
#diodeReading = d10d2.getPosition()

#pos eh_shutter "Open"

import time
# import numpy as np
n = 0

TOP = 32.76
MICROSCOPE_THICKNESS = 2
SAMPLE_NAME = "UK_06_R5_S2_1"


BOTTOM = 34.9
# BOTTOM = TOP+MICROSCOPE_THICKNESS+0.1


##
## RICHIE DO NOT TOUCH BELOW
##
def run_line_scan(a,c, run_number, strain_pos):
    counter = 0
    setSubdirectory(SAMPLE_NAME+"/strain_" + str(strain_pos)+ "_line_" + str(run_number))
    while counter < 5:
        setTitle(str(strain_pos) + "% strain no: " + str(run_number) + " pos " + str(a+c*counter))
        pos base_y a+c*counter
        # print("pos base_y " + str(a+c*counter)) 
        # print("staticscan ncddetectors")
        
        # Catch exceptions caused by the staticscan
        try:
            staticscan ncddetectors
        except java.lang.Exception:
            print "Exception caught, continuing script"
        
        counter += 1
    # print("pos base_y " + str(a))
    pos base_y a
    
    
strain = MICROSCOPE_THICKNESS * 0.2
a = TOP + strain
b = BOTTOM
c = (b-a)/4
sleep_time = 60
loop_time = 920
n=0
all_scan_times = []

# DO the first scan - this will start the triggering system
# setTitle("20% strain no: " + str(n))

n=n+1
# scan base_y a b c ncddetectors
run_line_scan(a, c, 0, 20)
initial_time = time.time()
total_accumulated_time = 0
max_cycle_time = 0
average_cycle_time = 0
# Do three more initial scans with no waiting time between
while n < 4:
    # setTitle("20% strain no: " + str(n))
    scan_start_time = time.time()
    # scan base_y a b c ncddetectors
    run_line_scan(a, c, n, 20)
    time_to_scan = time.time() - scan_start_time
    all_scan_times.append(time_to_scan)
    print("Timed: " + str(time_to_scan))
    elapsed_time = time.time() - initial_time
    average_cycle_time = sum(all_scan_times)/len(all_scan_times)
    max_cycle_time = max(all_scan_times)
    total_accumulated_time = elapsed_time  + average_cycle_time
    n=n+1
# Now keep running scans with a minute in between until time reaches 920 seconds
while total_accumulated_time < loop_time - max_cycle_time:
        # print "scan base_y " +  str(a) + " " + str(b) + " " + str(c)+  " ncddetectors"
    # setTitle("20% strain no: " + str(n))
    
    # setTitle("20% strain no: " + str(n))
    scan_start_time = time.time()
    run_line_scan(a, c, n, 20)
    # scan base_y a b c ncddetectors
    time_to_scan = time.time() - scan_start_time
    all_scan_times.append(time_to_scan)
    print("Timed: " + str(time_to_scan))
    elapsed_time = time.time() - initial_time
    average_cycle_time = sum(all_scan_times)/len(all_scan_times)
    max_cycle_time = max(all_scan_times)
    total_accumulated_time = elapsed_time  + average_cycle_time
    remaining_time = loop_time - total_accumulated_time
    sleep_this_cycle = min([remaining_time, sleep_time])
    if sleep_this_cycle > 0:
        print("Sleeping for: "+ str(int(sleep_this_cycle)) + " seconds")
        time.sleep(sleep_this_cycle)
    n=n+1
    total_accumulated_time = time.time() - initial_time  + average_cycle_time
total_accumulated_time = time.time() - initial_time  + average_cycle_time
if loop_time - total_accumulated_time > 0:
    time.sleep(loop_time - total_accumulated_time)
print("Finishing 20% strain at: " + time.strftime("%H:%M:%S"))
print("##########\n\n")
print("Statistics for 20% strain :")
print("Mean scan time: " + str(average_cycle_time))
# print("Standard deviation scan time: " + str(np.array(all_scan_times).std()))
print("\n\n")
print("##########")
print("Moving onto 40% strain")
# Now we do the 40% strain. It will start immediately so do not need to log average time per cycle

a= TOP+2*strain
c = (b-a)/4
initial_time = time.time()
n=0
while n < 4:
    # setTitle("40% strain no: " + str(n))
    # scan base_y a b c ncddetectors
    run_line_scan(a,c,n, 40)
    n=n+1
total_accumulated_time = time.time() - initial_time
while total_accumulated_time < loop_time - max_cycle_time:
        # print "scan base_y " +  str(a) + " " + str(b) + " " + str(c)+  " ncddetectors"
    # setTitle("20% strain no: " + str(n))
    
    # setTitle("40% strain no: " + str(n))
    run_line_scan(a,c,n,40)
    # scan base_y a b c ncddetectors
    total_accumulated_time = time.time() - initial_time
    remaining_time = loop_time - total_accumulated_time
    sleep_this_cycle = min([remaining_time, sleep_time])
    if sleep_this_cycle > 0:
        print("Sleeping for: "+ str(int(sleep_this_cycle)) + " seconds")
    
        time.sleep(sleep_this_cycle)
    n=n+1
    total_accumulated_time = time.time() - initial_time
print("Completed " + str(n+1) + " cycles for 40% strain.")

a= TOP+3*strain
c = (b-a)/4
initial_time = time.time()
n=0
while n < 4:
    # setTitle("60% strain no: " + str(n))
    # scan base_y a b c ncddetectors
    run_line_scan(a,c,n,60)
    n=n+1
total_accumulated_time = time.time() - initial_time
while total_accumulated_time < loop_time - max_cycle_time:
        # print "scan base_y " +  str(a) + " " + str(b) + " " + str(c)+  " ncddetectors"
    # setTitle("20% strain no: " + str(n))
    
    # setTitle("60% strain no: " + str(n))
    # scan base_y a b c ncddetectors
    run_line_scan(a,c,n,60)
    total_accumulated_time = time.time() - initial_time
    remaining_time = loop_time - total_accumulated_time
    sleep_this_cycle = min([remaining_time, sleep_time])
    if sleep_this_cycle > 0:
        print("Sleeping for: "+ str(int(sleep_this_cycle)) + " seconds")
        time.sleep(sleep_this_cycle)
    n=n+1
    total_accumulated_time = time.time() - initial_time
print("Completed " + str(n+1) + " cycles for 60% strain.")

print("All done")
# print("total time: " + str(time.time() - initial_time))
# n= 0 
# n_max_sleep = int((920 - 4*time_per_line)/(sleep_time+time_per_line))
# while n < n_max_sleep:
# #	if d10d2.getPosition() < 0.025:
#     # print "scan base_y " +  str(a) + " " + str(b) + " " + str(c)+  " ncddetectors"
#     setTitle("20% strain no: " + str(n+4))
#
#     scan base_y a b c ncddetectors
#     time.sleep(sleep_time)
#     # print("sleep: " + str(sleep_time))
#     n = n + 1 
# time.sleep(920 - (4*time_per_line + (time_per_line+sleep_time)*n_max_sleep))
# # print("sleep: " + str(920 - (4*time_per_line + (time_per_line+sleep_time)*n_max_sleep)) )
#
# print("Starting second compression at: " + time.strftime("%H:%M:%S"))
# #pos eh_shutter "Close"
# # n = 0
# # while n < 80:
# #     scan base_y 33.56 34.7 0.285 ncddetectors
# #     if n > 10:
# #         time.sleep(60)
# #     setTitle("MCLor100_HPC_Kinetic")
# #     n = n + 1 
# a_new = TOP+2*strain
# c_new = (b-a_new)/4
# time_per_line_new = (1+(b-a_new)/c_new)*(run_time+wait_time) + 2 * (b-a_new)
#
#
# n= 0
# while n < 4:
#         # print "scan base_y " +  str(a_new) + " " + str(b) + " " + str(c_new)+  " ncddetectors"
#     setTitle("40% strain no: " + str(n))
#
#     scan base_y a_new b c_new ncddetectors
#     n=n+1
#
# n= 0 
# n_max_sleep = int((920 - 4*time_per_line_new)/(sleep_time+time_per_line_new))
# while n < n_max_sleep:
# #    if d10d2.getPosition() < 0.025:
#     # print "scan base_y " +  str(a_new) + " " + str(b) + " " + str(c_new)+  " ncddetectors"
#     setTitle("40% strain no: " + str(n+4))
#
#     scan base_y a_new b c_new ncddetectors
#     time.sleep(sleep_time)
#     # print("sleep: " + str(sleep_time))
#     n = n + 1 
# time.sleep(920 - (4*time_per_line_new + (time_per_line_new+sleep_time)*n_max_sleep))
# # print("sleep: " + str(920 - (4*time_per_line_new + (time_per_line_new+sleep_time)*n_max_sleep)) )
#
#
# print "all done" 
