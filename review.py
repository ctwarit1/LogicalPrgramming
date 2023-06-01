"""
This robot roams around a 2D grid. It starts at (0, 0) facing
 North. After each time it moves, the robot rotates 90 degrees clockwise.
  Given the amount the robot has moved each time, you have to calculate the robot's final position.
To illustrate, if the robot is given the movements 20, 30, 10,
 40 then it will move:
20 steps North, now at (0, 20)
30 steps East, now at (30, 20)
10 steps South. now at (30, 10)
40 steps West, now at (-10, 10)
...and will end up at coordinates (-10, 10).
Examples
track_robot(20, 30, 10, 40) ➞ [-10, 10]
track_robot() ➞ [0, 0]
# No movement means the robot stays at (0, 0).
track_robot(-10, 20, 10) ➞ [20, -20]
# The amount to move can be negative.
Notes
Each movement is an integer (whole number).
"""
# track_robot = (20, 30, 10, 40)
# track_robot = (-10, 20, 10)
track_robot = ()
x, y = 0, 0
first_pos = 0
for i in track_robot:
    if first_pos == 0:
        y += i
    elif first_pos == 1:
        x += i
    elif first_pos == 2:
        y -= i
    elif first_pos == 3:
        x -= i

    first_pos = (first_pos + 1) % 4
print([x, y])
