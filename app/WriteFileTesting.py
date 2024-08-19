import json


temp = dict()

temp["creature"] = "human"

"""with open("test.txt", 'w') as file:
    json.dump(temp,file,indent=4)"""

with open("./data/tenant.txt", 'r') as file:
    temp2 = file.read()
    temp1 = json.loads(temp2)

temp3 = temp1.get("tenant_details")
print(type(temp3[0]))
print(type(temp3[0].get("mobile_phone")))


"""
def get_property_objects(self, data_path):
    temp = []

    with open(data_path, 'r') as f:
        file = f.read()
        file2 = json.loads(file)
        item_details = file2.get("property_details")
        for item in item_details:
            p1 = Property(item["property_address"], item["property_suburb"])
            temp.append(p1)

    return temp"""
"""
def display_on_search(self):
    #print all the fields required on search the property

def display_details(self):
    #print all the fields when a specific property is created

#then we can use for loop or for each in the list_of_properties

self.set_list_of_properties = self.get_property_objects(data_path)
for property in self.list_of_properties:
    property.display_on_search
    
# or upon selected view
self.list_of_properties[index].display_details"""


"""def get_property(self):
    temp = []
    with open(data_path, 'r') as f:
        file = f.read()
        file2 = json.loads(file)
        item_details = file2.get("property_details")
        for item in item_details:
            p1 = Property(item["property_address"], item["property_suburb"], item["property_price"],
                          item["property_condition"], item["property_type"], item["property_status"],
                          item["property_description"], item["property_agent"],
                          item["property_management_contact_number"], item["property_application_url"],
                          item["property_inspection_date_time"])
            temp.append(p1)

        print(temp)
        for l1 in temp:
            print(l1.__str__())"""


"""
    def __int__(self, option):
        self.option = option

    def is_valid_input(option):
        if option in ["1", "2", "3"]:
            return True"""