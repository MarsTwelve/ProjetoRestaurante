from restaurant import Restaurant

restaurant_boom_salmon = Restaurant(3000, "Boom Salmon", "Japan")
restaurant_boom_salmon.receive_rating("Joel", 5)
restaurant_boom_salmon.receive_rating("Daniel", 4)

restaurant_pasta_masters = Restaurant(2000, "Pasta Masters", "Italy")
restaurant_pasta_masters.receive_rating("Joel", 1)
restaurant_pasta_masters.receive_rating("Daniel", 1)


def print_app_name():
    print("""
███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  ███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝  ██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔══██╗
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░  █████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██║░░░██║██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗  ██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██║░░░██║██╔══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝╚██████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝
""")


def print_options():
    print("1. Register a new restaurant\n"
          "2. List all restaurants\n"
          "3. Activate restaurant\n"
          "4. Add restaurant rating\n"
          "5. Exit\n")


def print_subtitle_text(text):
    print(text, "\n")


def back_to_main_menu():
    input("\nPress any key to return back to the main menu: ")
    main()


def end_session():
    print_subtitle_text("Ending session")


def invalid_option():
    print("The option you entered is invalid!")
    back_to_main_menu()


def choose_option():
    try:
        chosen_option = int(input("Choose a option: "))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            change_restaurant_status()
        elif chosen_option == 4:
            rate_restaurant()
        elif chosen_option == 5:
            end_session()
        else:
            invalid_option()
    except ValueError:
        invalid_option()


def register_new_restaurant():
    print_subtitle_text("Register a new restaurant")
    restaurant_name = input("Please type the restaurant name you wish to register: ")
    restaurant_country = input("Please type the country the restaurant specializes in: ")
    restaurant_code = int(input("Please insert the restaurant code: "))
    Restaurant(restaurant_code, restaurant_name, restaurant_country)
    print(f"The restaurant {restaurant_name} was registered with success")
    back_to_main_menu()


def list_restaurants():
    Restaurant.list_restaurants()
    back_to_main_menu()


def change_restaurant_status():
    print_subtitle_text("Altering restaurant status")
    restaurant_code = int(input("Please type the code of the restaurant: "))
    restaurant_data = (Restaurant.activate_restaurant(restaurant_code))
    if type(restaurant_data) is tuple:
        (restaurant_name, restaurant_status) = restaurant_data
        print(f"The restaurant {restaurant_name} status was successfully changed to: {restaurant_status}")
    else:
        print(f"Could not find restaurant with code: {restaurant_code}")
    back_to_main_menu()


def rate_restaurant():
    restaurant_code = int(input("Please type the code of the restaurant you want to give a rating: "))
    client_name = input("Please type your name: ")
    client_rating = int(input("Please type the rating you want to give: "))
    Restaurant.rate_restaurant(restaurant_code, client_name, client_rating)
    print("Rating added successfully")
    back_to_main_menu()


def main():
    print_app_name()
    print_options()
    choose_option()


if __name__ == '__main__':
    main()
