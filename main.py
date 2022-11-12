# import numpy as np
# from scipy.optimize import linprog
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# %matplotlib inline

# fig, graph = plt.subplots(figsize=(8, 6))
# graph.grid()

# # Draw constraint lines
# graph.hlines(0, -1, 17.5)
# graph.vlines(0, -1, 12)
# graph.plot(np.linspace(-1, 17.5, 100), 6-0.4 *
#            np.linspace(-1, 17.5, 100), color="c")
# graph.plot(np.linspace(-1, 5.5, 100), 10-2 *
#            np.linspace(-1, 5.5, 100), color="c")
# graph.text(1.5, 8, "$2x_1 + 5x_2 \leq 30$", size=12)
# graph.text(10, 2.5, "$4x_1 + 2x_2 \leq 20$", size=12)
# graph.text(-2, 2, "$x_2 \geq 0$", size=12)
# graph.text(2.5, -0.7, "$x_1 \geq 0$", size=12)
