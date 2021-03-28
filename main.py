from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [255, 0, 0]
matrix = new_matrix()

for y in range(YRES + 1):
    if y % 70 < 35:
        add_edge(matrix, 0, y, 0, XRES // 2, y + (XRES // 2), 0)
        add_edge(matrix, XRES // 2, y + (XRES // 2), 0, XRES, y, 0)
draw_lines(matrix, screen, color)

color = [0, 0, 0]
matrix2 = new_matrix()

for x in range(XRES + 1):
    if x < XRES // 2:
        add_edge(matrix2, x, 0, 0, 0, YRES - x, 0)
    else:
        add_edge(matrix2, x, 0, 0, XRES, x, 0)

draw_lines(matrix2, screen, color)

display(screen)
save_ppm(screen, "binary.ppm")
save_ppm_ascii(screen, "ascii.ppm")
save_extension(screen, "img.png")

