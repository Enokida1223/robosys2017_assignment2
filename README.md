# robosys2017_assignment2
１５２６０２4　榎田真琴

RaspberryPi3でカウント機能とLED点灯  
講義で行ったroslaunchを用いて＋２ずつカウント  
PWM制御でLEDの点滅  
## Demo
[カウントとLチカ（PWM）](https://youtu.be/A7AUHAlWvvs)
## Requirements
+ RaspberryPi3
  + Ubuntu
+ LED  
+ 抵抗器(10Ω)  
## Circuit
![](https://github.com/Enokida1223/robosys2017_assignment2/blob/master/IMG_7233.JPG)　
## Usage
+ roslaunchを実行  
 `roslaunch mypkg mypkg.launch`
+ カウントを行う  
 `rostopic echo /twice`
+ LEDを光らせる   
`rosrun mypkg led.py`
## Reference/Quotation
[ロボットシステム学 講義資料](https://github.com/ryuichiueda/robosys2017/blob/master/12.md)
