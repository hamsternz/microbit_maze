from microbit import *

# Change the maze if you want
# '#' are walls
# 'S' is the start
# 'G' is the goal (finish point)
# ' ' is empty space

maze = [
   "#################",
   "#S#         #   #",
   "# # # ### # # # #",
   "#   #   # #   # #",
   "# ##### # ### # #",
   "# #   # #   # # #",
   "# ### # ### ### #",
   "#     # # # #   #",
   "### ### # # # ###",
   "#G  #   #   #   #",
   "#################"
]


def pos_valid(pos_x, pos_y):
    if pos_x < 0:
        return False
    if pos_y < 0:
        return False
    if pos_x >= len(maze):
        return False
    if pos_y >= len(maze[pos_x]):
        return False
    return True


def update_display(pos_x, pos_y, blink):
    for x in range(-2, 3):
        for y in range(-2, 3):
            if x == 0 and y == 0:
                if blink == 1:
                    display.set_pixel(x+2, y+2, 9)
                else:
                    display.set_pixel(x+2, y+2, 0)
            elif pos_valid(pos_x+x, pos_y+y):
                c = maze[pos_x+x][pos_y+y]
                if c == "G":
                    display.set_pixel(x+2, y+2, 9)
                elif c == " " or c == "S":
                    display.set_pixel(x+2, y+2, 0)
                else:
                    display.set_pixel(x+2, y+2, 7)
            else:
                display.set_pixel(x+2, y+2, 7)


blink = 0
start_x = 1
start_y = 1
for x in range(0, len(maze)):
    for y in range(0, len(maze[x])):
        if maze[x][y] == 'S':
            start_x = x
            start_y = y
start_x = start_x * 8 + 4
start_y = start_y * 8 + 4
pos_x = start_x
pos_y = start_y

while True:
    if maze[int(pos_x/8)][int(pos_y/8)] == 'G':
        display.show(Image.HEART)
        sleep(1000)
        pos_x = start_x
        pos_y = start_y

    update_display(int(pos_x/8), int(pos_y/8), blink)
    blink = -blink + 1

    x = accelerometer.get_x()
    y = accelerometer.get_y()

    try_pos_x = pos_x
    try_pos_y = pos_y

    if x < -100:
        try_pos_x -= 1
    if x > 100:
        try_pos_x += 1

    if y < -100:
        try_pos_y -= 1
    if y > 100:
        try_pos_y += 1

    if pos_valid(int(try_pos_x/8), int(try_pos_y/8)):
        if maze[int(try_pos_x/8)][int(try_pos_y/8)] != "#":
            pos_x = try_pos_x
            pos_y = try_pos_y
 