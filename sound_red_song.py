# Win10, PyCharm Professional 2019.2， Python 3.7
# Author: Zhang Bohua
# Date: 2019.11.20
# Version: 1.0, the style is command line.
"""
每天早上循环播放红歌，10分钟左右，7点30结束。
歌的时长不固定，但必须7点30结束，为保证歌的连贯性，不至于放到一半就到点了或者放完还有很长时间没到点，所以得通过代码逻辑推算出开始播放的时间。
"""

from playsound import playsound  # 播放mp3文件的第三方库
from apscheduler.schedulers.blocking import BlockingScheduler  # 定时执行任务第三方库
from apscheduler.triggers.cron import CronTrigger  # 定时执行任务第三方库
from mutagen.mp3 import MP3  # 获取mp3文件时长
import datetime  # 日期时间第三方库
import time  # 日期时间标准库

'''下面三行代码：获取文件名为11.mp3的音频文件的时长（秒），并打印到屏幕。'''
audio = MP3("sound/red_song/11.mp3")
time_length = audio.info.length
print('本周要播放的红歌的时长（秒）：', time_length, '秒。')

'''计划持续播放的时间：10分钟乘60秒，这里可以改写一下通过input函数获取任意持续播放的时间（分）'''
time_total = 10 * 60

'''将当天规定的结束时间转化为时间戳，这里也可以改写一下通过input函数获取规定的结束时间（小时、分、秒）'''
date_current = datetime.date.today()
time_string = str(date_current) + ' ' + '7' + ':' + '30' + ':' + '00'
time_objet = time.strptime(time_string, '%Y-%m-%d %H:%M:%S')
time_stamp_finish = time.mktime(time_objet)

'''因为每首歌的时长不一样，有可能会出现最后一遍没放完就到时间了或者放完还剩下很多时间，所以用下面的逻辑将播放时长控制在10分钟左或者右。'''
time_number = None
if (time_total % time_length) >= (time_length * (1 / 2)):
    time_number = time_total // time_length + 1
else:
    time_number = time_total // time_length
time_number = int(time_number)

'''获取实际开始播放时间的时间戳并转换为时间对象'''
time_stamp_start = time_stamp_finish - time_number * time_length
time_local = time.localtime(time_stamp_start)

'''获取实际开始播放时间的时、分、秒'''
hour = time_local.tm_hour
minute = time_local.tm_min
second = time_local.tm_sec

'''打印到屏幕提示'''
print('机器人程序24小时为您守候。' + '\n'
      '可以随便动我，但不要关掉哟。')


def red_song():  # 每周每天早上一红歌
    """
    连续播放遍数，此自定义函数也是下面定时任务代码行必须用到的参数
    """
    for i in range(time_number):
        playsound('sound/red_song/11.mp3')


'''定时播放任务'''
scheduler = BlockingScheduler()
trigger_red_song = CronTrigger(day_of_week='0-4', hour=hour, minute=minute, second=second)  # 周一到周五每天早上播放7：30结束
scheduler.add_job(red_song, trigger_red_song)
scheduler.start()

