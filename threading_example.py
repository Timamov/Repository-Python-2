import threading
from time import sleep


# def worker(num):
#     print(f'Worker: {num} is working')
#
#
# threads = []
#
# for proc_number in range(1100):
#     t = threading.Thread(target=worker, args=(proc_number,))
#     threads.append(t)
#     t.start()

def do_job(number, second_arg=None):
    for i in range(10):
        print(f'From child thread: {i=}, {number=} {second_arg=}')
        sleep(1)


thread = threading.Thread(target=do_job, args=(2,), kwargs={'second_arg':25})
thread.start()

for i in range(10, 30):
    print(f'From main thread: {i=}')
    sleep(0.3)