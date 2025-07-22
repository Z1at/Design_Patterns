import time


class AbstractClass:
    """
        Абстрактный класс, у которого определены три функции:
        add_obs - добавить наблюдателя
        remove_obs - удалить наблюдателя
        notify_observer - разослать уведомления наблюдателям
    """

    def __init__(self):
        self.__observers = []

    def add_obs(self, observer):
        self.__observers.append(observer)

    def remove_obs(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, *arg):
        for i in self.__observers:
            i.update(self, *arg)


class AbstractObserver:
    """
        Абстрактный наблюдатель от которого нужно будет наследоваться конкретным
        наблюдателям и переопределять метод update, который
    """

    def __init__(self):
        pass

    def update(self):
        pass


class HeartbeatMonitor(AbstractObserver):
    """
        Конкретный наблюдатель пульса - в зависимости от значения пульса
        выводит результат
    """

    def __init__(self):
        super().__init__()

    def update(self, tt):
        if type(tt).__name__ == 'Patient':
            hr = tt.get_value("heartrate")
            if hr > 120:
                print("Пульс слишком быстрый: " + str(hr))
            elif hr < 35:
                print("Пульс слишком медленный:  " + str(hr))
            else:
                print("Пульс в норме: " + str(hr))
        else:
            pass


class Thermometer(AbstractObserver):
    """
        Конкретный наблюдатель температуры - в зависимости от значения температуры
        выводит результат
    """

    def __init__(self):
        super().__init__()

    def update(self, tt):
        if type(tt).__name__ == 'Patient':
            temp = tt.get_value("temperature")
            if temp > 37.8:
                print("Слишком высокая температура: " + str(temp))
            elif temp < 35.0:
                print("Слишком низкая температура: " + str(temp))
            else:
                print("Температура в норме: " + str(temp))
        else:
            pass


class Patient(AbstractClass):
    """
        Конкретный пациент - который в случае изменения параметров вызывает
        функция notify_observer
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.params = {"temperature": 0.0, "heartrate": 0.0}

    def set_value(self, measure_type, val):
        if measure_type in self.params:
            self.params[measure_type] = val
            self.notify_observer()
        else:
            print("Такого параметра нет")

    def get_value(self, measure_type):
        if measure_type in self.params:
            return self.params[measure_type]
        else:
            return None


if __name__ == "__main__":
    sub = Patient("Кирилл")
    obs1 = Thermometer()
    obs2 = HeartbeatMonitor()

    for i in range(15):
        time.sleep(1)
        print("====== Шаг {} =======".format(i + 1))

        if i == 3:
            sub.add_obs(obs1) # На третью итерацию добавляем наблюдателя температуры
        elif i == 5:
            sub.add_obs(obs2) # На пятую итерацию добавляем наблюдателя пульса
        elif i == 10:
            sub.remove_obs(obs1) # На десятую итерацию убираем наблюдателя температуры

        if i % 3 == 0:
            sub.set_value("temperature", 35.5 + 0.5 * i)
        elif i % 3 == 1:
            sub.set_value("heartrate", 30 + 10 * i)
