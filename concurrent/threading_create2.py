import time
import datetime
from threading import Thread


class MyThread(Thread):
    def __init__(self, name,num):
        super(MyThread,self).__init__()
        self.name = name
        self.num = num

    def run(self):
        print(f'run thread:{self.name} and sleep :{self.num} s')
        time.sleep(self.num)
        print(f'run thread:{self.name} done')


print(f'start time:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

t1 = MyThread('t1',3)
t2 = MyThread('t2',5)
t1.start()
t2.start()

print(f'main processs end time:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

