class Worker:
    def __init__(self, hours):
        self._hours = hours


    @property
    def hours(self):
        return f"Worked hours {self._hours}"