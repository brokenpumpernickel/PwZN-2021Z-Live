from rich.console import Console
import rich.traceback
import functools

console = Console()
console.clear()
rich.traceback.install()

# class MonteCarloSimulation:
#     def __init__(self, b = 0):
#         self.b = b
    
#     def get_b(self):
#         return self._b

#     def set_b(self, b):
#         if b < 0:
#             self._b = 0
#         else:
#             self._b = b        
    
#     b = property(get_b, set_b)

class MonteCarloSimulation:
    def __init__(self, b = 0):
        self.b = b

    @property    
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if b < 0:
            self._b = 0
        else:
            self._b = b        

mcs = MonteCarloSimulation()
mcs.b = 15
console.print(mcs.b)

mcs.b = -500
console.print(mcs.b)

    

