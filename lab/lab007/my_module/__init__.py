#from . import sub_module1, sub_module2
import my_module.sub_module1, my_module.sub_module2

print(f'Hello from {__name__}')

def yolo():
    print('YOLO')

a = ['1', '2', '3']