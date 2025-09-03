def safe_divide(a, b, log_file):
    f = open(log_file, "a")  # open in append mode
    try:
        result = a / b
        f.write(f"SUCCESS: {a} / {b} = {result}\n")
        return result
    except ZeroDivisionError:
        return None
    finally:
        f.close()