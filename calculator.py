import math

print("=" * 50)
print("\t\tSIMPLE CALCULATOR")
print("=" * 50)
while True:
    print("\n\033[33mOperations:\033[0m")
    print("\033[34m[1]\033[0m Addition (+)")
    print("\033[34m[2]\033[0m Subtraction (-)")
    print("\033[34m[3]\033[0m Multiplication (*)")
    print("\033[34m[4]\033[0m Division (/)")
    print("\033[34m[5]\033[0m Mpdulus (%)")
    print("\033[34m[6]\033[0m Power (^)")
    print("\033[34m[7]\033[0m Square Root (√)")
    print("\033[34m[8]\033[0m Exit (X)")
    print("-" * 50)
    try:
        user_choice = int(input("Enter your choice(1-8): "))
        if user_choice == 1:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            print(
                f"\033[32mResult:\033[0m{first_number:2g} + {second_number:2g} = \033[32m{first_number+second_number:2g}\033[0m"
            )
        elif user_choice == 2:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            print(
                f"\033[32mResult:\033[0m{first_number:2g} - {second_number:2g} = \033[32m{first_number-second_number:2g}\033[0m"
            )
        elif user_choice == 3:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            print(
                f"\033[32mResult:\033[0m{first_number:2g} x {second_number:2g} = \033[32m{first_number*second_number:2g}\033[0m"
            )
        elif user_choice == 4:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            if second_number == 0:
                print("\033[33mThis number is not divisible by zero\033[0m")
            else:
                print(
                    f"\033[32mResult:\033[0m{first_number:2g} / {second_number:2g} = \033[32m{first_number/second_number:2g}\033[0m"
                )
        elif user_choice == 5:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            if second_number == 0:
                print("\033[33mThis number is not modulus by zero\033[0m")
            else:
                print(
                    f"\033[32mResult:\033[0m{first_number:2g} % {second_number:2g} = \033[32m{first_number%second_number:2g}\033[0m"
                )
        elif user_choice == 6:
            first_number = float(input("\nEnter First Number: "))
            second_number = float(input("\nEnter Second Number: "))
            print("-" * 50)
            print(
                f"\033[32mResult:\033[0m{first_number:2g} ^ {second_number:2g} = \033[32m{first_number**second_number:2g}\033[0m"
            )
        elif user_choice == 7:
            first_number = float(input("\nEnter First Number: "))
            print("-" * 50)
            if first_number < 0:
                print(
                    "\033[33mCannot calculate square root of a negative number\033[0m"
                )
            else:
                result = math.sqrt(first_number)
                print(
                    f"\033[32mResult:\033[0m √{first_number:2g} = \033[32m{result:2g}\033[0m"
                )
        elif user_choice == 8:
            print("\033[32mThankyou for using simple calculator. Goodbye!\033[0m")
            break
        else:
            print("-" * 50)
            print("\033[31mInvalid Option!\033[0m")
        print("-" * 50)
    except ValueError:
        print("-" * 50)
        print("\033[31mPlease Enter the valid number\033[0m")
        print("-" * 50)
    except KeyboardInterrupt:
        print("\n")
        break
