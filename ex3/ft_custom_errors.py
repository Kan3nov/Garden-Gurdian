class Plant:
    def __init__(
            self, name: str, height: float, age: int, water: float,
            ) -> None:
        if (name == ""):
            print("Error, no empty strings are permitted")
        else:
            self._name = name
        if (height < 0):
            print("Error, no negative values are permitted")
        else:
            self._height = height
        if (age < 0):
            print("Error, no negative values are permitted")
        else:
            self._age = age
        self.water = water

    def watering(self, food: float) -> None:
        self.water += food

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old, " +
              f"water {self.water:.2f} ml")


class Garden:
    def __init__(self, tank_content: float):
        self.tank_content = tank_content


class GardenError(Exception):
    def __init__(self, message: str = "Garden is in turmoil !!"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "A plant is suffering !!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Somebody is thirsty"):
        super().__init__(message)


def garden_checking() -> None:
    tomato = Plant("Tomato", 20.0, 220, 12)
    garden = Garden(12)
    try:
        print("Testing PlantError...")
        if (tomato.water < 30):
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)

    try:
        print()
        print("Testing WaterError...")
        water_content = 55
        if (water_content > garden.tank_content):
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)

    try:
        print()
        print("Testing catching all garden errors...")
        if (tomato.water < 30):
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        print()
        water_content = 55
        if (water_content > garden.tank_content):
            raise WaterError
    except GardenError as e:
        print("Caught GardenError:", e)


def main():
    print("=== Custom Garden Errors Demo ===")
    print()
    garden_checking()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
