from rich.console import Console
import rich.traceback
from rich.progress import track
import time

console = Console()
console.clear()

console.rule("Nasz super skrypt!")
console.print()

console.print('Hello [bold red]console[/bold red]! :snake:')

def do_some_work():
    time.sleep(1)

for i in track(range(10)):
    do_some_work()