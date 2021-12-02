import unittest #imports unitest module
from contact import Contact

class TestContact(unittest.TestCase):
    """
    test class that defines testcases for the contact class behaviours

    Args:
    unittest.TestCase:test case class that helps in creating test cases

    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_contact = Contact('Faith','Muthoni','0700123123','faith@gmail.com')

    def tearDown(self):
           """
           teardown method that doesn clean up after test case has run
           
           """
           Contact.contact_list = []
    
    def test__init__(self):
        """
        Test init test case to test if the object is initialized Properly
        """

        self.assertEqual(self.new_contact.first_name,'Faith')
        self.assertEqual(self.new_contact.last_name,'Faith')
        self.assertEqual(self.new_contact.phone_number,'0700123123')
        self.assertEqual(self.new_contact.email,'faith@gmail.com')
    
    def test_save_contact(self):
        """
        test_save_contact test case to test if the contact object is save in the contact list
    
        """

        self.new_contact_save()
        self.assertEqual(len(Contact.all_contacts),1)

    def test_save_multiple_contact(self):
        """
        test_save_multiple_contact test case to test if we can save nultiple  contact object in the cont list
        """
        pass


    def test_display_all_contacts(self):
        pass

    if __name__ == '__main__':
        unittest.main()
        

