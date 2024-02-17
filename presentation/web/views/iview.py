from abc import ABC, abstractmethod


class IView(ABC):

    @abstractmethod
    def render(self) -> str:
        pass
