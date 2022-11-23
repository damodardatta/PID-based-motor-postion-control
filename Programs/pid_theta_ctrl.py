# Importing modules and classes
import time
import numpy as np
from utils import plot_line
from gpiozero_extended import Motor, PID
import logging

def theta_rot(thetasp,kp = 0.08,ki = 0.4,kd = 0.01):
    #logging start
    log = logging.getLogger()
    logging.basicConfig(filename="angle.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')
    # Creating an logger object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    def get_line(f=open('angle.log'), cache=['']):
        for cache[0] in f:
            pass
        return cache[0][:-1]
    thetacurr=get_line()
    log_lastline=thetacurr.split(" ")
    try:
        theta_prev=float(log_lastline[2])
        print("Hello")
        print(theta_prev)
    except:
        theta_prev=0
    # Setting general parameters
    tstop = 3  # Execution duration (s)
    tsample = 0.01  # Sampling period (s)
    #thetasp = 45  # Motor position set point (deg)
    tau = 0.1  # Speed low-pass filter response time (s)
    thetasp = thetasp-theta_prev
    # Creating PID controller object
    
    taupid = 0.01
    pid = PID(tsample, kp, ki, kd, tau=taupid)

# Creating motor object using GPIO pins 16, 17, and 18
# (using SN754410 quadruple half-H driver chip)
# Integrated encoder on GPIO pins 24 and 25.
    mymotor = Motor(
        enable1=25, pwm1=24, pwm2=23,
        encoder1=20, encoder2=21, encoderppr=400)
#mymotor.reset_angle()

# Pre-allocating output arrays
    t = []  # Time (s)
    theta = []  # Measured shaft position (deg)
    u = []  # Controler output

# Initializing variables and starting clock
    thetaprev = 0
    tprev = 0
    tcurr = 0
    tstart = time.perf_counter()

# Running execution loop
    print('Running code for', tstop, 'seconds ...')
    print(theta_prev,thetasp)
    while tcurr <= tstop:
    # Pausing for `tsample` to give CPU time to process encoder signal
        time.sleep(tsample)
    # Getting current time (s)
        tcurr = time.perf_counter() - tstart
    # Getting motor shaft angular position: I/O (data in)
        thetacurr = mymotor.get_angle()
    # Calculating closed-loop output
        ucurr = pid.control(thetasp, thetacurr)
    # Assigning motor output: I/O (data out)
        mymotor.set_output(ucurr)
    # Updating output arrays
        t.append(tcurr)
        theta.append(thetacurr)
        u.append(ucurr)
    # Updating previous values
        thetaprev = thetacurr
        tprev = tcurr
        logger.info(thetacurr+theta_prev)

    #print('Done.')
# Stopping motor and releasing GPIO pins
    mymotor.set_output(0, brake=True)
    del mymotor
    #log.removeHandler(logger)
    return thetacurr