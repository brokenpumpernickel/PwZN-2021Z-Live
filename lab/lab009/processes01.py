import multiprocessing as mp
import os

class MyProcess(mp.Process):
    def run(self):
        index = 0
        while(True):
            print(f'Hello from process! {os.getpid()}')
            index = index * index

if __name__ == '__main__':
    p1 = MyProcess()
    p1.start()
    p2 = MyProcess()
    p2.start()    

    index = 0
    while(True):
        print(f'Hello from main! {os.getpid()}')
        index = index * index