from rich.console import Console
import rich.traceback
import functools

console = Console()
console.clear()
rich.traceback.install()

@functools.cache
def fibon(n):
    if n < 2:
        return n

    return fibon(n - 1) + fibon(n - 2)

for n in range(50):
    console.print(f'{n = } {fibon(n) = }')