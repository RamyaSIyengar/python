def checkDivision():
    try:
        try:
            x = 1 / 0  # Local exception
        except ZeroDivisionError:
             print("Local handler: Division by zero.")
        else:
            return x

    except Exception as e:
        print(f"Global handler: {e}")  # Won't be executed because the local handler caught the exception.


checkDivision()