from elevator_state import State


class FirstFloor(State):

    def pushDownBtn(self) -> None:
        print("Already in the bottom floor")

    def pushUpBtn(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.setElevator(SecondFloor())


class SecondFloor(State):

    def pushDownBtn(self) -> None:
        print("Elevator moving down a floor...")
        self.elevator.setElevator(FirstFloor())

    def pushUpBtn(self) -> None:
        print("Already in the top floor")
