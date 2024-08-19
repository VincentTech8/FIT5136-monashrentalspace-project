class Property:
    def __init__(self, property_address="", property_suburb="", property_price=-1, property_condition="",
                 property_type="", property_state="", property_description="", property_agent="",
                 property_management_contact_number="", property_application_url="",
                 property_inspection_date_time="", property_listed_date=""):
        """
        This method initialises the attributes of the Property class

        :param property_address: address of the property
        :param property_suburb: suburb of the property
        :param property_price: price of the property
        :param property_condition: condition of property
        :param property_type: type of property
        :param property_state: state of property
        :param property_description: description of property
        :param property_agent: agent of property
        :param property_management_contact_number: contact number of property management
        :param property_application_url: application url for a property
        :param property_inspection_date_time: a property inspection date and time
        :param property_listed_date: the listed date of a property
        """
        self.__property_address = property_address
        self.__property_suburb = property_suburb
        self.__property_price = property_price
        self.__property_condition = property_condition
        self.__property_type = property_type
        self.__property_state = property_state
        self.__property_description = property_description
        self.__property_agent = property_agent
        self.__property_management_contact_number = property_management_contact_number
        self.__property_application_url = property_application_url
        self.__property_inspection_date_time = property_inspection_date_time
        self.__property_listed_date = property_listed_date

    def display_property_details(self):
        """
        A method to display property details

        :return: None
        """
        to_print = f"\nAddress: {self.__property_address}\nSuburb: {self.__property_suburb}\nPrice: " \
                   f"{self.__property_price}\nCondition: {self.__property_condition}\nType: " \
                   f"{self.__property_type}\nState: {self.__property_state}\nDescription: " \
                   f"{self.__property_description}\nAgent: {self.__property_agent}\n" \
                   f"Management Contact Number: {self.__property_management_contact_number}\n" \
                   f"Application URL: {self.__property_application_url}\n" \
                   f"Inspection Date and Time: {self.__property_inspection_date_time}\n"

        print(to_print)

    def get_property_address(self):
        """
        Accessor method to retrieve property address

        :return: String - address of property
        """
        return self.__property_address

    def get_property_agent(self):
        """
        Accessor method to retrieve property agent

        :return: String - agent in-charge of property
        """
        return self.__property_agent

    def get_property_application_url(self):
        """
        Accessor method to retrieve application url for the property

        :return: String - application URL for the property
        """
        return self.__property_application_url

    def get_property_condition(self):
        """
        Accessor method to retrieve property condition

        :return: String - property condition
        """
        return self.__property_condition

    def get_property_description(self):
        """
        Accessor method to retrieve property description

        :return: String - description of property
        """
        return self.__property_description

    def get_property_inspection_date_time(self):
        """
        Accessor method to retrieve the inspection date & time for the property

        :return: String - Inspection date and time for property
        """
        return self.__property_inspection_date_time

    def get_property_listed_date(self):
        """
        Accessor method to retrieve the listed date of a property

        :return: String - Listed date of a property
        """
        return self.__property_listed_date

    def get_property_management_contact_number(self):
        """
        Accessor method to retrieve contact number of the property management

        :return: String - contact number of the property management
        """
        return self.__property_management_contact_number

    def get_property_price(self):
        """
        Accessor method to retrieve price of property

        :return: String - price of property
        """
        return self.__property_price

    def get_property_state(self):
        """
        Accessor method to retrieve state of property

        :return: String - state of property
        """
        return self.__property_state

    def get_property_suburb(self):
        """
        Accessor method to retrieve the suburb of the property

        :return: String - suburb of property
        """
        return self.__property_suburb

    def get_property_type(self):
        """
        Accessor method to retrieve type of property

        :return: String - type of property
        """
        return self.__property_type

    def set_property_address(self, property_address):
        """
        Mutator method to update teh address of property

        :param property_address: String - new address of the property

        :return: None
        """
        self.__property_address = property_address

    def set_property_agent(self, property_agent):
        """
        Mutator method to update the agent managing the property

        :param property_agent: String - new agent name

        :return: None
        """
        self.__property_agent = property_agent

    def set_property_application_url(self, property_application_url):
        """
        Mutator method to update the application URL for property

        :param property_application_url: String - new application URL

        :return: None
        """
        self.__property_application_url = property_application_url

    def set_property_condition(self, property_condition):
        """
        Mutator method to update the condition of the property

        :param property_condition: String - new/current property condition

        :return: None
        """
        self.__property_condition = property_condition

    def set_property_description(self, property_description):
        """
        Mutator method to update the description of the property

        :param property_description: String - new property description

        :return: None
        """
        self.__property_description = property_description

    def set_property_inspection_date_time(self, property_inspection_date_time):
        """
        Mutator method to update the property's inspection date and time

        :param property_inspection_date_time: String - new date and time

        :return: None
        """
        self.__property_inspection_date_time = property_inspection_date_time

    def set_property_management_contact_number(self, property_management_contact_number):
        """
        Mutator method to update the property management's contact number

        :param property_management_contact_number: String - new contact number

        :return: None
        """
        self.__property_management_contact_number = property_management_contact_number

    def set_property_price(self, property_price):
        """
        Mutator method to update price of the property

        :param property_price: String - new property price

        :return: None
        """
        self.__property_price = property_price

    def set_property_state(self, property_state):
        """
        Mutator method to update the property status

        :param property_state: String - new property status

        :return: None
        """
        self.__property_state = property_state

    def set_property_suburb(self, property_suburb):
        """
        Mutator method to update the suburb of the property

        :param property_suburb: String - new suburb

        :return: None
        """
        self.__property_suburb = property_suburb

    def set_property_type(self, property_type):
        """
        Mutator method to update the type of property

        :param property_type: String - new property type

        :return: None
        """
        self.__property_type = property_type

    def __str__(self):
        """
        A method to display all the property details as a String

        :return: String containing the property details
        """
        return f"Property address: {self.__property_address}, Property suburb: {self.__property_suburb}, " \
               f"Property price: {self.__property_price}, Property condition: {self.__property_condition}, " \
               f"Property type: {self.__property_type}, Property state: {self.__property_state}, " \
               f"Property description: {self.__property_description}, Property agent: {self.__property_agent}, " \
               f"Property Management Contact Number: {self.__property_management_contact_number}, " \
               f"Property Application URL: {self.__property_application_url}, " \
               f"Property Inspection Date and Time: {self.__property_inspection_date_time}, " \
               f"Property Listed Date: {self.__property_listed_date}"
