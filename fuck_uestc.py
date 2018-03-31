import win32api
import win32gui
import win32con
import time
import ctypes
# 只适用于windows平台，服务器需要在VNC方式下登陆使用，不然在mstsc方式下下线即自动熄屏，无法自动触发点击动作.
def click1(x,y):
	win32api.SetCursorPos((x,y)) 
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0) 
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def make_sure_secure():
	for i in range(8):
		win32api.keybd_event(13,0,0,0)     # 按下回车取消alert弹窗
		win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
		time.sleep(1)
for i in range(100):
	try:
		make_sure_secure();
		click1(120,160)
		time.sleep(5640)
	except Exception as e:
		print(e)
