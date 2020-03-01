# -*- coding: utf-8 -*-
# 2020.02.28
# 10:49:52
# author:mistchan
import time


def timing_app(f):  # f为被装饰函数

    """a wrapper to Record Running Time"""

    def inner(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return ret

    return inner

