from observers.thermometer import Thermometer
from observers.heartbeat_monitor import HeartbeatMonitor
from patients.covid_patient import CovidPatient
import time


if __name__ == "__main__":
    sub = CovidPatient("John")
    obs1 = Thermometer()
    obs2 = HeartbeatMonitor()

    for i in range(15):
        time.sleep(1)
        print("====== Time step {} =======".format(i + 1))

        # At rount #3: thermometer is added for monitoring temperature
        # At rount #5: heartbeatMonitor is added for monitoring heart rate
        # At rount #10: thermometer is removed

        if i == 3:
            sub.add_obs(obs1)
        elif i == 5:
            sub.add_obs(obs2)
        elif i == 10:
            sub.remove_obs(obs1)

        # simulating the variation of patient's physiological parameters
        if i % 3 == 0:
            sub.set_value("temperature", 35.5 + 0.5 * i)
        elif i % 3 == 1:
            sub.set_value("heartrate", 30 + 10 * i)
        else:
            sub.set_value("oxygen", 5.0 + 0.05 * i)