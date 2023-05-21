from tyre.tyre import Tyre


class CarriganTire(Tyre):
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn

    def needs_service(self):
        for value in self.tire_worn:
            if value >= 0.9:
                return True
        return False
