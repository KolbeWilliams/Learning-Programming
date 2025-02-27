#Exercise 5: Use a lambda function to calculate the average of the numbers in a list
grades = [90, 74, 87, 80]
output = lambda li: sum(li) / len(li)
print('The average grade is:', output(grades))