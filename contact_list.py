class ContactList():
    
# store contacts as a list of dictionaries (name and phone number)
# keep list sorted by contact's name

# handle multiple contact lists
    all_contact_lists = {}

    def __init__(self, list_name, contact_list):
        self.list_name = list_name
        self.contact_list = contact_list
        self.sort_contacts()
        ContactList.all_contact_lists[self.list_name] = self.contact_list

    def __str__(self):
        return f'{self.contact_list}'

    # add contact to list and re-sort list
    def add_contact(self, new_contact):
        self.contact_list.append(new_contact)
        self.sort_contacts()

    # remove contact from a list by name
    def remove_contact(self, name):
        for index in range(len(self.contact_list)):
            if name == self.contact_list[index]['name']:
                del self.contact_list[index]
    
    def sort_contacts(self):
        self.contact_list = sorted(self.contact_list, key=lambda x : x['name'])
        pass
    
    # accept another contact list as ARG and return a new list of dicts indicating contacts that are shared
    def find_shared_contacts(self, ContactList):
        temp_list = []
        for contact_a in self.contact_list:
            for contact_b in ContactList.contact_list:
                if contact_a == contact_b:
                    temp_list.append(contact_a)
        return temp_list
        

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)

#print(friends_i_work_with)

# print(my_friends_list)
my_work_buddies.add_contact({'name':'Billy', 'number':'111-2222'})
# print(my_friends_list)
# my_friends_list.remove_contact('carol')
# print(my_friends_list)

# print(my_work_buddies.list_name)
# print(ContactList.all_contact_lists)

print(ContactList.all_contact_lists)