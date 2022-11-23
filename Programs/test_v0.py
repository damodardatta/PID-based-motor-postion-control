from pid_theta_ctrl import theta_rot

#defifing var to track angle of the encoder
thetacurr=0.0
#end of session flag and thetha
flag=1
thetaend=0.0
while flag:
    print("please enter target angle or q for ending session")
    thetasp=input()
    if ((thetasp=='q')):                                                   
        break
    thetasp=float(thetasp)%360
    if (thetacurr>thetasp):
        thetacurr=thetacurr+theta_rot((thetasp-thetacurr))
        print(thetacurr)
    else:
        thetacurr=theta_rot(thetasp-thetacurr)+thetacurr
        print(thetacurr)
#returning to 0 degrees
thetacurr=thetacurr+theta_rot((-1*thetacurr))
print(thetacurr)
print('Done.')