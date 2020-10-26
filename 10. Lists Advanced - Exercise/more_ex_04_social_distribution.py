population = list(map(int, input().split(", ")))
min_wealth = int(input())

for index, person in enumerate(population):
    max_wealth_index = population.index(max(population))
    max_wealth_person = population[max_wealth_index]

    if person < min_wealth:
        difference = min_wealth - person
        if max_wealth_person - difference >= min_wealth:
            population[index] += difference
            population[max_wealth_index] -= difference
        else:
            print("No equal distribution possible")
            break
else:
    print(population)
