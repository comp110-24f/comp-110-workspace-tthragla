__author__ = "730698509"


# in between string concatenation call values
def main_planner(guests: int) -> None:
    """calls all functions in program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """compute the number of tea bags needed"""
    return people * 2


# in order to call tea_bags we have to set the old function parameter = new
def treats(people: int) -> int:
    """compute the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


# in order to change the type of an object you must put inside parentheses like float())
def cost(tea_count: int, treat_count: int) -> float:
    "compute the cost of the tea bags and tea"
    return float((tea_count * 0.50) + (treat_count * 0.75))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
