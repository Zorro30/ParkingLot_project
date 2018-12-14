class Car(object):

    def __init__(self):
        self._reg_no = None
        self._colour = None

    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value

    @classmethod
    def create(cls, reg_no, colour):
        car_obj = cls()
        car_obj.reg_no = reg_no
        car_obj.colour = colour
        return car_obj