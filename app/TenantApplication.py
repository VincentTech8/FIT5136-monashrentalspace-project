from Tenant import *


class TenantApplication(Tenant):
    def __init__(self, first_name="", last_name="", email="", mobile_phone="", employment_status="",
                 hours_of_work=-1, proof_of_income="", other_supporting_documents=[], saving=-1, property_address=""):
        """
        This method is to initialize all the attributes of the TenantApplication class

        :param first_name: String - tenant's first name
        :param last_name: String - tenant's last name
        :param email: String - tenant's email id
        :param mobile_phone: String - tenant's phone number
        :param employment_status: String - tenant's employment status
        :param hours_of_work: int - tenant's work hours
        :param proof_of_income: String - tenant's proof of income
        :param other_supporting_documents: List - a list of other supporting documents
        :param saving: int - tenant's saving
        :param property_address: String - tenant's applied property address
        """
        super().__init__(first_name, last_name, email, mobile_phone)
        self.__employment_status = employment_status
        self.__hours_of_work = hours_of_work
        self.__proof_of_income = proof_of_income
        self.__other_supporting_documents = other_supporting_documents
        self.__saving = saving
        self.__property_address = property_address

    def get_employment_status(self):
        """
        Accessor method to retrieve the tenant's employment status

        :return: String - tenant's employment status
        """
        return self.__employment_status

    def get_hours_of_work(self):
        """
        Accessor method to retrieve tenant's work hours

        :return: int - tenant's work hours
        """
        return self.__hours_of_work

    def get_other_supporting_documents(self):
        """
        Accessor method to retrieve the tenant's supporting documents

        :return: List - a list of tenant's supporting documents
        """
        return self.__other_supporting_documents

    def get_proof_of_income(self):
        """
        Accessor method to retrieve the tenant's proof of income

        :return: String - tenant's proof of income
        """
        return self.__proof_of_income

    def get_property_address(self):
        """
        Accessor method to retrieve the tenant's applied property address

        :return: String - tenant's applied property address
        """
        return self.__property_address

    def get_saving(self):
        """
        Accessor method to retrieve the tenant's saving

        :return: int - tenant's saving
        """
        return self.__saving

    def set_employment_status(self, employment_status):
        """
        Mutator method to update the tenant's employment status

        :param employment_status: String - tenant's employment status

        :return: None
        """
        self.__employment_status = employment_status

    def set_hours_of_work(self, hours_of_work):
        """
        Mutator method to update the tenant's work hours

        :param hours_of_work: int - tenant's work hours

        :return:  None
        """
        self.__hours_of_work = hours_of_work

    def set_other_supporting_documents(self, other_supporting_documents):
        """
        Mutator method to update the tenant's supporting documents

        :param other_supporting_documents: A list of the tenant's supporting documents

        :return: None
        """
        self.__other_supporting_documents = other_supporting_documents

    def set_proof_of_income(self, proof_of_income):
        """
        Mutator method to update the tenant's proof of income

        :param proof_of_income: String - tenant's proof of income

        :return: None
        """
        self.__proof_of_income = proof_of_income

    def set_property_address(self, property_address):
        """
        Mutator method to update the tenant's applied property address

        :param property_address: String - tenant's applied property address

        :return: None
        """
        self.__property_address = property_address

    def set_saving(self, saving):
        """
        Mutator method to update the tenant's saving

        :param saving: int - tenant's saving

        :return: None
        """
        self.__saving = saving

    def __str__(self):
        """
        A method to display the tenant's application details

        :return: A String containing the tenant's application details
        """
        return f"{super().__str__()}, Employment Status: {self.__employment_status}, Hours of Work: " \
               f"{self.__hours_of_work}, Proof of Income: {self.__proof_of_income}, Other Supporting Documents:" \
               f" {self.__other_supporting_documents}, Applied Property Address: {self.__property_address}"
