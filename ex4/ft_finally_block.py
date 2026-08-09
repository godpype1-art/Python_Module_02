class GardenError(Exception):

    def __init__(self, error: str = "Unknown garden error") -> None:
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "Invalid plant name to water:") -> None:
        super().__init__(error)


def water_plant(plant_name: str) -> None:
    verified: str = plant_name.capitalize()
    if plant_name == verified:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
        print("..ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
        print("..ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
