def safe_divide():
    print("--- Safe Division Calculator ---")
    try:
        num1_str = input("Enter the numerator: ")
        num1 = float(num1_str) 
        
        num2_str = input("Enter the denominator: ")
        num2 = float(num2_str) 
        
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Calculation attempt complete.")

if __name__ == "__main__":
    safe_divide()
