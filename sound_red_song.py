# Win10, PyCharm Professional 2019.2
# Author: Zhang Bohua
# Date: 2019.11.18
# Version: 1.0, the style is command line.

from playsound import playsound
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

print('机器人程序24小时为您守候。' + '\n'
      '可以随便动我，但不要关掉哟。')


def red_song():  # 每周每天早上一红歌
    for i in range(5):
        playsound('sound/red_song/2.mp3')


scheduler = BlockingScheduler()

'''红歌'''
trigger_red_song = CronTrigger(day_of_week='0-4', hour=7, minute=20, second=0)  # 红歌每天早上播放五遍7：30结束
scheduler.add_job(red_song, trigger_red_song)


scheduler.start()

