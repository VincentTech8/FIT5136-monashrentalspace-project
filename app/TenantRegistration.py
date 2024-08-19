from Tenant import *


class TenantRegistration(Tenant):
    def __init__(self, first_name="", last_name="", email="", mobile_phone="", password="", gender="",
                 preferred_renting_cost=-1, preferred_suburb=""):
        """
        This method to initialise the attributes of the TenantRegistration class

        :param first_name: String - Tenant's first name
        :param last_name: String - Tenant's last name
        :param email: String - Tenant's email id
        :param mobile_phone: String - Tenant's mobile number
        :param password: String - Tenant's password
        :param gender: String - Tenant's gender
        :param preferred_renting_cost: Int - Tenant's preferred renting cost
        :param preferred_suburb: String - Tenant's preferred suburb
        """
        super().__init__(first_name, last_name, email, mobile_phone)
        self.__password = password
        self.__gender = gender
        self.__preferred_renting_cost = preferred_renting_cost
        self.__preferred_suburb = preferred_suburb

    def get_gender(self):
        """
         Accessor method to retrieve the tenant's gender

        :return: String - Tenant's gender
        """
        return self.__gender

    def get_password(self):
        """
        Accessor method to retrieve the tenant's password

        :return: String - Tenant's password
        """
        return self.__password

    def get_preferred_renting_cost(self):
        """
        Accessor method to retrieve the tenant's preferred renting cost

        :return: Int - Tenant's preferred renting cost
        """
        return self.__preferred_renting_cost

    def get_preferred_suburb(self):
        """
        Accessor method to retrieve the tenant's preferred suburb

        :return: String - Tenant's preferred suburb
        """
        return self.__preferred_suburb

    def set_gender(self, gender):
        """
        Mutator method to update tenant's gender

        :param gender: String - Tenant's gender

        :return: None
        """
        self.__gender = gender

    def set_password(self, password):
        """
        Mutator method to update tenant's password

        :param password: String - Tenant's password

        :return: None
        """
        self.__password = password

    def set_preferred_renting_cost(self, preferred_renting_cost):
        """
        Mutator method to update tenant's preferred renting cost

        :param preferred_renting_cost: Int - Tenant's preferred renting cost

        :return: None
        """
        self.__preferred_renting_cost = preferred_renting_cost

    def set_preferred_suburb(self, preferred_suburb):
        """
        Mutator method to update tenant's preferred suburb

        :param preferred_suburb: String - Tenant's preferred suburb

        :return: None
        """
        self.__preferred_suburb = preferred_suburb

    def __str__(self):
        """
        A method to display the tenant's registration details

        :return: String containing tenant's registration details
        """
        return f"{super().__str__()}, Password: {self.__password}, Gender: {self.__gender}, Preferred Renting Cost:" \
               f"{self.__preferred_renting_cost}, Preferred Suburb: {self.__preferred_suburb}"
