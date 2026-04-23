def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = -1
    try:
        temp = int(temp_str)
        if (temp < 0):
            raise ValueError(f"Error : {temp}°C is too cold for plants " +
                             "(min 0°C)")
        elif (temp > 40):
            raise ValueError(f"Error : {temp}°C is too hot for plants " +
                             "(max 40°C)")
    except Exception as e:
        print(e)
    else:
        print(f"Temperature is now {temp}°C")
    return temp


def test_temperature() -> None:
    input_temperature("25")
    print()
    input_temperature("abc")
    print()
    input_temperature("100")
    print()
    input_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature Checker ===")
    test_temperature()


if __name__ == "__main__":
    main()
