import random


# FRACTIONAL KNAPSACK (GREEDY METHOD)
def fractional_knapsack(weights, profits, capacity):

    n = len(weights)

    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, i))

    items.sort(reverse=True)

    solution = [0] * n
    total_profit = 0

    for ratio, index in items:

        if weights[index] <= capacity:
            solution[index] = 1
            capacity -= weights[index]
            total_profit += profits[index]
        else:
            fraction = capacity / weights[index]
            solution[index] = round(fraction, 2)
            total_profit += profits[index] * fraction
            break

    return solution, round(total_profit, 2)


# GENERATE AND EXECUTE 10 TEST CASES

file = open("fractional_knapsack_testcases.txt", "w")

for t in range(1, 11):

    n = random.randint(4, 15)

    weights = []
    profits = []

    for _ in range(n):
        weights.append(random.randint(5, 50))
        profits.append(random.randint(10, 200))

    capacity = random.randint(40, 200)

    solution, total_profit = fractional_knapsack(weights, profits, capacity)

    output = "\nTest Case " + str(t)
    output += "\n----------------------------------"
    output += "\nNumber of Items: " + str(n)
    output += "\nWeights: " + str(weights)
    output += "\nProfits: " + str(profits)
    output += "\nCapacity: " + str(capacity)
    output += "\n\nOutput (Greedy - Fractional Knapsack):"
    output += "\nSolution Vector: " + str(solution)
    output += "\nTotal Profit: " + str(total_profit)
    output += "\n==================================\n"

    print(output)
    file.write(output)

file.close()