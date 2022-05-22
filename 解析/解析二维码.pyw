#模块引入
import os
import time
import psutil
import tkinter as tk
import pyzbar
import pyzbar.pyzbar as pyzbar
from PIL import ImageFilter
from PIL import Image,ImageEnhance
from tkinter import filedialog,END, INSERT, RAISED, SUNKEN
from PIL.ImageFilter import EMBOSS, CONTOUR,BLUR,DETAIL,EDGE_ENHANCE,FIND_EDGES,SMOOTH,SHARPEN



#主窗体
window = tk.Tk()
window.title('解析二维码')
window.geometry('350x300')
window.configure(bg = 'aquamarine')

#定义函数
def choose():
    explore = tk.Tk()                                           #打开资源管理器窗口
    explore.withdraw() 
    start = time.time()                                         #运行计时                          
    image = filedialog.askopenfilename()                        #选择文件
    img = Image.open(image)
    #处理图片
    img = ImageEnhance.Brightness(img).enhance(1.0)             #调整亮度        0~1~无穷
    img = ImageEnhance.Sharpness(img).enhance(1.0)              #锐利化          0~1~2
    img = ImageEnhance.Contrast(img).enhance(1.0)               #调整对比度      0~1~无穷
    img = ImageEnhance.Color(img).enhance(1.0)                  #调整色彩平衡    0~1~无穷
    #img = img.filter(BLUR)                                     #BLUR：模糊图像
    #img = img.filter(CONTOUR)                                  #CONTOUR：提取图像中的轮廓信息
    #img = img.filter(DETAIL)                                   #DETAIL：使得图像中细节更加明显
    #img = img.filter(EMBOSS)                                   #EMBOSS：使图像呈现出浮雕效果
    #img = img.filter(EDGE_ENHANCE)                             #EDGE_ENHANCE：突出、加强和改善图像中不同灰度区域之间的边界和轮廓
    #img = img.filter(FIND_EDGES)                               #FIND_EDGES：突出边缘信息
    #img = img.filter(SMOOTH)                                   #SMOOTH：突出图像的宽大区域、低频成分和主干部分，或抑制图像噪声和高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量
    img = img.filter(SHARPEN)                                   #SHARPEN：补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
    texts = pyzbar.decode(img)                                  #解析到信息
    if texts == []:
        result = '此图片不包含二维码,请重试或更换'
    else:                                              
        for text in texts:                                      #查找输出结果
            content = text.data.decode("utf-8")
            result = "二维码中的内容是:\n{:\0^39}".format(content)
    print(texts)                                                #data-内容；type-类型；rect-尺寸;polygon-边角定位点；quality-质量；orientation-方向
    end = time.time()
    tk.messagebox.showinfo(title="提示",message="解析完成！")    #弹窗提醒
    runtime = end - start
    runtime = "解析用时:{:.2f}s".format(runtime)                #解析内容格式化
    
    showarea1.config(state='normal')
    showarea1.insert(INSERT,'\n')                               #输出
    showarea1.insert(INSERT,result)
    showarea1.config(state='disabled')
    showarea2.config(state='normal')
    showarea2.insert(INSERT,'\n')
    showarea2.insert(INSERT,runtime)
    showarea2.config(state='disabled')

def close():                                         #通过kill进程完全关闭软件
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == '解析二维码.exe':
            cmd = 'taskkill /F /IM 解析二维码.exe'
            os.system(cmd)

def eraser():
    showarea1.config(state='normal')
    showarea1.delete('1.0','end')
    showarea1.config(state='disabled')
    showarea2.config(state='normal')
    showarea2.delete('1.0','end')
    showarea2.config(state='disabled')
    
#创建控件
button1 = tk.Button(window,bg='honeydew',text='选择二维码\n并解析',command = choose,relief = RAISED,font=('隶书',14))
button2 = tk.Button(window,bg='honeydew',text=' 完全 \n 退出 ',command = close,relief = RAISED,font=('隶书',13))
button3 = tk.Button(window,bg='honeydew',text='清空\n显示区',command = eraser,relief = RAISED,font=('隶书',13))
showarea1 = tk.Text(window,bg = 'whitesmoke',font = ('隶书',12),width = 39,height = 9,exportselection = True,relief = RAISED)
showarea2 = tk.Text(window,bg = 'paleturquoise',font = ('隶书',12),width = 16,height = 3,exportselection = True,relief = RAISED)

#放置控件
button1.place(relx=0.05,rely=0.1)
button2.place(relx=0.8,rely=0.01)
button3.place(relx=0.8,rely=0.18)
showarea1.place(relx=0.05,rely=0.35)
showarea2.place(relx=0.40,rely=0.1)

#主窗口循环
window.mainloop()
