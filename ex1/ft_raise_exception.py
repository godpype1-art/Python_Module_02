def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp: int = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    test_values: list[str] = ["25", "abc", "100", "-50"]
    for value in test_values:
        print()
        try:
            temp: int = input_temperature(value)
        except (TypeError, ValueError) as error:
            print(f"Caught input_temperature error: {error}")
        else:
            print(f"Temperature is now {temp}°C")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
