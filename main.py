from employees import gen_employees


def main():
    
    try:
        # Prompt the user to enter how many records worth of data they want to generate
        user_num = int(input("Please enter an integer (no commas) for how many records of test data you want to generate: "))
        gen_employees(user_num)
        print(f'{user_num} record(s) successfully. Check the "data" directory for an "employees.csv" file ')
    except ValueError:
        print("Please enter an integer. Program terminated.")


main()