class GardenError(Exception):

    def __init__(self, error: str = "Unknown garden error"):
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "The tomato plant is wilting!"):
        super().__init__(error)


class WaterError(GardenError):
    def __init__(self, error: str = "Not enough water in the tank!"):
        super().__init__(error)


def main() -> None:
    print("=== Custom Garden Error Demo ===")
    print()
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    print()
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        raise WaterError()
    except GardenError as error:
        print(f"Caught {GardenError.__name__}: {error}")
    print()
    print("All custom types work correctly!")


if __name__ == "__main__":
    main()
