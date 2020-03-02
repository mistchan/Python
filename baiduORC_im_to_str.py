# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:37:38 2018
利用百度api实现指定文件夹内所有图片转换为文本

选择有目标图片的文件夹
"""

import glob
import os
import sys
import tkinter
import tkinter.filedialog
from os import path

from PIL import Image
from aip import AipOcr

sys.path.append('E:/analyze_app')
from pwd import Pwd


def convertimg(picfile, outdir):
    '''调整图片大小，对于过大的图片进行压缩
    picfile:    图片路径
    outdir：    图片输出路径
    '''
    img = Image.open(picfile)
    width, height = img.size
    while (width * height > 4000000):  # 该数值压缩后的图片大约 两百多k
        width = width // 2
        height = height // 2
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(path.join(outdir, os.path.basename(picfile)))


def baiduOCR(picfile, outfile):
    """利用百度api识别文本，并保存提取的文字
    picfile:    图片文件名
    outfile:    输出文件
    """
    filename = path.basename(picfile)

    APP_ID = Pwd().baidu_pwd()["APP_ID"]
    API_KEY = Pwd().baidu_pwd()["API_KEY"]
    SECRECT_KEY = Pwd().baidu_pwd()["SECRECT_KEY"]
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    # message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    message = client.basicAccurate(img)  # 通用文字高精度识别，每天 800 次免费
    print("识别成功！")
    i.close()

    with open(outfile, 'a+') as fo:
        # 输出文本内容
        for text in message.get('words_result'):
            fo.writelines(text.get('words'))

    print("文本导出成功！")


root = tkinter.Tk()
root.title('请选择结果图片文件夹:')
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

ww = 500
wh = 50
root.geometry("%dx%d+%d+%d" % (ww, wh, (sw - ww) / 2, (sh - wh) / 2))


def c():
    global dir_im

    root.update()
    dir_im = tkinter.filedialog.askdirectory()
    root.destroy()
    return dir_im


tkinter.Button(root, text='选择目标文件夹', command=c, width=15, height=2,

               activebackground='grey', relief='groove').pack()
root.mainloop()

if __name__ == "__main__":

    for picfile in glob.glob(dir_im + '\\*'):
        baiduOCR(picfile, 'outfile.txt')
    os.startfile('outfile.txt')
