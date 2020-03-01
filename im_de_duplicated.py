# -*- coding: utf-8 -*-
# author:mistchan
from hashlib import md5
import glob


def de_rep_im(dirt):
    """
    Remove duplicate images in one folder
    :param dirt: full Folder path
    """
    list0 = []

    list1 = glob.glob(dirt + '\\*.png')

    # 计算每张图片的md5值，并将图片路径与其md5值整合到列表list中
    for n in range(len(list1)):
        hasho = md5()
        img = open(list1[n], 'rb')
        hasho.update(img.read())
        img.close()
        list2 = [list1[n], hasho.hexdigest()]

        list0.append(list2)

    # 两两比较md5值，若相同，则删去一张图片
    m = 0
    while m < len(list0):
        t = m + 1
        while t < len(list0):
            if list0[m][1] == list0[t][1]:
                os.remove(list0[t][0])
                del list0[t]
            else:
                t += 1
        m += 1
