from generators import gen_employees_csv
from main import main


options = {
    0: "Return to Main Menu.",
    1: "Generate Mock Data for Employees.",
}


def generators_main():

    for key, val in options.items():

        print(key, val)

    # Blank line for readability 
    print()

    u_choice = int(input("Enter a choice, based on the above options: "))

    if u_choice == 0:
        main()
    elif u_choice == 1:
        user_num = int(input("Please enter the number of records you want to generate: "))
        gen_employees_csv(user_num)
        print(f'{user_num} record(s) successfully generated. Check the "data" directory for an "employees.csv" file ')
    else:
        print("Please enter a valid int, from the above options.")
        generators_main()
