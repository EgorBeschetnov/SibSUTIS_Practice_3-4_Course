import random

POPULATION_SIZE = 100
CHROMOSOME_LENGTH = 20
MUTATION_RATE = 0.05
GENERATIONS = 100 

def create_individ():
    return [random.randint(0, 100) for _ in range(CHROMOSOME_LENGTH)]

def create_population():
    return [create_individ() for _ in range(POPULATION_SIZE)]

def fitness(individ):
    return (sum(individ) / len(individ))

def select_parent(population):
    contestants = random.sample(population, 3)
    return max(contestants, key = fitness)

def crossing(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutation(individ):
    for i in range(len(individ)):
        if random.random() < MUTATION_RATE:
            individ[i] = i - individ[i]
    return individ

print("--- Генетический алгоритм на 100 особей ---\n")
print(f"Параметры:")
print(f"- Размер популяции: {POPULATION_SIZE} особей")
print(f"- Длина хромосомы: {CHROMOSOME_LENGTH} генов")
print(f"- Вероятность мутации: {MUTATION_RATE*100}%")
print(f"- Количество поколений: {GENERATIONS}\n")

population = create_population()

for generation in range(GENERATIONS):

    fitnesses = [fitness(individ) for individ in population]

    best_individ = max(population, key = fitness)
    best_fitness = fitness(best_individ)

    if generation % 10 == 0:
        avg_fitness = sum(fitnesses) / len(fitnesses)
        print(f"Поколение {generation:3d}: лучшая приспособленность = {best_fitness:5.2f}, средняя = {avg_fitness:5.2f}")
    
    new_population = []

    for _ in range(POPULATION_SIZE):

        parent1 = select_parent(population)
        parent2 = select_parent(population)

        child = crossing(parent1, parent2)

        child = mutation(child)

        new_population.append(child)

    population = new_population

final_fitnesses = [fitness(individ) for individ in population]
final_best = max(population, key = fitness)
best_fitness = fitness(final_best)
avg_fitness = sum(final_fitnesses) / len(final_fitnesses)

print(f"\n--- Результат ---")
print(f"Лучшие особи: {final_best}")
print(f"Приспособленность лучшей особи: {best_fitness}%")
print(f"Средняя приспособленность популяции: {avg_fitness:.2f}%")
print(f"Максимально возможная приспособленность: 100")

perfect_individual = sum(1 for individ in population if fitness(individ) == CHROMOSOME_LENGTH)