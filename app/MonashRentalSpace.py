from Property import *
from TenantRegistration import *
from TenantApplication import *
from Utility import *
from UserInterface import *
from Wishlist import *
import json
from tabulate import tabulate


class MonashRentalSpace:
    def __init__(self, list_of_properties=None, list_of_tenants=None, list_of_wishlists=None,
                 list_of_applications=None, utility=Utility()):
        """
        A method to initialise the attributes of the MonashRentalSpace class

        :param list_of_properties: A list of properties
        :param list_of_tenants: A list of tenants
        :param list_of_wishlists: A list of tenant's wishlist
        :param list_of_applications: A list of tenant's rental applications
        :param utility: The utility function
        """

        if list_of_properties is None:
            list_of_properties = []
        self.__list_of_properties = list_of_properties
        if list_of_tenants is None:
            list_of_tenants = []
        self.__list_of_tenants = list_of_tenants
        if list_of_wishlists is None:
            list_of_wishlists = []
        self.__list_of_wishlists = list_of_wishlists
        if list_of_applications is None:
            list_of_applications = []
        self.__list_of_applications = list_of_applications
        self.__utility = utility

    def add_application(self, obj_application):
        """
        Method to add rental application to its list

        :param obj_application: Rental application object

        :return: None
        """
        self.__list_of_applications.append(obj_application)

    def add_to_wishlist(self, property_name, tenant):
        """
        A method to add to wishlist

        :param property_name: The property to be added to wishlist
        :param tenant: The tenant whose wants to update his wishlist

        :return: None
        """
        # print("Function called")
        tenant_email = tenant.get_email()
        for wishlist in self.__list_of_wishlists:
            # print("Iterating wishlist",wishlist.get_tenant_email(),tenant_email)
            if wishlist.get_tenant_email() == tenant_email:
                wishlist.add_to_wishlist(property_name)
                # Abhishek Save to wishlist.txt happens when logout
                self.save_list_of_wishlists()

    def check_application_exists(self, obj_property):
        """
        A method to check if application exists

        :param obj_property: Property object

        :return: boolean
        """
        application_properties = []
        for application in self.__list_of_applications:
            application_properties.append(application.get_property_address())

        if obj_property.get_property_address() in application_properties:
            return True
        else:
            return False

    def check_property_exists(self):
        """
        A method to check if the property exists

        :return: property object
        """
        obj_ui = UserInterface()
        property_list = self.__list_of_properties
        flag = True
        while flag:
            opted_property_number = obj_ui.display_enter_property_number_to_view()
            index = int(opted_property_number) - 1
            if len(self.__list_of_properties) > index:
                return property_list[index]
            else:
                print("Invalid input. Property number is out of range.")

    def check_tenant_exists(self):
        """
        A method to check if the tenant exists

        :return: A list containing a true or false value and the corresponding tenant object
        """
        obj_ui = UserInterface()
        obj_tenant_useless = TenantApplication()
        flag = True
        while flag:
            print("\nEnter 'exit' to go back.")
            email = obj_ui.display_login_email()
            if email == "exit":
                login = [False, obj_tenant_useless]
                return login
            password = obj_ui.display_login_password()
            if password == "exit":
                login = [False, obj_tenant_useless]
                return login
            tenant_credential = (email, password)

            for tenant in self.__list_of_tenants:
                if tenant.get_email() == tenant_credential[0] and tenant.get_password() == tenant_credential[1]:
                    login = [True, tenant]
                    return login

            print("The credential does not exist. Please try again!")

    def display_list_of_wishlists(self, tenant):
        """
         A method to display all the wishlists

        :param tenant: The tenant object

        :return: None
        """
        tenant_email = tenant.get_email()
        header = ['Property_no', 'Property Address', 'Added to Wishlist On', 'Property Suburb', 'Property Price',
                  'Property Condition', 'Property Type', 'Property State', 'Listed Date']
        data = [header]
        index = 0
        for wishlist in self.__list_of_wishlists:
            # print("Iterating wishlist",wishlist.get_tenant_email(),tenant_email)
            if wishlist.get_tenant_email() == tenant_email:
                for each in wishlist.get_property_details():
                    index += 1
                    for each_property in self.__list_of_properties:
                        if each_property.get_property_address() == each["property_address"]:
                            each_row = [index, each["property_address"], each["added_time"],
                                        each_property.get_property_suburb(),
                                        each_property.get_property_price(), each_property.get_property_condition(),
                                        each_property.get_property_type(),
                                        each_property.get_property_state(),
                                        each_property.get_property_listed_date()]
                            data.append(each_row)

        print("\n My wishlist: \n")
        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

    def display_properties_on_search(self, tenant):
        """
        A method to display the properties available

        :param tenant: Tenant object

        :return: None
        """
        header = ['Wishlist Status', 'Property Number', 'Property Address', 'Property Suburb', 'Property Price',
                  'Property Condition', 'Property Type', 'Property State']
        data = [header]
        # Star starts here!
        list_of_property_address_on_search = []
        for each in self.__list_of_properties:
            property_address = each.get_property_address()
            list_of_property_address_on_search.append(property_address)

        wishlist_object = []
        for thing in self.__list_of_wishlists:
            if thing.get_tenant_email() == tenant.get_email():
                wishlist_object.append(thing)

        wishlist_object_property_addresses = []
        for property_address in wishlist_object[0].get_property_details():
            wishlist_object_property_addresses.append(property_address.get("property_address"))

        star_list = []
        for each in list_of_property_address_on_search:
            if each in wishlist_object_property_addresses:
                star_list.append("★")
            else:
                star_list.append("☆")

        index = 0
        for each in self.__list_of_properties:
            index2 = index + 1
            each_row = [star_list[index], index2, each.get_property_address(), each.get_property_suburb(),
                        each.get_property_price(), each.get_property_condition(), each.get_property_type(),
                        each.get_property_state()]
            data.append(each_row)
            index += 1

        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

    def extract_list_of_applications(self):
        """
        A method to extract list of all application

        :return: None
        """
        data = []

        with open("./data/application.txt", 'r') as file:
            file_content = file.read()
            file_content_dict = json.loads(file_content)
            application_details = file_content_dict.get("application_details")
            for item in application_details:
                obj_application = TenantApplication(first_name=item["first_name"], last_name=item["last_name"],
                                                    email=item["email"], mobile_phone=item["mobile_phone"],
                                                    saving=item["saving"],
                                                    property_address=item["property_address"])
                data.append(obj_application)

        self.__list_of_applications = data

    def extract_list_of_properties(self):
        """
        A method to extract list of all properties

        :return: None
        """
        data = []

        with open("./data/property.txt", 'r') as file:
            file_content = file.read()
            file_content_dict = json.loads(file_content)
            property_details = file_content_dict.get("property_details")
            for item in property_details:
                obj_property = Property(item["property_address"], item["property_suburb"],
                                        item["property_price"], item["property_condition"],
                                        item["property_type"], item["property_state"],
                                        item["property_description"], item["property_agent"],
                                        item["property_management_contact_number"],
                                        item["property_application_url"],
                                        item["property_inspection_date_time"],
                                        item["property_listed_date"])
                data.append(obj_property)

        self.__list_of_properties = data

    def extract_list_of_tenants(self):
        """
        A method to extract list of all tenants

        :return: None
        """
        data = []

        with open("./data/tenant.txt", 'r') as file:
            file_content = file.read()
            file_content_dict = json.loads(file_content)
            tenant_details = file_content_dict.get("tenant_details")
            for tenant in tenant_details:
                obj_tenant = TenantRegistration(tenant["first_name"], tenant["last_name"],
                                                tenant["email"], tenant["mobile_phone"],
                                                tenant["password"], tenant["gender"],
                                                tenant["preferred_renting_cost"], tenant["preferred_suburb"])
                data.append(obj_tenant)

        self.__list_of_tenants = data

    def extract_list_of_wishlists(self):
        """
        A method to extract list of all wishlists

        :return: None
        """
        data = []
        with open("./data/wishlist.txt", 'r') as file:
            file_content = file.read()
            file_content_dict = json.loads(file_content)
            wishlist_details = file_content_dict.get("wishlist_details")
            for wishlist in wishlist_details:
                obj_wishlist = Wishlist(wishlist["tenant_email"], wishlist["property_details"])
                data.append(obj_wishlist)

        self.__list_of_wishlists = data

    def get_list_of_applications(self):
        """
        Accessor method to list all tenant applications

        :return: list of tenant applications
        """
        return self.__list_of_applications

    def get_list_of_properties(self):
        """
        Accessor method to list all properties

        :return: list of all properties
        """
        return self.__list_of_properties

    def get_list_of_tenants(self):
        """
        Accessor method to list all tenants

        :return: list of all tenants
        """
        return self.__list_of_tenants

    def get_list_of_wishlists(self):
        """
        Accessor method to list all the wishlists

        :return: list of wishlists
        """
        return self.__list_of_wishlists

    def get_utility(self):
        """
        Accessor method to get utility object

        :return: utility object
        """
        return self.__utility

    def remove_property_from_wishlist(self, property_name, tenant):
        """
        A method to remove a property from Tenant's wishlist

        :param property_name: Name of property
        :param tenant: Tenant object

        :return: None
        """
        tenant_email = tenant.get_email()
        for wishlist in self.__list_of_wishlists:
            if wishlist.get_tenant_email() == tenant_email:
                wishlist.remove_from_wishlist(property_name)
                self.save_list_of_wishlists()

    def run(self):
        """
        A method to execute the entire application

        :return: None
        """
        obj_ui = UserInterface()
        self.extract_list_of_properties()
        self.extract_list_of_tenants()
        self.extract_list_of_wishlists()
        self.extract_list_of_applications()

        flag_layer_1 = True
        while flag_layer_1:
            print(obj_ui.system_logo())
            welcome_option = obj_ui.display_welcome()

            if welcome_option == "1":
                login = self.check_tenant_exists()

                flag_layer_2 = True
                while flag_layer_2:
                    if login[0]:
                        obj_ui.main_logo()
                        main_menu_option = obj_ui.display_main_menu()
                        if main_menu_option == "1":
                            print("\nSearch Results:\n")
                            self.display_properties_on_search(login[1])
                            search_property_option = obj_ui.display_property_search()
                            if search_property_option == "1":
                                selected_property = self.check_property_exists()

                                flag_layer_3 = True
                                while flag_layer_3:
                                    selected_property.display_property_details()
                                    property_details_option = obj_ui.display_opted_property_screen()
                                    if property_details_option == "1":
                                        if not self.check_application_exists(selected_property):
                                            application_option = obj_ui.display_application_option()
                                            if application_option == "1":
                                                obj_tenant = login[1]
                                                mobile_phone_opt1 = obj_ui.display_application_mobile_phone()
                                                saving_opt1 = obj_ui.display_application_saving()
                                                obj_application = TenantApplication(
                                                    first_name=obj_tenant.get_first_name(),
                                                    last_name=obj_tenant.get_last_name(),
                                                    email=obj_tenant.get_email(),
                                                    mobile_phone=mobile_phone_opt1,
                                                    saving=saving_opt1,
                                                    property_address=selected_property.get_property_address())
                                                self.add_application(obj_application)
                                                print("\nApplication has been successfully submitted!\n")
                                                input("Press any keys to go back...")
                                            elif application_option == "2":
                                                first_name_opt2 = obj_ui.display_application_first_name()
                                                last_name_opt2 = obj_ui.display_application_last_name()
                                                email_opt2 = obj_ui.display_application_email()
                                                mobile_phone_opt2 = obj_ui.display_application_mobile_phone()
                                                saving_opt2 = obj_ui.display_application_saving()
                                                obj_application = TenantApplication(
                                                    first_name=first_name_opt2,
                                                    last_name=last_name_opt2,
                                                    email=email_opt2,
                                                    mobile_phone=mobile_phone_opt2,
                                                    saving=saving_opt2,
                                                    property_address=selected_property.get_property_address())
                                                self.add_application(obj_application)
                                                print("\nApplication has been successfully submitted!\n")
                                                input("Press any keys to go back...")
                                            elif application_option == "3":
                                                continue
                                        else:
                                            print("\nSorry, only one application is allowed to be submitted to "
                                                  "the same house.\n")
                                            # To create a stop before reiterate the while loop
                                            input("Press any keys to go back...")
                                    elif property_details_option == "2":
                                        self.add_to_wishlist(selected_property.get_property_address(), login[1])
                                        input("Press any keys to go back...")
                                    elif property_details_option == "3":
                                        flag_layer_3 = False
                            elif search_property_option == "2":
                                continue
                        elif main_menu_option == "2":
                            self.display_list_of_wishlists(login[1])
                            wishlist_option = obj_ui.display_wishlist_option()
                            if wishlist_option == "1":
                                print("\nYet to be implemented")
                                input("Press any keys to go back...")
                            elif wishlist_option == "2":
                                list_of_properties = []
                                property_no_to_remove = ""
                                size_of_wishlist = 0
                                for wishlist in self.__list_of_wishlists:
                                    if wishlist.get_tenant_email() == login[1].get_email():
                                        list_of_properties = wishlist.get_property_address()
                                        size_of_wishlist = len(list_of_properties)
                                # if len(size_of_wishlist == 0):
                                    is_valid = False
                                    while not is_valid:
                                        property_no_to_remove = obj_ui.display_enter_property_number_to_remove()
                                        is_valid = obj_ui.validate_input_property(int(property_no_to_remove),
                                                                                  len(list_of_properties))
                                    property_name = list_of_properties[int(property_no_to_remove)-1]
                                    print(list_of_properties[int(property_no_to_remove)-1])
                                    self.remove_property_from_wishlist(property_name, login[1])
                                    input("Press any keys to go back...")
                                else:
                                    print("\nNothing to be removed.")
                                    input("Press any keys to go back...")
                            elif wishlist_option == "3":
                                continue
                        elif main_menu_option == "3":
                            print("\nYet to be implemented.")
                        elif main_menu_option == "4":
                            flag_layer_2 = False
                            print("\nBack to the Welcome menu...")
                        elif main_menu_option == "5":
                            self.save_list_of_applications()
                            self.save_list_of_wishlists()
                            flag_layer_1 = False
                            flag_layer_2 = False
                            obj_ui.exit_logo()
                    elif not login[0]:
                        flag_layer_2 = False
                        print("\nBack to the Welcome menu...")

            elif welcome_option == "2":
                print("\nYet to be implemented.")
                input("Press any keys to go back...")
            elif welcome_option == "3":
                self.save_list_of_applications()
                self.save_list_of_wishlists()
                flag_layer_1 = False
                obj_ui.exit_logo()

    def save_list_of_applications(self):
        """
        A method to save the list of rental applications

        :return: None
        """
        data = {"application_details": []}
        for application in self.__list_of_applications:
            data["application_details"].append({"first_name": application.get_first_name(),
                                                "last_name": application.get_last_name(),
                                                "email": application.get_email(),
                                                "mobile_phone": application.get_mobile_phone(),
                                                "saving": application.get_saving(),
                                                "property_address": application.get_property_address()})
        with open("./data/application.txt", 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data, indent=4))

    def save_list_of_wishlists(self):
        """
        A method to save the list of wishlists

        :return: None
        """
        wishlist_data = {"wishlist_details": []}
        for wishlist in self.__list_of_wishlists:
            wishlist_data["wishlist_details"].append(
                {"tenant_email": wishlist.get_tenant_email(), "property_details": wishlist.get_property_details()}
            )
        with open("./data/wishlist.txt", 'w', encoding='UTF-8') as file:
            file.write(json.dumps(wishlist_data, indent=4))

    def set_list_of_applications(self, list_of_applications):
        """
        Mutator method to update list of applications

        :param list_of_applications: new list of rental applications

        :return: None
        """
        self.__list_of_applications = list_of_applications

    def set_list_of_properties(self, list_of_properties):
        """
        Mutator method to update list of all properties

        :param list_of_properties: a new list of properties

        :return: None
        """
        self.__list_of_properties = list_of_properties

    def set_list_of_tenants(self, list_of_tenants):
        """
        Mutator method to update list of all tenants

        :param list_of_tenants: a new list of tenants

        :return: None
        """
        self.__list_of_tenants = list_of_tenants

    def set_list_of_wishlists(self, list_of_wishlists):
        """
        Mutator method to update list of wishlist

        :param list_of_wishlists: new list of wishlist

        :return: None
        """
        self.__list_of_wishlists = list_of_wishlists

    def set_utility(self, utility):
        """
        Mutator method to update utility object

        :param utility: new utility object

        :return: None
        """
        self.__utility = utility


if __name__ == '__main__':
    obj_run = MonashRentalSpace()
    obj_run.run()
