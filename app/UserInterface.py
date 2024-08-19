import re


class UserInterface:
    @staticmethod
    def display_application_email():
        """
        A method to ask the tenant to enter the email used for application

        :return: String - tenant's email
        """
        flag = True
        while flag:
            email = input("\nEnter your email: ")
            if len(email.split()) > 1 or len(email) == 0:
                print("Invalid email. Email should not contain any whitespaces or blank.")
            elif not re.match(r"[^@]+@student\.monash\.edu", email):
                print("Invalid email format. Please use Monash student email.")
            else:
                option = UserInterface.validate_input("Email = ", email)
                if option == "1":
                    return email

    @staticmethod
    def display_application_first_name():
        """
        A method to ask the tenant to enter their first name

        :return: String - tenant's first name
        """
        flag = True
        while flag:
            first_name = input("\nEnter your first name: ")
            if len(first_name.split()) > 1 or len(first_name) == 0:
                print("Invalid first name. First name should not contain any whitespaces or blank.")
            elif not first_name.isalpha():
                print("Invalid input. Input must be characters.")
            else:
                option = UserInterface.validate_input("First name = ", first_name)
                if option == "1":
                    return first_name

    @staticmethod
    def display_application_last_name():
        """
        A method to ask the tenant to enter their last name

        :return: String - tenant's last name
        """
        flag = True
        while flag:
            last_name = input("\nEnter your last name: ")
            if len(last_name.split()) > 1 or len(last_name) == 0:
                print("Invalid last name. Last name should not contain any whitespaces or blank.")
            elif not last_name.isalpha():
                print("Invalid input. Input must be characters.")
            else:
                option = UserInterface.validate_input("Last name = ", last_name)
                if option == "1":
                    return last_name

    @staticmethod
    def display_application_mobile_phone():
        """
        A method to ask the tenant to enter their mobile number

        :return: String - tenant's mobile number
        """
        flag = True
        while flag:
            mobile_phone = input("\nEnter your mobile phone: ")
            if len(mobile_phone.split()) > 1 or len(mobile_phone) == 0:
                print("Invalid mobile phone number. Mobile phone number should not contain any whitespaces or blank.")
            elif not re.match(r"^(?:\+614|04)\d{8}$", mobile_phone):
                print("Invalid mobile phone number. Please use Australia mobile phone number.\n"
                      "(Format: either +61 or 04 followed by 8 digits)")
            else:
                option = UserInterface.validate_input("Mobile phone = ", mobile_phone)
                if option == "1":
                    return mobile_phone

    @staticmethod
    def display_application_option():
        """
        A method to verify the tenant's choice of using their existing information for the application

        :return: String - tenant's option
        """
        print("\nUse the existing personal details from registration form? (1-3): ")
        print("1. Yes \n2. No \n3. Go Back to Property Details")

        options = ["1", "2", "3"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 3.")

    @staticmethod
    def display_application_saving():
        """
        A method to have the tenant enter their savings

        :return: String - tenant's saving
        """
        flag = True
        while flag:
            print("\n(Optional: Press enter to continue)")
            saving = input("Enter your saving: ")
            if len(saving.split()) > 1:
                print("Invalid saving. Saving should not contain any whitespaces.")
            elif len(saving) == 0:
                option = UserInterface.validate_input("Saving = ", "EMPTY")
                if option == "1":
                    return saving
            elif not saving.isnumeric():
                print("Invalid input. Input must be a number.")
            else:
                option = UserInterface.validate_input("Saving = ", saving)
                if option == "1":
                    return saving

    @staticmethod
    def display_enter_property_number_to_remove():
        """
        A method to take the tenant's input on which property they wish to remove from their wishlist

        :return: String - tenant's input
        """
        flag = True
        while flag:
            user_input = input("\nPlease enter the property number to remove: ")
            if len(user_input.split()) > 1 or len(user_input) == 0:
                print("Invalid input. Input should not contain any whitespaces or blank.")
            elif not user_input.isnumeric():
                print("Invalid input. Input must be a number.")
            else:
                return user_input

    @staticmethod
    def display_enter_property_number_to_view():
        """
        A method to take the tenant's input on which property they wish to view more details on

        :return: String - tenant's input
        """
        flag = True
        while flag:
            user_input = input("Please enter the property number to view: ")
            if len(user_input.split()) > 1 or len(user_input) == 0:
                print("Invalid input. Input should not contain any whitespaces or blank.")
            elif not user_input.isnumeric():
                print("Invalid input. Input must be a number.")
            else:
                return user_input

    @staticmethod
    def display_login_email():
        """
        A method to have the tenant enter their email

        :return: String - tenant's email
        """
        flag = True
        while flag:
            email = input("Enter your email: ")
            if email == "exit":
                return email
            elif len(email.split()) > 1 or len(email) == 0:
                print("Invalid email format. Email should not contain any whitespaces or blank.")
            elif not re.match(r"[^@]+@student\.monash\.edu", email):
                print("Invalid email format. Please use Monash student email.")
            else:
                return email

    @staticmethod
    def display_login_password():
        """
        A method to have the tenant enter their password

        :return: String - tenant's password
        """
        flag = True
        while flag:
            password = input("Enter your password: ")
            if password == "exit":
                return password
            elif len(password.split()) > 1 or len(password) == 0:
                print("Invalid password. Password should not contain any whitespaces or blank.")
            elif len(password) < 8:
                print("Invalid password. Password should have a minimum of 8 characters.")
            elif len(password) > 16:
                return password
            elif not re.search(r"[A-Z]", password) or not re.search(r"\d", password):
                print("Invalid password. Password should contain at least one uppercase letter and one number.")
            else:
                return password

    @staticmethod
    def display_main_menu():
        """
        A method to display the main menu options to tenant

        :return: String - tenant's option
        """
        print("Please enter the option (1-5): ")
        print("1. Search Property \n2. View Wishlist \n3. Calculate Optimal Rental Price"
              "\n4. Logout \n5. EXIT MRS")

        options = ["1", "2", "3", "4", "5"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 5.")

    @staticmethod
    def display_opted_property_screen():
        """
        A method to display the tenant's options on property screen

        :return: String - tenant's option
        """
        print("Please enter the option (1-3): ")
        print("1. Apply for the Property \n2. Add to Wishlist \n3. Go Back to Main Menu")

        options = ["1", "2", "3"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 3.")

    @staticmethod
    def display_property_search():
        """
        A method to display a tenant's option on search property screen

        :return: String - tenant's option
        """
        print("\nPlease enter the option (1-2): ")
        print("1. View a Property \n2. Go Back to Main Menu")

        options = ["1", "2"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 2.")

    @staticmethod
    def display_welcome():
        """
        A method to display the tenant's options on the welcome screen

        :return: String - tenant's option
        """
        print("Please enter the option (1-3): ")
        print("1. Login \n2. Registration \n3. EXIT MRS")

        options = ["1", "2", "3"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 3.")

    @staticmethod
    def display_wishlist_option():
        """
        A method to display the tenant's options on the wishlist screen

        :return: String - tenant's option
        """
        print("\nPlease enter the option (1-3): ")
        print("1. View a Property \n2. Remove a Property \n3. Go Back to Main Menu")

        options = ["1", "2", "3"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 3.")

    @staticmethod
    def exit_logo():
        """
        A method to display the application's exit logo

        :return: None
        """
        print("\n*****************************************************************")
        print("      Thank you for using Monash Rental Space (MRS) System")
        print("*****************************************************************")

    @staticmethod
    def main_logo():
        """
        A method to display the application's welcome logo

        :return: None
        """
        print("\n*****************************************************************")
        print("          Welcome to Monash Rental Space (MRS) System")
        print("*****************************************************************\n")

    @staticmethod
    def system_logo():
        """
        A method to display the application's logo

        :return: String - application logo
        """
        monash_rental_system_logo = r"""

        ___  ___                      _      ______           _        _   _____           _                 
        |  \/  |                     | |     | ___ \         | |      | | /  ___|         | |                
        | .  . | ___  _ __   __ _ ___| |__   | |_/ /___ _ __ | |_ __ _| | \ `--. _   _ ___| |_ ___ _ __ ___  
        | |\/| |/ _ \| '_ \ / _` / __| '_ \  |    // _ \ '_ \| __/ _` | |  `--. \ | | / __| __/ _ \ '_ ` _ \ 
        | |  | | (_) | | | | (_| \__ \ | | | | |\ \  __/ | | | || (_| | | /\__/ / |_| \__ \ ||  __/ | | | | |
        \_|  |_/\___/|_| |_|\__,_|___/_| |_| \_| \_\___|_| |_|\__\__,_|_| \____/ \__, |___/\__\___|_| |_| |_|
                                                                                  __/ |                      
                                                                                 |___/                      
        """
        return monash_rental_system_logo

    @staticmethod
    def validate_input(user_text, variable_name):
        """
        A method to validate the tenant's input

        :param user_text: String - tenant's input
        :param variable_name: String - variable name

        :return: String - tenant's option
        """
        print("\n" + user_text + variable_name)
        print("Are you sure with the input?")
        print("1. Yes \n2. No")

        options = ["1", "2"]
        flag = True
        while flag:
            option = input("Enter your option: ")
            if option in options:
                return option
            else:
                print("Invalid Option. Please enter between 1 and 2.")

    @staticmethod
    def validate_input_property(property_no, size):
        """
        A method to validate the property to be removed from wishlist

        :param property_no: int - The property to be removed
        :param size: int - The total number of properties

        :return: boolean
        """
        if property_no <= 0:
            print("Enter value in range.")
            return False
        elif property_no > size:
            print("Enter value in range.")
            return False
        else:
            return True
