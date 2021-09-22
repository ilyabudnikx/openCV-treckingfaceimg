class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


class Room:

    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square




room_1 = Room(3,3,2.5)
print(room_1.square)
room_1.addWD(1.5, 1.5, 'big_win')
room_1.addWD(1, 2, 'Fiodoor')
room_1.addWD(0.20, 0.40, 'schel')
print(room_1.wd)