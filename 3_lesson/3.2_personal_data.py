def collect_and_print_data(name, last_name, birth_year, town, email, phone_number):
    print(f'name - {name}, '
          f'last_name - {last_name}, '
          f'birth_year - {birth_year}, '
          f'town - {town}, '
          f'email - {email}, '
          f'phone_number - {phone_number}')


def main():
    collect_and_print_data(name="kek", last_name="lol", birth_year="1921", town="Novosibirsk", email="www.kek.com", phone_number="112")


if __name__ == '__main__':
    main()
