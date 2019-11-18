from playsound import playsound
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

print('机器人程序24小时为您守候。' + '\n'
      '可以随便动我，但不要关掉哟。')


def red_song():  # 每周每天早上一红歌
    for i in range(5):
        playsound('sound/red_song/2.mp3')


def am_before_class():  # 上午预铃
    playsound('sound/am_before_class.mp3')


def am_first_class_begin():  # 上午第一节上课
    playsound('sound/am_first_class_begin.mp3')


def am_first_class_over_and_eye_exercises():  # 上午第一节下课并眼保健操
    playsound('sound/am_first_class_over_and_eye_exercises.mp3')


def am_second_class_begin():  # 上午第二节上课
    playsound('sound/am_second_class_begin.mp3')


def am_second_class_over_and_sport():  # 上午第二节下课并大课间
    playsound('sound/am_second_class_over_and_sport.mp3')


def am_third_class_begin():  # 上午第三节上课
    playsound('sound/am_third_class_begin.mp3')


def am_third_class_over():  # 上午第三节下课
    playsound('sound/am_third_class_over.mp3')


def am_fourth_class_begin():  # 上午第四节上课
    playsound('sound/am_fourth_class_begin.mp3')


def am_fourth_class_over_and_shool_over():  # 上午第四节下课并放学
    playsound('sound/am_fourth_class_over_and_shool_over.mp3')


def pm_before_class():  # 上午预铃
    playsound('sound/pm_before_class.mp3')


def pm_first_class_begin():  # 下午第一节上课
    playsound('sound/pm_first_class_begin.mp3')


def pm_first_class_over():  # 下午第一节下课
    playsound('sound/pm_first_class_over.mp3')


def pm_second_class_begin():  # 下午第二节上课
    playsound('sound/pm_second_class_begin.mp3')


def pm_second_class_over_and_sport():  # 下午第二节下课并大课间
    playsound('sound/pm_second_class_over_and_sport.mp3')


def pm_third_class_begin():  # 下午第三节上课
    playsound('sound/pm_third_class_begin.mp3')


def pm_third_class_over_and_shool_over():  # 下午第三节下课并放学
    playsound('sound/pm_third_class_over_and_shool_over.mp3')


def other():  # 其它时间事件预留
    pass


scheduler = BlockingScheduler()

'''红歌'''
trigger_red_song = CronTrigger(day_of_week='0-4', hour=15, minute=54, second=0)  # 周一上午预铃时间变为上课时间7：50
scheduler.add_job(red_song, trigger_red_song)


'''周一上午第一节'''
trigger_monday_7_50 = CronTrigger(day_of_week='0', hour=7, minute=50, second=0)  # 周一上午预铃时间变为上课时间7：50
scheduler.add_job(am_first_class_begin, trigger_monday_7_50)
trigger_class_over_8_30 = CronTrigger(day_of_week='0', hour=8, minute=30, second=0)  # 周一上午第一节下课时间8：30
scheduler.add_job(am_first_class_over_and_eye_exercises, trigger_class_over_8_30)

'''周一上午第二节'''
trigger_class_begin_8_45 = CronTrigger(day_of_week='0', hour=8, minute=45, second=0)  # 周一上午第二节上课时间8：45
scheduler.add_job(am_second_class_begin, trigger_class_begin_8_45)
trigger_class_over_9_25 = CronTrigger(day_of_week='0', hour=9, minute=25, second=0)  # 周一上午第二节下课时间9：25
scheduler.add_job(am_second_class_over_and_sport, trigger_class_over_9_25)


'''周二到周五上午预铃'''
trigger_before_class_7_50 = CronTrigger(day_of_week='1-4', hour=7, minute=50, second=0)  # 周二到周五早上预铃时间7:50
scheduler.add_job(am_before_class, trigger_before_class_7_50)

'''周二到周五上午第一节'''
trigger_class_begin_8_00 = CronTrigger(day_of_week='1-4', hour=8, minute=00, second=0)  # 周二到周五上午第一节上课时间8:00
scheduler.add_job(am_first_class_begin, trigger_class_begin_8_00)
trigger_class_over_8_40 = CronTrigger(day_of_week='1-4', hour=8, minute=40, second=0)  # 周二到周五上午第一节下课时间8:40
scheduler.add_job(am_first_class_over_and_eye_exercises, trigger_class_over_8_40)

'''周二到周五上午第二节'''
trigger_class_begin_8_55 = CronTrigger(day_of_week='1-4', hour=8, minute=55, second=0)  # 周二到周五上午第二节上课时间8:55
scheduler.add_job(am_second_class_begin, trigger_class_begin_8_55)
trigger_class_over_9_35 = CronTrigger(day_of_week='1-4', hour=9, minute=35, second=0)  # 周二到周五早上第二节下课时间9:35
scheduler.add_job(am_second_class_over_and_sport, trigger_class_over_9_35)

'''周一到周五上午第三节'''
trigger_class_begin_10_00 = CronTrigger(day_of_week='0-4', hour=10, minute=00, second=0)  # 周一到周五上午第三节上课时间10:00
scheduler.add_job(am_third_class_begin, trigger_class_begin_10_00)
trigger_class_over_10_40 = CronTrigger(day_of_week='0-4', hour=10, minute=40, second=0)  # 周一到周五上午第三节下课时间10:40
scheduler.add_job(am_third_class_over, trigger_class_over_10_40)

'''周一到周五上午第四节'''
trigger_class_begin_10_50 = CronTrigger(day_of_week='0-4', hour=10, minute=50, second=0)  # 周一到周五上午第四节上课时间10:50
scheduler.add_job(am_fourth_class_begin, trigger_class_begin_10_50)
trigger_class_over_11_30 = CronTrigger(day_of_week='0-4', hour=11, minute=30, second=0)  # 周一到周五上午第四节下课（放学）时间11:30
scheduler.add_job(am_fourth_class_over_and_shool_over, trigger_class_over_11_30)


'''周一到周五下午预铃'''
trigger_before_class_13_50 = CronTrigger(day_of_week='0-4', hour=13, minute=50, second=0)  # 周一到周五下午预铃时间13:50
scheduler.add_job(pm_before_class, trigger_before_class_13_50)

'''周一到周五下午第一节'''
trigger_class_begin_14_00 = CronTrigger(day_of_week='0-4', hour=14, minute=00, second=0)  # 周一到周五下午第一节上课时间14:00
scheduler.add_job(pm_first_class_begin, trigger_class_begin_14_00)
trigger_class_over_14_40 = CronTrigger(day_of_week='0-4', hour=14, minute=40, second=0)  # 周一到周五下午第一节下课时间14:40
scheduler.add_job(pm_first_class_over, trigger_class_over_14_40)

'''周一到周五下午第二节'''
trigger_class_begin_14_50 = CronTrigger(day_of_week='0-4', hour=14, minute=50, second=0)  # 周一到周五下午第二节上课时间14:50
scheduler.add_job(pm_second_class_begin, trigger_class_begin_14_50)
trigger_class_over_15_30 = CronTrigger(day_of_week='0-4', hour=15, minute=30, second=0)  # 周一到周五下午第二节下课时间15:30
scheduler.add_job(pm_second_class_over_and_sport, trigger_class_over_15_30)

'''周一到周五下午第三节'''
trigger_class_begin_15_40 = CronTrigger(day_of_week='0-4', hour=15, minute=50, second=0)  # 周一到周五下午第二节上课时间15:40
scheduler.add_job(pm_third_class_begin, trigger_class_begin_15_40)
trigger_class_over_16_30 = CronTrigger(day_of_week='0-4', hour=16, minute=30, second=0)  # 周一到周五下午第二节下课时间16:30
scheduler.add_job(pm_third_class_over_and_shool_over, trigger_class_over_16_30)

scheduler.start()

