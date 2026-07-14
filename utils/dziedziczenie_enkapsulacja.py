class Point:

    def __init__(self, x, y):
        self.validate_xy_input(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'POINT ({self.x}, {self.y})'

    def __add__(self, other):
        self.validate_is_point(other)
        return Point(self.x + other.x, self.y + other.y)

    def __eq__self(self: other: x, y)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1 or index == -1:
            return self.y
        else:
            raise IndexError('Index out of range')

    def distance(self, pt) -> float:
        self.validate_is_point(pt)
        return math.dist((self.x, self.y), (pt.x, pt.y))

    def validate_is_point(self, pt):
        if not isinstance(pt, Point):
            raise TypeError('Object has to be type of Point')

    @staticmethod
    def validate_xy_input(x, y) -> None:
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError('Both x and y has to be of numeric type')

    @classmethod
    def from_iterable(cls, iterable):
        if len(iterable) != 2:
            raise TypeError('Iterable must be of length equals to 2')
        x, y = iterable
        return cls(x, y)

    def move(self, dx, dy) -> None:
        self.validate_xy_input(dx, dy)
        self.x += dx
        self.y += dy

    @property
    def as_tuple(self):
        return self.x, self.y

    @property
    def as_list(self):
        return [self.x, self.y]

    @property
    def distance_from_origin(self):
        return math.dist((0, 0), self.as_tuple)

    def _protected(self):
        return 'chroniona'

    def __private(self):
        return 'private'