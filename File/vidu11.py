import matplotlib.pyplot as plt
import numpy as np
divisions = ["Div-A", "Div-B", "Div-C", "Div_D", "Div-E"]
division_average_marks = [30, 92, 63, 70, 50]
boys_average_marks = [68, 67, 77, 61, 70]

index = np.arange(5)
width = 0.30

plt.bar(index, division_average_marks, width, color='#1E90FF', label='Division Marks')
plt.bar(index+width, division_average_marks, width, color='red', label='Boys Marks')

plt.xlabel("Marks")
plt.ylabel("Divisions")
plt.xticks(index+ width/2, divisions)

plt.legend(loc='best')
plt.show()
