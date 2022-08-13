def collect_and_print_data(name, last_name, birth_year, town, email, phone_number):
    print(f'name - {name}, '
          f'last_name - {last_name}, '
          f'birth_year - {birth_year}, '
          f'town - {town}, '
          f'email - {email}, '
          f'phone_number - {phone_number}')


def main():
    name = input("Enter name: ")
    last_name = input("Enter last_name: ")
    birth_year = int(input("Enter birth_year: "))
    town = input("Enter town: ")
    email = input("Enter email: ")
    phone_number = int(input("Enter phone_number: "))

    collect_and_print_data(name, last_name, birth_year, town, email, phone_number)


if __name__ == '__main__':
    main()
