import matplotlib.pyplot as plt
import numpy as np
divisions = ["Div-A", "Div-B", "Div-C", "Div_D", "Div-E"]
division_average_marks = [30, 92, 63, 70, 50]
variance = [5, 8, 7, 6, 4]

plt.barh(divisions, division_average_marks, xerr=variance, color='#1E90FF')
plt.title('Bar Graph')
plt.xlabel("Marks")
plt.ylabel("Divisions")
plt.show()
