from __future__ import annotations
import math
import doctest


class Circle:

    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        :param radius: radius of the circle, may be zero.
        :raises ValueError: if radius is negative.
        """
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def add_area(self, circle: Circle) -> Circle:
        """Return a new circle whose area equals the combined
        area of this circle and another circle.
        Since area is pi*r**2, the radii of the 3 circles
        should form a Pythagorean triple (r1^2 + r2^2 = r3^2)
        """
        r1 = self.get_radius()
        r2 = circle.get_radius()
        # this is important, so show the operation in a rounded-box
        # on the Circle lifeline, or show it as a comment.
        r = math.hypot(r1, r2)
        # In a sequence diagram create a name for the new circle
        # so that you can show what is being returned.
        return Circle(r)

    def get_area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def get_radius(self) -> float:
        return self.radius

    def __str__(self) -> str:
        return f"Circle({self.radius})"

    def add(self, circle: Circle):
        """
        :param circle with radius = 4
        :return: Circle withradius = 5

        Example:
        >>> first_circle = Circle(3)
        >>> second_circle = Circle(4)
        >>> first_circle.add(second_circle)
        5.0
        """
        new_circle = self.add_area(circle)
        new_radius = new_circle.get_radius()
        return new_radius

    def circle_radius(self, circle: Circle):
        """
        :param circle with negative radius
        :raise: Exception

        Example:
        >>> normal_circle = Circle(8)
        >>> negative_circle = Circle(-9)
        >>> normal_circle.circle_radius(negative_circle)
        Traceback (most recent call last):
        ...
        """
        new_circle = self.add_area(circle)
        new_radius = new_circle.get_radius()
        if new_radius < 0:
            raise ...

    __repr__ = __str__


if __name__ == "__main__":
    doctest.testmod(verbose=True)
