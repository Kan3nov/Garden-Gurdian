def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = -1
    try:
        temp = int(temp_str)
    except Exception:
        print("Error : Invalid input")
    else:
        print(f"Temperature is now {temp}°C")
    return temp


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    print("All tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
