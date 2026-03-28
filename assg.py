import matplotlib.pyplot as plt
# -------------------------------
# Bresenham's Line Drawing Algorithm
# -------------------------------
def bresenham_line(x1, y1, x2, y2):
  points = []
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  sx = 1 if x2 > x1 else -1
  sy = 1 if y2 > y1 else -1
  err = dx - dy
  while True:
    points.append((x1, y1))
    if x1 == x2 and y1 == y2:
    break
    e2 = 2 * err
    if e2 > -dy:
    err -= dy
    x1 += sx
    if e2 < dx:
    err += dx
    y1 += sy
  return points
# -------------------------------
# Bresenham's Circle Drawing Algorithm
# -------------------------------
def bresenham_circle(xc, yc, r):
  points = []
  x = 0
  y = r
  d = 3 - 2 * r
  while x <= y:
    # 8-way symmetry
    points.extend([
    (xc + x, yc + y), (xc - x, yc + y),
    (xc + x, yc - y), (xc - x, yc - y),
    (xc + y, yc + x), (xc - y, yc + x),
    (xc + y, yc - x), (xc - y, yc - x)
    ])
    if d < 0:
      d = d + 4 * x + 6
    else:
      d = d + 4 * (x - y) + 10
      y -= 1
    x += 1
  return points
# -------------------------------
# Drawing the Car
# -------------------------------
# Rectangle coordinates
top_left = (20, 20)
bottom_right = (100, 60)
# Extract rectangle corners
x1, y1 = top_left
x2, y2 = bottom_right
# Rectangle edges
rectangle_points = []
rectangle_points += bresenham_line(x1, y1, x2, y1) # Top
rectangle_points += bresenham_line(x2, y1, x2, y2) # Right
rectangle_points += bresenham_line(x2, y2, x1, y2) # Bottom
rectangle_points += bresenham_line(x1, y2, x1, y1) # Left
# Wheels
left_wheel = bresenham_circle(40, 10, 10)
right_wheel = bresenham_circle(80, 10, 10)
# Combine all points
all_points = rectangle_points + left_wheel + right_wheel
# Plot
x_vals = [p[0] for p in all_points]
y_vals = [p[1] for p in all_points]
plt.figure()
plt.scatter(x_vals, y_vals, s=5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Car-like Structure using Bresenham Algorithms")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
