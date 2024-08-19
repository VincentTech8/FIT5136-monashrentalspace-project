class Utility:

    def __init__(self, tenant_preference="", weekly_income=-1):
        """
        This method initialises the attributes of the utility class

        :param tenant_preference: String - preference of tenant as to how the recommended optimal price is to be displayed
        :param weekly_income: int - weekly income of tenant
        """
        self.__tenant_preference = tenant_preference
        self.__weekly_income = weekly_income

    def get_tenant_preference(self):
        """
        Accessor method to retrieve tenant preference

        :return: String - tenant's preference
        """
        return self.__tenant_preference

    def get_weekly_income(self):
        """
        Accessor method to retrieve the tenant's weekly income

        :return: int - the tenant's weekly income
        """
        return self.__weekly_income

    def set_tenant_preference(self, tenant_preference):
        """
        The mutator method to update the tenant's preference

        :param tenant_preference: String - tenant's preference

        :return: None
        """
        self.__tenant_preference = tenant_preference

    def set_weekly_income(self, weekly_income):
        """
        The mutator method to update the tenant's weekly income

        :param weekly_income: int - new weekly income

        :return: None
        """
        self.__weekly_income = weekly_income

    def __str__(self):
        """
        A method to display the tenant's preference and weekly income as a string

        :return: A string containing utility details
        """
        return f"Tenant Preference: {self.__tenant_preference}, Weekly Income: {self.__weekly_income}"
