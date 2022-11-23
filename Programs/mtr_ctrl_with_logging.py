""" post_motor_position_control_step.py

Contains the example code to run a DC motor that has an integrated shaft
encoder as a closed-loop position system with a PID controller.
A step input is applied and can be used to tune the PID gains.
https://thingsdaq.org/2022/05/15/motor-position-control-with-raspberry-pi/

Run this in a terminal instead of an interactive window.

Author: Eduardo Nigro
    rev 0.0.1
    2022-05-15

"""
# Importing modules and classes
import time
import numpy as np
from utils import plot_line
from gpiozero_extended import Motor, PID
import matplotlib.pyplot as plt
import numpy as np
import logging

#logging start
logging.basicConfig(filename="angle.log",
                    format='%(asctime)s %(message)s',
                    filemode='r+')
 
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
tstop = 2  # Execution duration (s)
tsample = 0.01  # Sampling period (s)
thetasp = 180-theta_prev  # Motor position set point (deg)
tau = 0.1  # Speed low-pass filter response time (s)

# Creating PID controller object
kp = 0.08
ki = 0.4
kd = 0.01
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

print('Done.')
# Stopping motor and releasing GPIO pins
mymotor.set_output(0, brake=True)
del mymotor
#np_theta=np.array(theta)
#np_time=np.array(t)
#lines=plt.plot(np_time, np_theta)
#plt.setp(lines, color='r', linewidth=2.0)
# Plotting results
#plot_line(
 #   [t]*2, [theta, u], marker=True, axes='multi',
  #  yname=['Shaft Position (deg.)', 'Control Output (-)'])
#plot_line(t[1::], 1000*np.diff(t), marker=True, yname='Sampling Period (ms)')
