class Tenant:

    def __init__(self, first_name="", last_name="", email="", mobile_phone=""):
        """
        A method to initialise the attributes of the tenant class

        :param first_name: String - tenant's first name
        :param last_name: String - tenant's last name
        :param email: String - tenant's email id
        :param mobile_phone: String - tenant's phone number
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__mobile_phone = mobile_phone

    def get_email(self):
        """
        Accessor method to get the tenant's email id

        :return: String - tenant's email id
        """
        return self.__email

    def get_first_name(self):
        """
        Accessor method to retrieve the tenant's first name

        :return: String - tenant's first name
        """
        return self.__first_name

    def get_last_name(self):
        """
        Accessor method to retrieve the tenant's last name

        :return:  String - tenant's last name
        """
        return self.__last_name

    def get_mobile_phone(self):
        """
        Accessor method to retrieve the tenant's mobile number

        :return: String - tenant's phone number
        """
        return self.__mobile_phone

    def set_email(self, email):
        """
        Mutator method to update the tenant's email id

        :param email: String - tenant's email id

        :return: None
        """
        self.__email = email

    def set_first_name(self, first_name):
        """
        Mutator method to update the tenant's first name

        :param first_name: String - tenant's first name

        :return: None
        """
        self.__first_name = first_name

    def set_last_name(self, last_name):
        """
        Mutator method to update the tenant's last name

        :param last_name: String - tenant's last name

        :return: None
        """
        self.__last_name = last_name

    def set_mobile_phone(self, mobile_phone):
        """
        Mutator method to update the tenant's phone number

        :param mobile_phone: String - tenant's phone number

        :return: None
        """
        self.__mobile_phone = mobile_phone

    def __str__(self):
        """
        A method to display the Tenant details

        :return: A string containing all the tenant details
        """
        return f"First Name: {self.__first_name}, Last Name: {self.__last_name}, " \
               f"Email: {self.__email}, Mobile Phone: {self.__mobile_phone}"
