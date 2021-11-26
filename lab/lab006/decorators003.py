from rich.console import Console
import rich.traceback
import functools

console = Console()
console.clear()
rich.traceback.install()

class MonteCarloSimulation:
    def __init__(self, hamiltonian = None):
        self._hamiltonian = hamiltonian

    def next_step(self):
        console.print(self._hamiltonian())

    def hamiltonian(self, func):
        self._hamiltonian = func

        return func

mcs = MonteCarloSimulation()

@mcs.hamiltonian
def my_super_hamiltonian():
    return 5

mcs.next_step()