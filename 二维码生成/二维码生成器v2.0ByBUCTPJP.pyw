from fileinput import close
import qrcode
import tkinter as tk
from tkinter import filedialog,END, INSERT, RAISED, SUNKEN
from PIL import Image
import time
import psutil
import os

 #主窗体
window = tk.Tk()
window.title('二维码生成器v2.0 By BUCTPJP')
window.geometry('850x300')
window.configure(bg = 'aquamarine')

 #函数部分
def produce():
    start = time.time()                                         #开始计时
    string = e1.get()                                           #获取用户输入内容
    saved = e2.get()
    color = e3.get()                                            #获取用户输入内容
    qr = qrcode.QRCode(
            version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
            box_size=8,                                         # 控制二维码中每个小格子包含的像素数
            border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
    )
    qr.add_data(string)
    qr.make(fit=True)                                           #使用make方法生成
    img = qr.make_image() 
    img = qr.make_image(fill_color=color, back_color='white')  # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
    img.save(saved)                                             #保存二维码
    end = time.time()                                           #结束计时
    tk.messagebox.showinfo(title="提示",message="成功生成！")    #弹窗提醒
    a = end - start
    runtime = "生成用时：{:.2f}s".format(a)                      

    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,runtime)                             #显示二维码生成用时

def logo():
    start = time.time()

    string = e1.get()
    saved = e2.get()
    color = e3.get()
    qr = qrcode.QRCode(
            version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
            box_size=8,                                         # 控制二维码中每个小格子包含的像素数
            border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image() 
    img = qr.make_image(fill_color=color, back_color='white')  # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
    
    explore = tk.Tk()                                          #打开资源管理器窗口
    explore.withdraw()                             
    image = filedialog.askopenfilename()                       #选择文件
    icon = Image.open(image).convert('RGBA')                   #转换为RGBA4通道
    img_w, img_h = img.size                                    #获得二维码尺寸
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:                                        #调整logo图片大小
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h))
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)                              #将logo图片贴在二维码指定位置
    img.save(saved)                                            #保存

    end = time.time()
    tk.messagebox.showinfo(title="提示",message="成功生成！")
    a = end - start
    runtime = "生成用时：{:.2f}s".format(a)

    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,runtime)


def bg():
    start = time.time()

    string = e1.get()
    saved = e2.get()
    color = e3.get()
    qr = qrcode.QRCode(
            version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
            box_size=8,                                         # 控制二维码中每个小格子包含的像素数
            border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image() 
    img = qr.make_image(fill_color=color, back_color='white')  # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
    img = img.convert('RGBA')

    explore = tk.Tk()
    explore.withdraw()
    image = filedialog.askopenfilename()
    background = Image.open(image).convert('RGBA')
    img_w, img_h = img.size
    color_0 = img.getpixel((0,0))                                 #改变二维码图片背景透明度
    for h in range(img_h):
        for l in range(img_w):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot,color_1)

    background_w,background_h = background.size                  #获得背景图片尺寸
    if background_w != img_w:                                    #改变背景图片大小与二维码一致
        background_w = img_w
    if background_h != img_h:
        background_h = img_h
    background = background.resize((background_w, background_h))
    background.paste(img,(0,0),img)                              #将二维码贴在背景图片上
    background = background.convert('RGB')                       
    background.save(saved)

    end = time.time()
    tk.messagebox.showinfo(title="提示",message="成功生成！")
    a = end - start
    runtime = "生成用时：{:.2f}s".format(a)

    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,runtime)

def close():                                                     #解决关闭软件后进程残留问题，关闭进程
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == '二维码生成器v2.0ByBUCTPJP.exe':
            cmd = 'taskkill /F /IM 二维码生成器v2.0ByBUCTPJP.exe'
            os.system(cmd)

 #创建控件
tip1 = tk.Label(window,bg='lightcyan',text='请输入二维码要显示的内容:',font = ('楷体',12),padx=5,pady=5)
e1 = tk.Entry(window,cursor = 'xterm',relief = SUNKEN,width=80)
tip2 = tk.Label(window,bg='lightcyan',text='请输入二维码要保存的文件名:',font = ('楷体',12),padx=5,pady=5)
e2 = tk.Entry(window,cursor = 'xterm',relief = SUNKEN,width=30)
tip3 = tk.Label(window,bg='lightcyan',text='请输入二维码想要的颜色:',font = ('楷体',12),padx=5,pady=5)
e3 = tk.Entry(window,cursor = 'xterm',relief = SUNKEN,width=20)
tip4 = tk.Text(window,bg = 'aquamarine',font = ('隶书',12),width = 55,height = 2,exportselection = True,relief = RAISED)
tip4.insert(INSERT,'       输入英文,参照如下网址(可以使用CTRL+V复制)\nhttps://blog.csdn.net/Koyurion/article/details/85857344')
tip4.config(state='disabled')
button1 = tk.Button(window,bg='honeydew',text='直接生成',command = produce,relief = RAISED,font=('隶书',14))
button2 = tk.Button(window,bg='honeydew',text='选择log并生成',command = logo,relief = RAISED,font=('隶书',14))
button3 = tk.Button(window,bg='honeydew',text='选择背景并生成',command = bg,relief = RAISED,font=('隶书',14))
button4 = tk.Button(window,bg='honeydew',text='完全退出程序',command = close,relief = RAISED,font=('华文新魏',14))
showarea = tk.Text(window,bg = 'palegreen',font = ('隶书',12),width = 20,height = 3,exportselection = True,relief = RAISED)

 #放置控件
tip1.place(relx=0.02,rely=0.1)
e1.place(relx=0.3,rely=0.1)
tip2.place(relx=0.02,rely=0.25)
e2.place(relx=0.3,rely=0.25)
tip3.place(relx=0.02,rely=0.4)
e3.place(relx=0.3,rely=0.4)
tip4.place(relx=0.475,rely=0.38)
button1.place(relx=0.05,rely=0.55)
button2.place(relx=0.25,rely=0.55)
button3.place(relx=0.5,rely=0.55)
button4.place(relx=0.78,rely=0.55)
showarea.place(relx=0.35,rely=0.75)


 #主窗口循环
window.mainloop()
