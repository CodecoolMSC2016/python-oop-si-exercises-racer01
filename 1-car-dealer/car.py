from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_running = None

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
