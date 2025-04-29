from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(200, 200))
    win.draw_line(line, "red")
    line2 = Line(Point(200, 100), Point(100, 200))
    win.draw_line(line2, "blue")
    win.redraw()
    win.wait_for_close()


main()