def input_temperature(temp_str: str) -> int:
    print(f"Input date is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        temp: int = input_temperature("25")
    except Exception as error:
        print(f"Caught input error: {error}")
    else:
        print(f"Temperature is now {temp}°C")
    print()
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input error: {error}")
    else:
        print(f"Temperature is now {temp}°C")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
