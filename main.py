import random

odds = [1, 1, 1, 1, 100]
max_value = 30
min_value = 20
generation = []
rates = []
probabilities = []
pairs = []
average = 0
last_average = 100000


def initialize():
    for i in range(5):
        element = []
        for j in range(4):
            element.append(round(random.uniform(min_value, max_value), 0))
        generation.append(element)


def calculate_survival_rates(gen):
    for i in range(5):
        rate = 0
        for j in range(4):
            rate += gen[i][j] * odds[j]
        rate -= odds[4]
        if rate < 0:
            rate = rate * -1
        rates.append(rate)


def calculate_probabilities(array_of_rates):
    odd = 0
    for i in range(5):
        odd += 1 / array_of_rates[i]
    for j in range(5):
        probabilities.append((1 / array_of_rates[j]) / odd)


def choose_pairs(prob):
    for i in range(5):
        el1 = random.random()
        el2 = random.random()
        line1 = 0
        line2 = 0
        first = 0
        second = 0
        for j in range(5):
            line1 += prob[j]
            if el1 < line1:
                first = j
                break
            else:
                continue
        for k in range(5):
            line2 += prob[k]
            if el2 < line2:
                second = k
                break
            else:
                continue
        res = [first, second]
        pairs.append(res)


def new_generation(array_of_pairs):
    new_generation_elements = []
    for i in range(5):
        element = []
        if i == 0 or i == 3:
            element.append(generation[(array_of_pairs[i][0])][0])
            element.append(generation[(array_of_pairs[i][1])][1])
            element.append(generation[(array_of_pairs[i][1])][2])
            element.append(generation[(array_of_pairs[i][1])][3])
        if i == 1 or i == 4:
            element.append(generation[(array_of_pairs[i][0])][0])
            element.append(generation[(array_of_pairs[i][0])][1])
            element.append(generation[(array_of_pairs[i][1])][2])
            element.append(generation[(array_of_pairs[i][1])][3])
        if i == 2:
            element.append(generation[(array_of_pairs[i][0])][0])
            element.append(generation[(array_of_pairs[i][0])][1])
            element.append(generation[(array_of_pairs[i][0])][2])
            element.append(generation[(array_of_pairs[i][1])][3])
        new_generation_elements.append(element)
    generation.clear()
    for k in range(len(new_generation_elements)):
        generation.append(new_generation_elements[k])


initialize()
while True:
    indicator = 0
    calculate_survival_rates(generation)
    avg = 0
    for t in range(len(rates)):
        avg += rates[t]
    avg /= len(rates)
    if avg > last_average:
        for u in range(len(generation)):
            generation[u][3] = random.uniform(min_value, max_value)
        calculate_survival_rates(generation)
    for z in range(5):
        if rates[z] == 0:
            print(generation[z])
            indicator += 1
            break
    if indicator != 0:
        break
    calculate_probabilities(rates)
    choose_pairs(probabilities)
    new_generation(pairs)
