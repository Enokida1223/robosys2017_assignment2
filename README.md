# robosys2017_assignment2
１５２６０２4　榎田真琴

RaspberryPi3でカウント機能とLED点灯
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
+ カウントを行う
 
+ LEDを光らせる  
`echo 1 > /dev/myled0`
+ LEDを消す  
`echo 0 > /dev/myled0`

## Reference/Quotation
[ロボットシステム学 講義資料](https://github.com/ryuichiueda/robosys2017/blob/master/12.md)
