from datetime import datetime


class Wishlist:
    def __init__(self, tenant_email="", property_details=[]):
        """
        A method to initialise the attributes of the Wishlist class

        :param tenant_email: String - Tenant's email id
        :param property_details: List of property details
        """
        self.__tenant_email = tenant_email
        self.__property_details = property_details

    def add_to_wishlist(self, property_address):
        """
        A method to add property to tenant's wishlist

        :param property_address: String - new property address to be added to wishlist

        :return: None
        """
        is_match = False
        for each_property in self.__property_details:
            if each_property["property_address"] == property_address:
                is_match = True

        if is_match == False:
            self.__property_details.append(
                {"property_address": property_address, "added_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
            print("\nProperty has been added to wishlist!")
        else:
            print("\nProperty already in the wishlist!")

    def display_wishlist_properties(self):
        """
        A method to display wishlisted properties

        :return: A list of wishlisted properties
        """
        list_of_prop = ""
        for each_property in self.__property_details:
            list_of_prop += each_property["property_address"] + "\n"
        return list_of_prop

    def get_property_address(self):
        """
        A method to get the list of property addresses

        :return: list of property addresses
        """
        list_of_prop = []
        for each_property in self.__property_details:
            list_of_prop.append(each_property["property_address"])
        return list_of_prop

    def get_property_details(self):
        """
        Accessor method to retrieve the list of property details

        :return: list of property details
        """
        return self.__property_details

    def get_tenant_email(self):
        """
        Accessor method to retrieve tenant's email id

        :return: String - tenant's email id
        """
        return self.__tenant_email

    def remove_from_wishlist(self, property_address):
        """
        A method to remove a property from tenant's wishlist

        :param property_address: Property address that is to be removed from wishlist

        :return: None
        """
        new_property_details = [each_property for each_property in self.__property_details if
                                each_property["property_address"] != property_address]
        if len(new_property_details) != len(self.__property_details):
            print("\nProperty has been removed from wishlist!")
            self.__property_details = new_property_details
        else:
            print("\nProperty not found in the wishlist!")

    def set_property_details(self, property_details):
        """
        Mutator method to update the property details

        :param property_details: new property details

        :return: None
        """
        self.__property_details = property_details

    def set_tenant_email(self, tenant_email):
        """
        Mutator method to update the tenant's email

        :param tenant_email: Tenant's new email id

        :return: None
        """
        self.__tenant_email = tenant_email
    
    def __str__(self):
        """
        A method to display the details of the tenant's wishlist

        :return: String containing details of tenant's wishlist
        """
        return f"Tenant Email: {self.__tenant_email}, Property List: {self.__property_details}"
