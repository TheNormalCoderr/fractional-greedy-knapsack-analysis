import matplotlib.pyplot as plt
import math

item_sizes = []
average_times = []

# Read saved data
with open("items_vs_time.txt", "r") as f:
    next(f)
    for line in f:
        n, t = line.strip().split()
        item_sizes.append(int(n))
        average_times.append(float(t))

# -------- Create theoretical n log n --------
nlogn = []

for n in item_sizes:
    value = n * math.log2(n)   # n log n
    nlogn.append(value)

# -------- Scale theoretical curve --------
# Scale so that last point roughly matches experimental value
scale_factor = average_times[-1] / nlogn[-1]
nlogn_scaled = [x * scale_factor for x in nlogn]

# -------- Plot --------
plt.figure()

plt.plot(item_sizes, average_times, label="Experimental Time")
plt.plot(item_sizes, nlogn_scaled, linestyle="--", label="Theoretical n log n")

plt.xlabel("Number of Items (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Greedy Knapsack: Experimental vs Theoretical")
plt.legend()
plt.grid()

plt.show()