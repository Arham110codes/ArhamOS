from abc import ABC, abstractmethod
from rich.console import Console

console = Console()


class Workflow(ABC):
    """
    Base class for every workflow inside ArhamOS.

    Every workflow follows the same lifecycle:

        setup()
            ↓
        execute()
            ↓
        cleanup()
    """

    def run(self):

        console.rule(f"[bold cyan]{self.__class__.__name__}")

        self.setup()

        self.execute()

        self.cleanup()

    def setup(self):
        """
        Optional preparation step.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Main workflow logic.
        """
        pass

    def cleanup(self):
        """
        Optional cleanup step.
        """
        pass