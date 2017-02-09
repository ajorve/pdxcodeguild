"""
Population Sim
In a small town the population is 1000 at the beginning of a year.
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town.
How many years does the town need to see its population greater or equal to 1200 inhabitants?
Write a function to determine the the answer given input of the starting population, the number of additional inhabitants coming each year, the anual percent of increase, and the target population.
solve(start_pop, additional, delta, target)
In: solve(1000, 50, 2, 1200)
Out: 3 Years.
"""


def pop_sim(start_pop, growth, births, target):
    """
    Write a function to determine the the answer given
    input of the starting population,
    the number of additional inhabitants coming each year,
    the annual percent of increase,
    and the target population.

    >>> pop_sim(1000, 50, 2, 1200)
    It took approximately 3 years to get to 1200 people

    :param start_pop: int
    :param growth: int
    :param births: int
    :param target: int
    :return: str
    """

    population = start_pop
    new_inhabs = births
    pop_change = growth
    target_pop = target

    years_past = 0

    while population < target_pop:
        result = ((population * (pop_change * .01)) + new_inhabs)
        population += result
        years_past += 1

    message = f"It took approximately {years_past} years to get to {target_pop} people"
    print(message)
    return message


def pop_collection():
    print("Welcome to the Global Population Simulator!")
    start_pop = int(input("What is the current population?:  "))
    growth = int(input("What is the average annual growth rate % (use whole number) ?:  "))
    births = int(input("How many annual births?:  "))
    target = int(input("What is the desired target population?:  "))

    data = (start_pop, growth, births, target)
    pop_sim(*data)


if __name__ == "__main__":
    pop_collection()