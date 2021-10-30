import matplotlib.pyplot as plt
import numpy as np
divisions = ["Div-A", "Div-B", "Div-C", "Div_D", "Div-E"]
division_average_marks = [30, 92, 63, 70, 50]

plt.bar(divisions, division_average_marks, color='#1E90FF')
plt.title('Bar Graph')
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()
