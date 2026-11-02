"""
File: circle_rotate.py
Fills each of the 120 sectors of a circle with a random color, then rotates
the colors around the circle. One full trip around takes 60 seconds.
"""
#I did use ai for this color program this was my prompt
#The prompt The prompt. I need a Python turtle program. Fill each of the 120 sectors of a circle with a random color, then make the colors rotate around the circle so one full trip takes 60 seconds. Explain how it works in beginner terms.

import math
import random
import time
import turtle

SECTORS = 120                               # Same 120 steps as drawCircle
SECONDS_PER_TURN = 60                       # One full rotation takes 60 seconds
SECONDS_PER_SECTOR = SECONDS_PER_TURN / SECTORS     # 0.5 seconds per sector


def randomColors(count):
    """Returns a list of count random (red, green, blue) colors."""
    colors = []
    for index in range(count):
        colors.append((random.random(), random.random(), random.random()))
    return colors


def drawSectors(t, x, y, radius, colors, shift):
    """Fills the 120 sectors of the circle centered at (x, y).
    Sector number i gets colors[i + shift], so a bigger shift
    moves the colors farther around the circle."""
    distance = 2.0 * math.pi * radius / SECTORS

    t.up()
    t.goto(x + radius, y)
    t.setheading(91.5)

    for i in range(SECTORS):
        t.color(colors[(i + shift) % SECTORS])
        start = t.position()            # This sector's first point on the edge
        t.begin_fill()
        t.forward(distance)             # Move along the edge to the next point
        end = t.position()
        t.goto(x, y)                    # Over to the center...
        t.goto(start)                   # ...and back to the start (a triangle)
        t.end_fill()
        t.goto(end)                     # Return to the edge to continue
        t.left(3)


def main():
    screen = turtle.Screen()
    screen.title("Rotating Color Circle")
    screen.tracer(0)                    # Draw each frame all at once
    t = turtle.Turtle()
    t.hideturtle()

    colors = randomColors(SECTORS)
    startTime = time.time()

    def update():
        """Works out how far to rotate, redraws the circle, and runs again."""
        elapsed = time.time() - startTime
        shift = int(elapsed / SECONDS_PER_SECTOR) % SECTORS
        t.clear()
        drawSectors(t, 0, 0, 200, colors, shift)
        screen.update()
        screen.ontimer(update, 100)     # Check again in 100 milliseconds

    update()
    screen.mainloop()


if __name__ == "__main__":
    main()