from tyre.tyre import Tyre


class OctoprimeTire(Tyre):
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn

    def needs_service(self):
        total = sum(self.tire_worn)
        if total >= 3:
            return True
        return False
