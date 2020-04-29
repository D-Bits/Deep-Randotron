from faker import Faker
from faker.providers.address import Provider
from csv import DictWriter


# Generate an arbitrary number of fake employees, and write them to a CSV
def gen_employees_csv(emp_num):

    emp = open('data/employees.csv', 'w', newline='')
    fields = ['last_name','first_name','email','emp_password', 'phone', 'home_address','city','state', 'zip']
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
                'emp_password': fake.sha256().upper(),
                'phone': fake.phone_number(),
                'home_address': fake.street_address(),
                'city': fake.city(),
                'state': fake.state(),
                'zip': fake.random_int(00000, 99999),
            }
        )

