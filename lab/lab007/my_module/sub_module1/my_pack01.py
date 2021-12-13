def my_function_a():
    print(f'(A) Hello from package: {__name__}')

def my_function_b():
    print(f'(B) Hello from package: {__name__}')

__all__ = ['my_function_a']