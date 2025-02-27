#Exercise 4: Using 2 given dictionaries, create a single graph with 2 plots based on the 
#dictionaries. Also implement labels, color, linewidth, legend, and a y range of 0-100
from matplotlib import pyplot as plt

COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}

x1 = COSC1310grades.keys()
x2 = COSC3360grades.keys()
y1 = COSC1310grades.values()
y2 = COSC3360grades.values()

plt.plot(x1, y1, label = 'COSC1310', color = 'r', linewidth = '3')
plt.plot(x2, y2, label = 'COSC3360', color = 'b', linewidth = '3')
plt.legend(loc = 'lower left')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grades')
plt.ylim(0, 100)
plt.show()