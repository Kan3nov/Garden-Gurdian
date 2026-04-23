def garden_oprations(op_num: int) -> None:
    print(f"Testing operation {op_num}...")
    try:
        if (op_num == 0):
            int("meow")
        elif (op_num == 1):
            1 / 0
        elif (op_num == 2):
            open("meow")
        elif (op_num == 3):
            '1' + 1
        else:
            print("Operation completed successfully")
    except ValueError as e:
        print("Caught ValueError:", e)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    except TypeError as e:
        print("Caught TypeError:", e)


def test_error_types() -> None:
    garden_oprations(0)
    print()
    garden_oprations(1)
    print()
    garden_oprations(2)
    print()
    garden_oprations(3)
    print()
    garden_oprations(4)
    print()


def main():
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
