"""
File: circle.py
Draws a circle with a Turtle by moving a short distance and
turning 3 degrees, 120 times (120 x 3 degrees = 360 degrees).
"""

import math
from turtle import Turtle, Screen


def drawCircle(t, x, y, radius):
    """Draws a circle with its center at (x, y) and the given radius.
    Arguments: a Turtle, the center's x and y coordinates, and the radius."""
    # Distance around the whole circle divided by 120 steps
    distance = 2.0 * math.pi * radius / 120.0

    # Move to the starting point on the right side of the circle without drawing
    t.up()
    t.goto(x + radius, y)
    # Point a little past straight up (90 degrees). Half of the 3 degree turn
    # (1.5) keeps the finished circle centered on (x, y).
    t.setheading(91.5)
    t.down()

    # Move forward a little, turn 3 degrees, and repeat 120 times
    for count in range(120):
        t.forward(distance)
        t.left(3)


def main():
    t = Turtle()
    t.speed(0)
    drawCircle(t, 0, 0, 150)
    t.hideturtle()
    Screen().exitonclick()      # Close the window by clicking on it


if __name__ == "__main__":
    main()