from apscheduler.scheduler.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=30)

sched.start()
