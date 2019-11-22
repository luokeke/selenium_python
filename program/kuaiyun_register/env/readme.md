## Selenium自动化测试环境搭建（windows) ##

	1、安装Anaconda（一个用于科学计算的python发行版），安装完成之后请将安装的路径添加到系统环境变量,如：
		***(其他环境变量);D:\Anaconda2;D:\Anaconda2\Scripts;

	2、安装Pycharm (一个python的IDE)

	3、将pytesser_v0.0.1目录整个拷贝至任意磁盘位置，然后将该目录的路径设置到系统环境变量，如：
		***(其他环境变量);D:\pytesser_v0.0.1;

	4、安装如下用到的轮子：
		pip install opencv-python
		pip install pytesseract
		pip install selenium

	5、将browser driver/chromedriver_win32目录下的chromedriver.exe拷贝至anaconda的安装目录下	

	6、至此基本环境已搭建完成，可以开始使用pycharm编写自动化测试脚本了