from faker import Faker
from faker.providers.address import Provider
from csv import DictWriter
from main import main


options = {
    1: "Generate Mock Data for Employees.",
    2: "Generate Mock Data for Servers."
}


# Generate an arbitrary number of fake employees, and write them to a CSV
def gen_employees_csv(filename, records_num):

    emp = open(f'data/{filename}.csv', 'w', newline='')
    fields = ['last_name','first_name','job','email','password_hash','phone','home_address','city','state','zip']
    writer = DictWriter(emp, fieldnames=fields)
    # Write the columns to file
    writer.writeheader()
    
    fake = Faker()

    for i in range(records_num):

        writer.writerow(
            {
                'last_name': fake.last_name(),
                'first_name': fake.first_name(),
                'job': fake.job(),
                'email': fake.email(),
                'password_hash': fake.sha256().upper(),
                'phone': fake.phone_number(),
                'home_address': fake.street_address(),
                'city': fake.city(),
                'state': fake.state(),
                'zip': fake.random_int(11111, 99999),
            }
        )


# Generate fake information about servers
def gen_servers(filename, records_num):

    servers = open(f'data/{filename}.csv', 'w', newline='')
    fields = ['hostname', 'ip_public', 'ip_private', 'mac_address', 'port']
    writer = DictWriter(servers, fieldnames=fields)
    # Write the columns to file
    writer.writeheader()

    fake = Faker()

    for i in range(records_num):

        writer.writerow(
            {
                'hostname': fake.hostname(),
                'ip_public': fake.ipv4_public(),
                'ip_private': fake.ipv4_private(),
                'mac_address': fake.mac_address(),
                'port': fake.port_number(),
            }
        )


def generators_main():

    for key, val in options.items():

        print(key, val)

    # Blank line for readability 
    print()

    u_choice = int(input("Enter a choice, based on the above options: "))
    user_num = int(input("Please enter the number of records you want to generate: "))

    if u_choice == 1:
        user_filename = input("Enter a name (without an extension) for the file containing mock data: ")   
        gen_employees_csv(user_filename, user_num)
        print(f'{user_num} record(s) successfully generated. Check the "data" directory for an "employees.csv" file ')
    elif u_choice == 2:
        user_filename = input("Enter a name (without an extension) for the file containing mock data: ") 
        gen_servers(user_filename, user_num)
        print(f'{user_num} record(s) successfully generated. Check the "data" directory for an "servers.csv" file ')
    else:
        print("***Please enter a valid int, from the below options.***")
        generators_main()
