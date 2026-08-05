def basic_calculate(operation: str, x: float, y: float) -> float:
    """Core calculation engine processing on local host CPU."""
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero value bounds.")
        return x / y
    else:
        raise ValueError(f"Unknown operation profile passed: {operation}")
