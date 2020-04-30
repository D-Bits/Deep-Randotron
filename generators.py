from faker import Faker
from faker.providers.address import Provider
from csv import DictWriter



options = {
    0: "Return to Main Menu.",
    1: "Generate Mock Data for Employees.",
}


# Generate an arbitrary number of fake employees, and write them to a CSV
def gen_employees_csv(emp_num):

    emp = open('data/employees.csv', 'w', newline='')
    fields = ['last_name','first_name','email','password_hash','phone','home_address','city','state','zip']
    writer = DictWriter(emp, fieldnames=fields)
    # Write the columns to file
    writer.writeheader()
    
    fake = Faker()

    for i in range(emp_num):

        writer.writerow(
            {
                'last_name': fake.last_name(),
                'first_name': fake.first_name(),
                'email': fake.email(),
                'password_hash': fake.sha256().upper(),
                'phone': fake.phone_number(),
                'home_address': fake.street_address(),
                'city': fake.city(),
                'state': fake.state(),
                'zip': fake.random_int(11111, 99999),
            }
        )


def generators_main():

    for key, val in options.items():

        print(key, val)

    # Blank line for readability 
    print()

    u_choice = int(input("Enter a choice, based on the above options: "))

    if u_choice == 1:
        user_num = int(input("Please enter the number of records you want to generate: "))
        gen_employees_csv(user_num)
        print(f'{user_num} record(s) successfully generated. Check the "data" directory for an "employees.csv" file ')
    else:
        print("***Please enter a valid int, from the below options.***")
        generators_main()
