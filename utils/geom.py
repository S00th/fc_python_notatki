import math
from typing import Sequence

def circle_area(radius: int | float) -> float:
    return radius ** 2 * math.pi

def calculate_euclidean_distance(
        point1: Sequence,
        point2: Sequence
) -> float:
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)