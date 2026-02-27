import time
import random

def greedyMethod(items, bagSize):
    profit = 0.0
    remainingCap = bagSize

    for weight, value, ratio in items:
        if remainingCap == 0:
            break

        if weight <= remainingCap:
            profit += value
            remainingCap -= weight
        else:
            fraction = remainingCap / weight
            profit += value * fraction
            remainingCap = 0

    return profit


TRIALS = 20
START_ITEMS = 1000
MAX_ITEMS = 200000
STEP_SIZE = 2000

item_sizes = range(START_ITEMS, MAX_ITEMS + 1, STEP_SIZE)
average_times = []

for n in item_sizes:
    total_time = 0

    for _ in range(TRIALS):

        # Generate random data
        weights = [random.randint(1, 100) for _ in range(n)]
        profits = [random.randint(10, 1000) for _ in range(n)]

        # -------- NEW PART --------
        total_weight = sum(weights)

        # Bag size between 40% and 60% of total weight
        capacity = random.uniform(0.4, 0.6) * total_weight
        # --------------------------

        items = []
        for i in range(n):
            ratio = profits[i] / weights[i]
            items.append((weights[i], profits[i], ratio))

        start = time.perf_counter()

        # O(n log n)
        items.sort(key=lambda x: x[2], reverse=True)

        # O(n)
        greedyMethod(items, capacity)

        end = time.perf_counter()

        total_time += (end - start)

    avg_time = total_time / TRIALS
    average_times.append(avg_time)

    print(f"Completed for n = {n}")

# Save data
with open("items_vs_time.txt", "w") as f:
    f.write("Items\tAverageTime\n")
    for n, t in zip(item_sizes, average_times):
        f.write(f"{n}\t{t}\n")

print("Data saved to items_vs_time.txt")