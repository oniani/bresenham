import matplotlib.pyplot as plt


def bresenham(radius: float) -> None:
    """Draws a circle using Bresenham's Circle Drawing Algorithm."""

    # Initial parameters
    x = 0
    y = radius
    d = 3 - 2 * radius

    # Consider the upper half of the first quadrant
    while x <= y:
        # Put eight points via eight-way symmetry
        plt.scatter([x, x, -x, -x, y, y, -y, -y], [y, -y, y, -y, x, -x, x, -x])

        # Make decisions and update parameters
        if d <= 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    # Show the drawing
    plt.title("Circle Drawing Using Bresenham's Circle Drawing Algorithm")
    plt.show()
