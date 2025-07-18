from Observer.code.abstracts.abstract_classes import AbstractObserver


class HeartbeatMonitor(AbstractObserver):
    """
        Concrete Observer - heartbeat monitor
    """

    def __init__(self):
        super().__init__()

    def update(self, tt):
        if type(tt).__name__ == 'CovidPatient':
            hr = tt.get_value("heartrate")
            if hr > 120:
                print("EMCY - " + "Heart rate too high: " + str(hr))
            elif hr < 35:
                print("EMCY - " + "Heart rate too slow:  " + str(hr))
            else:
                print("INFO - " + "Heart rate normal: " + str(hr))
        else:
            pass