class Timer:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self.time = 0

    def start_timer(self):
        self.start = time.time()

    def stop_timer(self):
        self.end = time.time()
        self.time = self.end - self.start

    def get_time(self):
        return self.time

    def reset(self):
        self.start = time.time()
        self.end = time.time()
        self.time = 0
