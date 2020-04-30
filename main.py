from generators import generators_main
from converters import converter_main


# Store the user's options in a dictionary
options = {
    1: 'Generate Random Data.',
    2: 'Convert random CSV data to other formats.'
}


def main():
    
    # Blank line for readability 
    print()

    for key, val in options.items():

        print(key, val)

    print()

    u_choice = int(input("Enter a choice, based on the below options: "))

    if u_choice == 1:
        generators_main()
    elif u_choice == 2:
        converter_main()
    else:
        print()
        print("***Please enter a valid int, from the above options.***")
        main()

main()