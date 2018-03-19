def population_growth():
    population = int(input("What is the starting population? "))
    rate = float(input("What is the rate of growth? "))
    initial = float(input("What is the time already elapsed? "))
    time = float(input("What is the time to be elapsed for prediction? "))

    estimation = population * rate * time / initial

    print(int(estimation))

population_growth()