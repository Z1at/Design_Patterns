from Observer.code.abstracts.abstract_classes import AbstractSubject


class CovidPatient(AbstractSubject):
    """
        Concrete subject - patient
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.__physioParams = {"temperature": 0.0, "heartrate": 0.0, "oxygen": 0.0, "respiration": 0.0}

    def set_value(self, measure_type, val):
        if measure_type in self.__physioParams:
            self.__physioParams[measure_type] = val
            self.notify_observer()
        else:
            print("parameter type not yet supported")

    def get_value(self, measure_type):
        if measure_type in self.__physioParams:
            return self.__physioParams[measure_type]
        else:
            return None