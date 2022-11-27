import datetime
import hashlib
import logging
import sys
import time

WARN = 0
INFO = 1
MESSAGE = 2
logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)


def logFormat(code, info) -> None:
    # 打log
    if code == 0:
        level = 'WARN'
    elif code == 1:
        level = 'INFO'
    elif code == 2:
        level = 'MESSAGE'
    else:
        level = 'MESSAGE'

    t = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    val = '[{}] {} {}'.format(level, t, info)
    logging.info(val)


def getTimeStamp() -> int:
    # 获取时间戳，计时单位毫秒
    return int(time.time() * 1000)


def string2sha256(s: str) -> str:
    # 字符串转哈西
    ss = s.encode('utf-8')
    return hashlib.sha256(ss).hexdigest()


def getNowTime() -> str:
    # 获取当前时间，转化为字符串
    return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def getNowTime2() -> str:
    # 获取当前时间，转化为没有空格的字符串
    return datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S")


def getNowDate() -> str:
    # 获取当前年月日
    return datetime.datetime.today().strftime("%Y-%m-%d")
