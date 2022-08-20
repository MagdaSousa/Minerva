class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The {self.f} is not in a valid range {self.min_f, self.max_f}'