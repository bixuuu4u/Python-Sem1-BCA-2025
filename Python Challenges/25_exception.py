# Program to Demonstrate Exception Handling for Various Exceptions

try:
    # Division by zero error
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("Result:", num1 / num2)

    # Index error
    my_list = [1, 2, 3]
    print(my_list[5])

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
