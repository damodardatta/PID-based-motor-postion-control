from pid_theta_ctrl import theta_rot

#defifing var to track angle of the encoder
thetacurr=0.0
#end of session flag and thetha
flag=1
thetaend=0.0
while flag:
    print("please enter target angle or q for ending session")
    thetasp=input()
    if (thetasp!='q'):
        thetasp=int(thetasp)
        theta_rot(thetasp)
    else:
        flag=0
#returning to 0 degrees
thetacurr=theta_rot(0)
print(thetacurr)
print('Done.')