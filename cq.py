from tkinter import *
import random as r
import threading
import time

#初始化窗口
窗=Tk()
窗.title("抽签")
窗.geometry('500x500')
窗.resizable(False,False)
窗.flag = True
#窗.iconbitmap('抽签.ico')
#none
菜单栏 = Menu(窗)

def about():
    关于=Tk()
    关于.title("关于抽签")
    关于.geometry("350x450")
    关于文本一=Label(关于,text='抽签 第五版',font = ("宋体", 20,"normal"))
    关于文本一.place(x=100,y=50,width=150,height=30)
    github=Label(关于,text='giuhub地址:',font = ("宋体", 20,"normal"))
    github.place(x=20,y=100,width=150,height=40)
    github2=Label(关于,text='https://github.com/tianr-r/pytk_cq',font = ("宋体",12,"normal"))
    github2.place(x=20,y=150,width=300,height=30)
    by=Label(关于,text='by tianr',font = ("宋体", 20,"normal"))
    by.pack()
def settings():
    设置=Tk()
    设置.title("抽签设置")
    设置.geometry("350x450")
    设置文本=Label(设置,text='对于抽签的设置项',font = ("宋体", 20,"normal"))
    设置文本.place(x=20,y=20,width=300,height=100)

菜单项目= Menu(菜单栏, tearoff=0)
菜单栏.add_cascade(label='其他', menu=菜单项目)#容器
菜单项目.add_command(label="关于",command=about)
#.add_command(label='Open', command=none)
#菜单项目.add_command(label='Save', command=none)
菜单项目.add_separator()    # 添加一条分隔线
菜单项目.add_command(label='退出', command=窗.quit)

设置= Menu(菜单栏, tearoff=0)
菜单栏.add_cascade(label='设置', menu=设置)#容器
设置.add_command(label="未完成...",command=settings)
窗.config(menu=菜单栏)







抽签文本 = Label(窗,text='每日一抽，其乐无穷！',font = ("宋体", 20,"normal"))
抽签文本.place(x=100,y=20,width=300,height=70)
#三个Lable标签
名字_1 =      Label(窗,text='',font = ("宋体", 25,"normal"))
名字_1.place(x=180,y=200,width=150,height=100)
名字_1['fg'] = 'gray'
名字_2 =      Label(窗,text='',font = ("宋体", 25,"normal"))
名字_2['fg'] = 'gray'
名字_2.place(x=180,y=270,width=150,height=100)

名字_3 =      Label(窗,text='',font = ("宋体",50,"normal"))
名字_3.place(x=150,y=350,width=200,height=100)
名字_3['fg'] = 'black'

名组 = ['王馨尉','张慧','马爽','王钰博','辛梓同','狄畅','黄子轩','魏宇涵','刘春炜','柴汶溪','顾天诚','刘祉璠','靳旭','陈继涛','郑宇航','孟天威','张丹丹','丛熙','张族康','李俊皓','田在旭','赵嵘嘉','王皓鸣','邹宛蓉','关琳琦','康可馨','姜贺华','李鸿','曲仲博','孟祥慧','张沐琦','赵明辉','杜佳洁','陈弈妃','杜遥遥','李雨梦','姜宁','李斯禹','刘若彤','吕明聪','孙睿晗','王美骄','王科研','李明哲','邸子轩','陈劲池','赵旭阳','谷慧子','袁彩嘉']


def switch1():
    窗.flag=True
    while 窗.flag:
        i              =r.randint(0, len(名组)-1)
        名字_1['text']  =名字_2['text']
        名字_2['text'] =名字_3['text']
        名字_3['text']  =名组[i]
        time.sleep(999999)
        #窗.root=False
def switch2():
    窗.flag=True
    while 窗.flag:
        i              =r.randint(0, len(名组)-1)
        名字_1['text']  =名字_2['text']
        名字_2['text'] =名字_3['text']
        名字_3['text']  =名组[i]
        time.sleep(0.1)
        #窗.root=False

#开始按钮
def 按钮开始():
    窗.root=True
    t=      threading.Thread(target=switch1)
    t.start()
开始=   Button(窗,text='开始',bg="green",font=('宋体', 20),command=按钮开始)#定义
开始.place(x=20, y=100, width=150, height=50)#放置

#结束按钮
def 按钮结束():
    窗.flag=False#状态

结束=    Button(窗,text='停止',bg="#ff3838",font=('宋体', 20),command=按钮结束)#定义
结束.place(x=330, y=100, width=150, height=50)#放置

#滚动抽签
def 滚动抽签():
    窗.root=True
    t=      threading.Thread(target=switch2)
    t.start()
滚动=   Button(窗,text='滚动',bg="#75ff3a",font=('宋体', 20),command=滚动抽签)#定义
滚动.place(x=175, y=100, width=150, height=50)#放置




窗.mainloop()