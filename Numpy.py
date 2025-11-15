import matplotlib.pyplot as pt
import numpy as np

x = np.random.randint(10,100,50)
y = np.random.randint(-10, 100, 50)

pt.scatter(x, y)
pt.title("scatter plot")
pt.xlabel("x-axis")
pt.ylabel("y-axis")
pt.show()