from MyQR import myqr
import tkinter as tk
from tkinter import filedialog,END, INSERT, RAISED, SUNKEN
import tkinter.messagebox
import time

 #主窗体
window = tk.Tk()
window.title('二维码生成器v1.0 By BUCTPJP')
window.geometry('500x200')
window.configure(bg = 'lemonchiffon')

 #定义函数

def produce():
    start = time.time()

    content = e1.get()
    saved = e2.get()

    explore = tk.Tk()
    explore.withdraw()
    img = filedialog.askopenfilename()
    print(img)

    myqr.run(
        words=content,                             # 扫描二维码后，显示的内容，或是跳转的链接
        version=5,                                 # 设置容错率
        level='H',                                 # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture=img,                               # 图片所在目录，可以是动图
        colorized=True,                            # 黑白(False)还是彩色(True)
        contrast=1.0,                              # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
        brightness=1.0,                            # 用来调节图片的亮度，用法同上。
        save_name=saved,                           # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )

    end = time.time()
    tk.messagebox.showinfo(title="提示",message="成功生成！")
    a = end - start
    runtime = "生成用时：{:.2f}s".format(a)

    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,runtime) 

 #创建控件
showarea = tk.Text(window,bg = 'palegreen',font = ('隶书',12),width = 20,height = 3,exportselection = True,relief = RAISED)
tip1 = tk.Label(window,bg='lightcyan',text='请输入二维码要显示的内容：',font = ('楷体',12),padx=5,pady=5)
e1 = tk.Entry(window,cursor = 'xterm',relief = SUNKEN,width=30)
tip2 = tk.Label(window,bg='lightcyan',text='请输入生成二维码的文件名：',font = ('楷体',12),padx=5,pady=5)
e2 = tk.Entry(window,cursor = 'xterm',relief = SUNKEN,width=30)
button = tk.Button(window,bg='honeydew',text='选择背景图片并生成',command = produce,relief = RAISED,font=('隶书',14))

 #放置控件
showarea.place(relx=0.37,rely=0.58)
tip1.place(relx=0.05,rely=0.1)
e1.place(relx=0.5,rely=0.1)
tip2.place(relx=0.05,rely=0.26)
e2.place(relx=0.5,rely=0.26)
button.place(relx=0.35,rely=0.42)

 #主窗口循环显示
window.mainloop()