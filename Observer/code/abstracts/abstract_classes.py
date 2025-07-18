class AbstractSubject:
    """
        Abstract patient
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
        Abstract medical device
    """

    def __init__(self):
        pass

    def update(self):
        pass
