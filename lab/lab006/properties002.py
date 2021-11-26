from rich.console import Console
import rich.traceback
import functools

console = Console()
console.clear()
rich.traceback.install()

# class MyClass:
#     def __getattr__(self, name):
#         console.print(f'{name = }')
#         return 'YOLO'

# mc = MyClass()
# console.print(mc.yolo)

class MyInnerClass:
    def __get__(self, instance, owner = None):
        console.print(f'{instance = } {owner = }')
        return 'Always look at the bright side of life!'

class MyClass:
    yolo = MyInnerClass()

mc = MyClass()
console.print(mc.yolo)
console.print(MyClass.yolo)