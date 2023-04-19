# Random-text-with-countdown-floating-window
一个基于python3.8和PySide2的桌面悬浮窗倒计时的软件，倒计时附带随机文本，可以用来背点东西？   
需要python的环境变量   
需要PySide2库
```
pip install PySide2
```
需要datetime库
```
pip install datatime
```

——————————

目前没有鼠标穿透，并不会一直置于最顶层，可以挂在桌面看。  
没法移动，没法设置大小，更改只能改 `main.py` 文件里的参数。  
启动后只能通过任务管理器找到进程进行关闭。  
还有一堆未知BUG。

——————————

WuW制作， 偷税定制版（dog）  
单词库来自 https://www.bilibili.com/read/cv15568162

## 更新日志
### 0.0.1版本
- 优化了随机取值，采用队列剔除，防止伪随机随机性不够导致的取不到某个值。
- 优化了一点位置。
- 单词库添加了音标文件。
- 每个单词的持续时间进行了优化，现在是根据单词长度来设定的切换时间，目前是**单词长度\*3**
