class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"{self.x, self.y, self.z}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y, self.z / other.z)

    def get_x(self):
        return self.x

    def change_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def change_y(self, new_y):
        self.y = new_y

    def get_z(self):
        return self.z

    def change_z(self, new_z):
        self.z = new_z
