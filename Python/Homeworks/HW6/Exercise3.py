#Exercise 3: Plot absolute value graph for user-provided x-values and ask user for color, marker, marker size, linestyle,
#linewidth, label, legend location, x label, y label, and title
from matplotlib import pyplot as plt

minimum = int(input('Enter  minimum value for x: '))
maximum = int(input('Enter maximum value for x: '))
x = [x for x in range(minimum, maximum + 1)]
y = [-i if i <= 0 else i for i in x]

colorUsed = input('Enter color: ')
markerUsed = input('Enter marker: ')
markerSizeUsed = int(input('Enter marker size: '))
lineStyleUsed = input('Enter linestyle: ')
lineWidthUsed = input('Enter line width: ')
labelUsed = input('Enter label: ')
legendLocationUsed = input('Enter legend location: ')
xLabelUsed = input('Enter x label: ')
yLabelUsed = input('Enter y label: ')
titleUsed = input('Enter title: ')

plt.plot(x, y, color = colorUsed, marker = markerUsed, linestyle = lineStyleUsed, linewidth = lineWidthUsed, markersize = markerSizeUsed, label = labelUsed)
plt.xlabel(xLabelUsed)
plt.ylabel(yLabelUsed)
plt.title(titleUsed)
plt.legend(loc = f'{legendLocationUsed}')
plt.show()