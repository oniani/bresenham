import matplotlib.pyplot as plt


def bresenham(radius: float) -> None:
    """Draw a circle using Bresenham's Circle Drawing Algorithm."""

    # Initial parameters
    x: int = 0
    y: float = radius
    d: float = 3 - 2 * radius

    # Only consider upper 45 degrees in the first quadrant and draw a circle
    while x <= y:
        # Plot eight points using eight-way symmetry
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
