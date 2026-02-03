#!/usr/bin/env python3
"""Plot a stacked bar chart of fruit counts per person."""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
fruits = ["Apples", "Bananas", "Oranges", "Peaches"]
persons = ["Farrah", "Fred", "Felicia"]

plt.figure(figsize=(8, 6))

bottom = np.zeros(len(persons))
for i, fruit_name in enumerate(fruits):
    plt.bar(
        persons,
        fruit[i],
        bottom=bottom,
        color=colors[i],
        label=fruit_name,
        width=0.5,
    )
    bottom += fruit[i]

plt.xlabel("Person")
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.xticks(fontsize="small")
plt.yticks(np.arange(0, 81, 10), fontsize="small")
plt.legend(title="Fruit", fontsize="small")
plt.ylim(0, 80)
plt.grid(axis="y")

plt.show()
