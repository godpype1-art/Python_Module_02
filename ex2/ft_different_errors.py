def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        operation_number / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + operation_number
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test_values: list[int] = [0, 1, 2, 3, 4]
    for value in test_values:
        try:
            garden_operations(value)
        except (
            TypeError, ValueError, ZeroDivisionError, FileNotFoundError
                ) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
