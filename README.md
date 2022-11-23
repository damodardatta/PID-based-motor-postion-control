# PID-based-motor-postion-control
Controlling motor angular position through PID controller.

it used a PID controller, Please find the reference for PID class and motor control example code written from : https://github.com/EduardoNigro/Things-DAQ-Code

For trying the code you can check inside Programs folder test.py
  cd Programs
  python test.py

### List of items used:
1) Dc motor : 100RPM, 3-12V, 140mA.
2) Raspberry pi 3B+
3) Motor driver L298M : 5-35V, 2A
4) Power Supply : 12 VDC
5) Rotary Encoder: min 400PPR, 5-24V, 40mA

![setup](https://user-images.githubusercontent.com/33845372/203396730-39b56581-41cd-4ea2-a9ea-ebb113f86981.png)

### Circuit Diagram:

![circuit](https://user-images.githubusercontent.com/33845372/203396927-27ed0dfb-df00-4f82-9bfe-efe0f2bb7ff1.jpeg)

### Hardware and controller Explanation 

The motor and rotary encoder are coupled and housed together. For the PID controller, motor angle is the input and motor current is the output whereas Encoder angle feedback acts as the comparator.

![setup_raw](https://user-images.githubusercontent.com/33845372/203401452-c480c8dc-db60-4d90-b4b7-5d24c56b43fe.jpeg)

![Untitled Diagram drawio(2)](https://user-images.githubusercontent.com/33845372/203536631-873996b6-c4e5-491f-ab9f-4e20f51ce0dd.png)


 The output $m_n$ of a PID controller obeys the equation $$ m_n = k_p*e_n + \frac{k_e*T}{T_{reset}}\sum_{i=0}^{n}e_i + k_d\frac{e_n - e_{n-1}}{\delta t} + m_{R}$$ where $m_n$ is the output of the controller at the {\em n}th sampling instant, $m_R$ is the reference value at which the control action is initialized, $e_n$ is the value of the error at the {\em n}th sampling instant, $T_{reset}$ is the reset or integral time, $kp$ and $kd$ are the proportional and derivate gains respectively.


Enocoder 1 and 2, also ppr values are used to calculate the angles in the following in the mtr_ctrl_with_logging.py program

https://github.com/damodardatta/PID-based-motor-postion-control/blob/cd5bb9bed4415cf83b7bb9033c9c0a805efd7129/Programs/mtr_ctrl_with_logging.py#L60-L62


