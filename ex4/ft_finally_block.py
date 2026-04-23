class GardenError(Exception):
    def __init__(self, message: str = "Garden is in turmoil !!"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "A plant is suffering !!"):
        super().__init__(message)

def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f'Watering {plant_name}: [OK]')
    else:
        raise PlantError(f"Plant '{plant_name}' doesn't like its name!")


def test_watering_system(plants : list[str]) -> None:
    print("Opening the watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e, ".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()