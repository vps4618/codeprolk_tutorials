import pyautogui,time
def vishwa(arg1,arg2):#at first def keyword shoud be given.then name and wanted arguments.then press enter and give what to do with this function
    print(arg1,arg2)
vishwa(1,"v")    

def click(picture):
    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    b=pyautogui.center(a)  
    x,y=b
    pyautogui.click(x, y)
    time.sleep(3)
    
click("windows button.png")
click("settings.png")
click("time.png")
click("sync.png")