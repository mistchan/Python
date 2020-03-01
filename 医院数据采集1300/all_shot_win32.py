# -*- coding: utf-8 -*-
"""
Created on 2019.10.06

@author: mistchan

win32GUI1.0
"""

import pyautogui, os, time, shelve, sys, tkinter
from tkinter import *

from PIL import Image

if not os.path.isdir('.\\setup'):
    os.makedirs('.\\setup')
if not os.path.isdir('.\\wsetup'):
    os.makedirs('.\\wsetup')

pyautogui.PAUSE = 0.2


def setupapp():
    pyautogui.alert(text='现在运行设置向导，请跟着文字引导进行软件设置，也可以同时打开【设置手册】文件夹里【设置手册】文件，参考里面的图文设置指导', title='设置向导')  # 运行设置向导

    save = pyautogui.prompt(text='运行设置向导后将储存本次配置以备以后直接调用\n请输入需要保存的本次配置的名称，如【儿科急诊1电脑】的【全拼】，不要包含中文字符', title='储存配置名称',
                            default='jizhen1diannao')
    datasaved = shelve.open('.\\wsetup\\' + str(save))

    pyautogui.alert(text="现在请打开医院的软件，进入病人列表\n请将鼠标移至病人列表右侧空白处\n然后按【enter】键\n我们以后需要单击此处来重新获取焦点使列表可以下翻",
                    title='【1】获取焦点使列表下翻')
    time.sleep(0.5)
    Listdown = pyautogui.position()

    pyautogui.alert(text='现在获取扫描范围，扫描范围应包括全部医嘱药品列表\n请双击任意病人条目，进入医嘱列表;\n再双击第一条医嘱条目使医嘱列表最大化\n然后点击【enter】键',
                    title='获取扫描范围')
    pyautogui.alert(text='请将鼠标移至整个医嘱药品名称列表的左上角\n然后按【enter】键', title='【2】获取扫描范围')

    time.sleep(0.5)
    listLTx, listLTy = pyautogui.position()

    pyautogui.alert(text='现在请将鼠标移至整个医嘱药品名称列表右下角后按【enter】键', title='【3】获取扫描范围')
    time.sleep(0.5)
    listRBx, listRBy = pyautogui.position()

    listRegion = (listLTx, listLTy, listRBx - listLTx, listRBy - listLTy)

    pyautogui.alert(
        text='现在请鼠标移至第一条医嘱的开始日期和时间，例如：【2019.08.07 09:20:10】上，应避开刚才获取的扫描范围\n然后按【enter】键\n程序以后需要自动双击此处让医嘱列表最大化',
        title='【4】获取点击使医嘱列表最大化')
    time.sleep(0.5)
    orders1 = pyautogui.position()

    pyautogui.alert(text='现在获取住院号\n请将鼠标移至屏幕左上方住院号的左上角\n然后按【enter】键', title='【5】获取住院号')
    time.sleep(0.5)
    PatientIdLTx, PatientIdLTy = pyautogui.position()

    pyautogui.alert(text='现在请将鼠标移至住院号右下角后按【enter】键', title='【6】获取住院号')
    time.sleep(0.5)
    PatientIdRBx, PatientIdRBy = pyautogui.position()

    PatientIdRegion = (PatientIdLTx, PatientIdLTy, PatientIdRBx - PatientIdLTx, PatientIdRBy - PatientIdLTy)
    patientIdwidth = PatientIdRBx - PatientIdLTx

    pyautogui.alert(
        text='现在设置最终生成的单条信息的图片大小，长度应包含【药品名称、剂量、数量、用法、途径、单价、开嘱医生、停止时间、转抄、复核、停止医生】，宽度为一列医嘱的宽度。\n请任意选择一单列医嘱表格，将鼠标移至其左上起点\n然后按【enter】键。\n注意需包含完整药品名称',
        title='【7】设置最终生成的图片的大小')
    time.sleep(0.5)
    sLTx, sLTy = pyautogui.position()

    pyautogui.alert(text='请将鼠标移至此单列医嘱列表【停止时间、转抄、复核、停嘱医生】项目的右下角，然后按【enter】键', title='【8】设置最终生成的图片的大小')
    time.sleep(0.5)
    sRBx, sRBy = pyautogui.position()

    imWidth = sRBx - sLTx
    imHeight = sRBy - sLTy

    while True:
        pyautogui.alert(text="现在请将鼠标移至医嘱列表右上方'停嘱复核'下方【第一个】表格的最右侧框线上\n然后按【enter】键。\n我们判断此点是否为黑色。", title='【9】黑色框线')
        time.sleep(0.5)
        Blackline = pyautogui.position()

        if pyautogui.screenshot().getpixel(Blackline) == (0, 0, 0):
            break
        else:
            pyautogui.alert(text="选择错误！请重新选择", title='选择错误')

    while True:
        pyautogui.alert(text="现在请将鼠标移至医嘱列表最上方'发药属性'下面【第一个】'普  通'两字之间\n然后按【enter】键。\n我们判断此点是否为蓝色。", title='【10】首项是否为蓝色')
        time.sleep(0.5)
        BlueBar = pyautogui.position()

        if pyautogui.screenshot().getpixel(BlueBar) == (0, 0, 128):
            break
        else:
            pyautogui.alert(text="选择错误，请重新选择", title='选择错误')

    pyautogui.alert(text="现在请将鼠标移至医嘱列表下方'长期'前面的复选框中，然后按【enter】键。\n我们以后需要取消选择此复选框来取消显示长期医嘱。", title='【11】获取点击取消长期医嘱')
    time.sleep(0.5)
    cancellong = pyautogui.position()

    pyautogui.alert(text="再将鼠标移至'费用'前面的复选框中，然后按【enter】键,我们以后需要取消选择此复选框来取消显示费用医嘱", title='【12】获取点击取消费用医嘱')
    time.sleep(0.5)
    cancelfees = pyautogui.position()

    while True:
        pyautogui.alert(
            text="现在请将鼠标移至医嘱列表最右侧滚动条的黑色正三角形△上，然后按【enter】键,我们判断此点是否为白色。\n如果没有滚动条，请换一个有滚动条的病人再点击本窗口，然后将鼠标移至医嘱列表最右侧滚动条的黑色正三角形△上，再按【enter】键。",
            title='【13】是否有滚动条')
        time.sleep(0.5)
        RollBar = pyautogui.position()

        if pyautogui.screenshot().getpixel(RollBar) != (255, 255, 255):
            break
        else:
            pyautogui.alert(text="选择错误，请重新选择", title='选择错误')

    datasaved['listRegion'] = listRegion
    datasaved['imWidth'] = imWidth
    datasaved['imHeight'] = imHeight
    datasaved['PatientIdRegion'] = PatientIdRegion
    datasaved['patientIdwidth'] = patientIdwidth

    datasaved['orders1'] = orders1
    datasaved['cancellong'] = cancellong
    datasaved['cancelfees'] = cancelfees
    datasaved['Blackline'] = Blackline
    datasaved['RollBar'] = RollBar
    datasaved['BlueBar'] = BlueBar
    datasaved['Listdown'] = Listdown
    datasaved.close()

    pyautogui.alert(text='已完成设置，并储存为： ' + str(save) + ',按enter键后继续', title='设置已完成!')  # 设置完成

    global savedname
    savedname = str(save)


files = os.listdir('.\\wsetup')
setups = []
for eachs in files:
    if eachs[-4:] == '.dir':
        setups.append(eachs)

lv = tuple(setups)

root3 = Tk()
root3.title('选择配置文件')

sw3 = root3.winfo_screenwidth()
sh3 = root3.winfo_screenheight()

ww3 = 300
wh3 = 400
root3.geometry("%dx%d+%d+%d" % (ww3, wh3, (sw3 - ww3) / 2, (sh3 - wh3) / 2))

val = StringVar()
val.set(lv)
textv = StringVar()
textv.set('请从下列已存在的配置文件中点选需要的配置并加载：')
label1 = Label(root3, textvariable=textv)
label1.pack()
lb = Listbox(root3, listvariable=val, cursor='plus', bd=1, selectbackground='brown')

lb.pack()


def lc():
    global savedname

    lx = lb.get(lb.curselection())
    savedname = lx[:-4]
    root3.destroy()
    return savedname


def lcc():
    global savedname
    root3.destroy()
    setupapp()


bx = tkinter.Button(root3, text='加载配置', command=lc, width=10, height=1,

                    activebackground='grey', relief='groove')
bx.pack()

textv2 = StringVar()
textv2.set('\n如果现存配置不符合要求\n请点击下面按钮运行设置向导：\n')
label2 = Label(root3, textvariable=textv2)
label2.pack()
tkinter.Button(root3, text='运行设置向导', command=lcc, width=10, height=1,

               activebackground='grey', relief='groove').pack()

if setups == []:
    textv.set('未找到任何配置文件，请运行设置向导！')
    textv2.set('\n未找到任何配置文件，\n请点击下面按钮运行设置向导：')
    label1.config(state=tkinter.DISABLED)

    lb.config(state=tkinter.DISABLED)
    bx.config(state=tkinter.DISABLED)
root3.mainloop()

datasaved = shelve.open('.\\wsetup\\' + str(savedname))
listRegion = datasaved['listRegion']
imWidth = datasaved['imWidth']
imHeight = datasaved['imHeight']
PatientIdRegion = datasaved['PatientIdRegion']
patientIdwidth = datasaved['patientIdwidth']

orders1 = datasaved['orders1']
cancellong = datasaved['cancellong']
cancelfees = datasaved['cancelfees']
Blackline = datasaved['Blackline']
RollBar = datasaved['RollBar']
BlueBar = datasaved['BlueBar']
Listdown = datasaved['Listdown']
datasaved.close()

ddatasaved = shelve.open('.\\setup\\nosetup')

if 'folder' not in list(ddatasaved.keys()):
    deft1 = '201908zl1'
else:
    deft1 = (ddatasaved['folder'])

    # 获得并生成科室分类文件夹

if 'PatientNo' not in list(ddatasaved.keys()):
    deft2 = '400'
else:
    deft2 = (ddatasaved['PatientNo'])

if 'counter' not in list(ddatasaved.keys()):
    deft3 = '1'
else:
    deft3 = (ddatasaved['counter'])

root = tkinter.Tk()
root.title('输入查询内容')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

ww = 500
wh = 300
root.geometry("%dx%d+%d+%d" % (ww, wh, (sw - ww) / 2, (sh - wh) / 2))


def show1(event):
    t.delete('1.0', END)
    t.insert(INSERT, '本次准备查询哪个月份哪个科室？\n请填入例如【201908zl1】代表查询【2019年08月肿瘤1病区】')


def show2(event):
    t.delete('1.0', END)
    t.insert(INSERT, '本次准备查询多少个病人？')


def show3(event):
    t.delete('1.0', END)
    t.insert(INSERT, '设定【起始病人序号】即从第几个病人查起。\n首次运行程序时，此处应该填1。\n如果中断程序后重新开始时，应根据最后提示填写【起始病人序号】。')


l1 = tkinter.Label(root, text='查询日期科室', width=12)
l1.pack()
df = tkinter.StringVar()
df.set(str(deft1))
e1 = tkinter.Entry(root, textvariable=df)
e1.pack()
e1.bind('<ButtonRelease-1>', show1)

l2 = tkinter.Label(root, text='查询病人总数', width=12)
l2.pack()
df2 = tkinter.StringVar()
df2.set(str(deft2))
e2 = tkinter.Entry(root, textvariable=df2)
e2.pack()
e2.bind('<ButtonRelease-1>', show2)

l3 = tkinter.Label(root, text='起始病人序号', width=12)
l3.pack()
df3 = tkinter.StringVar()
# df3.set(str(deft3))
e3 = tkinter.Entry(root, textvariable=df3)
e3.pack()
e3.bind('<ButtonRelease-1>', show3)


def x():
    global af, b, c
    af = e1.get()
    b = e2.get()
    c = e3.get()
    root.destroy()
    return af, b, c


tkinter.Button(root, text='确定', command=x, width=8, height=1, activebackground='grey', relief='groove').pack()
t = tkinter.Text(root, width=50, height=5, bg='silver')
t.pack()

root.mainloop()
folder = af
PatientNo = b
counter = c
if os.path.isdir('.\\results\\' + str(folder)) == False:
    os.makedirs('.\\results\\' + str(folder))

if os.path.isdir('.\\results\\' + str(folder) + '\\all') == False:
    os.makedirs('.\\results\\' + str(folder) + '\\all')
if folder:

    ddatasaved['folder'] = folder
else:
    try:
        sys.exit(0)
    except:
        pyautogui.alert(text='用户退出程序', title='运行结束')
        sys.exit(0)
if PatientNo:

    ddatasaved['PatientNo'] = PatientNo
else:
    try:
        sys.exit(0)
    except:
        pyautogui.alert(text='用户退出程序', title='运行结束')
        sys.exit(0)
if counter:

    ddatasaved['counter'] = counter
else:
    try:
        sys.exit(0)
    except:
        pyautogui.alert(text='用户退出程序', title='运行结束')
        sys.exit(0)

start = pyautogui.confirm(
    text='请打开医院软件，进入病人列表，选中要查询的第【1】个病人条目，准备开始扫描！\n开始扫描请点击【确定】键\n退出程序请点击【取消】键。\n程序运行时，若要临时暂停程序，请【快速将鼠标移至屏幕左上角】！',
    title='现在准备开始扫描！！！', buttons=['OK', 'Cancle'])
if start == 'OK':
    pass
else:
    try:
        sys.exit(0)
    except:
        pyautogui.alert(text='用户退出程序', title='运行结束')
        sys.exit(0)


def imopen(imo):
    im = Image.open(imo)

    return im


for impath in impathlist:
    imdoc = Image.open(impath)

if 'x' not in list(ddatasaved.keys()):
    deft4 = '1'
else:
    deft4 = (ddatasaved['x'])
ddatasaved.close()


# GUI界面设置

def qu():
    root.destroy()


def gbar(now, tatal, s):
    canvas.coords(fillrec, (7, 7, 6 + (now / tatal) * 895, 80))
    root.update()
    x_s.set('已完成' + str(round(now / tatal * 100)) + '%剩余' + str(s))
    root.update()

    if round(now / tatal * 100) > 100:
        root.update()
        x_s.set('运行结束')


root = Tk()
root.wm_attributes('-topmost', 1)
root.overrideredirect(True)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

ww = 1040
wh = 30
root.geometry("%dx%d+%d+%d" % (ww, wh, (sw - ww) / 2, (sh - wh) / 2 * 1.90))

frame = Frame(root).grid(row=0, column=0)
canvas = Canvas(frame, width=902, height=20, bg="gold")
canvas.grid(row=0, column=0)
x_s = StringVar()
outrec = canvas.create_rectangle(5, 5, 900, 80, outline="black", width=1)
out1rec = canvas.create_rectangle(6, 6, 899, 78, outline="grey", width=1)
fillrec = canvas.create_rectangle(7, 7, 5, 80, outline="white", width=1, fill="blue")
Label(frame, textvariable=x_s).grid(row=0, column=1)

i = int(counter)

if i != 1:
    x = int(deft4)
else:
    x = 1
runts = '?:?:?'


def ttos(s):
    ss = time.strftime('%H:%M:%S', time.gmtime(s))
    return ss


ddatasaved = shelve.open('.\\setup\\nosetup')

while True:

    bt = time.time()
    gbar(i - int(counter), int(PatientNo) + 1 - int(counter), runts)

    try:

        x0 = x
        pyautogui.click(Listdown[0], Listdown[1])
        pyautogui.press('y')

        time.sleep(1)
        if i == int(PatientNo):
            imlast = pyautogui.screenshot(region=PatientIdRegion)
        pyautogui.click(cancellong[0], cancellong[1])
        pyautogui.click(cancelfees[0], cancelfees[1])
        time.sleep(0.5)
        pyautogui.doubleClick(orders1[0], orders1[1])
        while True:

            if pyautogui.pixel(Blackline[0], Blackline[1]) == (255, 255, 255):
                break
            imall = pyautogui.screenshot()
            imall.save('.\\results\\' + str(folder) + '\\all\\' + str(i) + '_' + str(x) + '.png')

            x += 1

            if pyautogui.pixel(RollBar[0], RollBar[1]) == (255, 255, 255):
                break

            pyautogui.press('pgdn')

            if pyautogui.pixel(BlueBar[0], BlueBar[1]) != (0, 0, 128):
                imall = pyautogui.screenshot()
                imall.save('.\\results\\' + str(folder) + '\\all\\' + str(i) + '_' + str(x) + '.png')

                x += 1
                break

        pyautogui.press('esc')

        pyautogui.click(Listdown[0], Listdown[1])
        pyautogui.press('down')
        i += 1
        et = time.time()
        runs = int(et - bt) * (int(PatientNo) + 1 - i)
        runts = ttos(runs)

        if i == int(PatientNo) + 1:
            break
    except:
        pand = pyautogui.confirm(text='程序暂停；已完成了对第 ' + str(
            i - 1) + ' 个病人的扫描。\n若要继续扫描，请退回到病人列表，然后点击【继续】键。\n结束扫描请点击【结束】；继续上次运行时请将【起始病人序号】设置为【 ' + str(
            i) + ' 】 \n最后扫描的住院号参见自动打开的图片，下次需要从此住院号病人查起', title='暂停/结束', buttons=['继续', '结束'])

        if pand == '继续':
            x = x0

        else:

            imabort = pyautogui.screenshot(region=PatientIdRegion)

            ddatasaved['counter'] = str(i)
            ddatasaved['x'] = str(x0)
            ddatasaved.close()
            root.destroy()
            sys.exit(0)

root.update()

root.destroy()

resultfolder = pyautogui.alert(text='完成!已完成了对第 ' + str(i - 1) + ' 个病人的扫描。\n如未完成扫描任务，再次运行时请将【起始病人序号】设置为【 ' + str(
    i) + ' 】 \n最后扫描的病人住院号参见点击【确定】按钮后自动打开的图片，下次需要从此住院号病人查起\n点击【确定】键以打开结果文件夹及最后一个住院号截图', title='完成')

os.system('explorer.exe /n, .\\results\\' + str(folder))

ddatasaved['x'] = str(x0)
ddatasaved['counter'] = str(i)
ddatasaved.close()
