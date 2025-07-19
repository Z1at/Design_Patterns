from elevator_state import Elevator
from floors import FirstFloor


if __name__ == "__main__":
    myElevator = Elevator(FirstFloor())
    myElevator.presentState()

    myElevator.pushUpBtn()
    myElevator.presentState()

    myElevator.pushDownBtn()
    myElevator.presentState()
