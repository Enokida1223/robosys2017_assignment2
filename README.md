# robosys2017_assignment2
RaspberryPi3でカウント機能とLED点灯
## Demo
[動画のタイトル](動画のURL)
## Requirements
+ RaspberryPi3
  + Raspbian
+ linux kernel sorce  
  + `/usr/src/linux`をダウンロード  
  + kernel build scripts:https://github.com/ryuichiueda/raspberry_pi_kernel_build_scripts  
+ LED  
+ 抵抗器(10Ω)  
## Circuit
![](回路の画像のURL)　//これはお好み
## Usage
+ LEDを光らせる  
`echo 1 > /dev/myled0`
+ LEDを消す  
`echo 0 > /dev/myled0`
+ 寿司を大量に表示させる  
`cat /dev/myled0`
## Reference/Quotation
[ロボットシステム学 講義資料](https://github.com/ryuichiueda/robosys2017/blob/master/07.md)
