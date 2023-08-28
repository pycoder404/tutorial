import time
import datetime
from threading import Thread


def print_number(n: int) -> None:
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{times} - {n}')
    time.sleep(n)
    print(f"thread :{n} done")

print(f'start time:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

for i in range(1,4):
    # 这里通过传给Thread传入target可调用对象来实现线程创建
    t = Thread(target=print_number,args=(i,))
    t.start()

print(f'main processs  end time:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')