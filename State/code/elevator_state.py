from __future__ import annotations
from abc import ABC, abstractmethod


class Elevator:
    _state = None

    def __init__(self, state: State) -> None:
        self.setElevator(state)

    def setElevator(self, state: State):
        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}")

    def pushDownBtn(self):
        self._state.pushDownBtn()

    def pushUpBtn(self):
        self._state.pushUpBtn()


class State(ABC):
    def __init__(self):
        self._elevator = None

    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def pushDownBtn(self) -> None:
        pass

    @abstractmethod
    def pushUpBtn(self) -> None:
        pass
