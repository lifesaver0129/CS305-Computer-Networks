class Problem3:
    def __init__(self, value_x):
        self.value_x = value_x
        self.value_r = 2 * 1024 ^ 3
        self.pro_speed = 2 * 10 ^ 8
        self.range = 50000000

    def ans_1(self):
        if self.value_x < self.range * self.value_r / self.pro_speed:
            return self.value_x
        else:
            return self.range * self.value_r * self.pro_speed

    def ans_2(self):
        return self.pro_speed * self.value_r

    def ans_3(self):
        return self.range / self.pro_speed + self.value_x / self.value_r
