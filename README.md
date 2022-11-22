# PID-based-motor-postion-control
Controlling motor angular position through PID controller.

it used a PID controller, Please find the reference for PID class written from : https://github.com/EduardoNigro/Things-DAQ-Code

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

The motor and rotary encoder are coupled together. For the PID controller, motor angle is the input and motor current is the output whereas Encoder angle feedback acts as the comparator.

![setup_raw](https://user-images.githubusercontent.com/33845372/203399062-45303972-a7c2-479f-92cf-bf778ae7c705.jpeg)

