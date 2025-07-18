from Observer.code.abstracts.abstract_classes import AbstractObserver


class Thermometer(AbstractObserver):
    """
        Concrete observer - thermometer
    """

    def __init__(self):
        super().__init__()

    def update(self, tt):
        if type(tt).__name__ == 'CovidPatient':
            temp = tt.get_value("temperature")
            if temp > 37.8:
                print("EMCY - " + "Temperature too high: " + str(temp))
            elif temp < 36.0:
                print("EMCY - " + "Temperature too slow: " + str(temp))
            else:
                print("INFO - " + "Temperature normal: " + str(temp))
        else:
            pass