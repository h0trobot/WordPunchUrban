class Uno:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def sum(self, *args):
        value = 2
        return value


class Dos:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_value()

    def use_value(self, *args):
        if Uno().sum() == 2:
            print(Uno().sum())


Uno()
Dos()
