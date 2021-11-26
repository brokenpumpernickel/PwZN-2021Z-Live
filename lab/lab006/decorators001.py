from rich.console import Console
import rich.traceback
import functools

console = Console()
console.clear()
rich.traceback.install()

# def called_decorator(func):
#     def wrapper():
#         console.print("Called")
#         return func()
    
#     return wrapper

# @called_decorator
# def fibon():
#     return 'Hello fibon!'

# #fibon = called_decorator(fibon)

# fibon()

##############################

# def called_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwars):
#         console.log(f'Called {func.__name__}')
#         return func(*args, **kwars)
    
#     return wrapper

# @called_decorator
# @called_decorator
# def fibon(n):
#     return f'Hello fibon! {n}'

# #fibon = called_decorator(fibon)
# console.print(fibon(5))

# ##############################

# def called_decorator(colour):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwars):
#             console.log(f'[{colour}]Called {func.__name__}[/{colour}]')
#             return func(*args, **kwars)
        
#         return wrapper
    
#     return decorator

# @called_decorator(colour = 'blue')
# def fibon(n):
#     return f'Hello fibon! {n}'
# # fibon = called_decorator(colour = 'red')(fibon)

# console.print(fibon(5))

##############################

def called_decorator(_func = None, colour = 'yellow'):
    console.log(colour)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwars):
            console.log(f'[{colour}]Called {func.__name__}[/{colour}]')
            return func(*args, **kwars)
        
        return wrapper
    
    if _func is not None:
        return decorator(_func)

    return decorator

@called_decorator(colour = 'blue')
def fibon(n):
    return f'Hello fibon! {n}'
# fibon = called_decorator(colour = 'red')(fibon)
# fibon = called_decorator(fibon)

console.print(fibon(5))