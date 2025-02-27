#Exercise 5: Do the same as exercise 4 but use two graphs
from matplotlib import pyplot as plt

COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}

x1 = COSC1310grades.keys()
x2 = COSC3360grades.keys()
y1 = COSC1310grades.values()
y2 = COSC3360grades.values()

fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].plot(x1, y1, label = 'COSC1310', color = 'r', linewidth = '3')
ax[0].legend(loc = 'upper right')
ax[0].set_title('COSC1310')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_ylim(0, 100)

ax[1].plot(x2, y2, label = 'COSC3360', color = 'b', linewidth = '3')
ax[1].legend(loc = 'lower left')
ax[1].set_title('COSC3360')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_ylim(0, 100)
plt.show()
