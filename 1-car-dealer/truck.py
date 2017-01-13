from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, carry_limit=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.carry_limit = carry_limit
        self.current_carriage_weight = None

    def has_carriage(self):
        if self.current_carriage_weight:
            return True
        else:
            return False

    def attach_carriage(self, carriage_weight):
        if carriage_weight <= self.carry_limit:
            self.current_carriage_weight = carriage_weight
            return True
        else:
            return False

    def detach_carriage(self):
        self.current_carriage_weight = None
