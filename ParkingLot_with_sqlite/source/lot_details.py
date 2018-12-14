class PSlot(object):

    def __init__(self, slot_no=None, available=None):
        self.car = None
        self.slot_no = slot_no
        self.available = available

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value

    @property
    def slot_no(self):
        return self._slot_no

    @slot_no.setter
    def slot_no(self, value):
        self._slot_no = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value