class Contact:
    """
    class generates new instances of contacts
    
    """
    all_contacts = []

    def __init__(self,first_name,last_name,phone_number,email):
        """
        init method helps  define properties for our objects

        Args:
        first_name: new contact first name
        last_name: new contact last name
        number: new contact phone number

        """

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save(self):
        self.all_contacts.append(self)