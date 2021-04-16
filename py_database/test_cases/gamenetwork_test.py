#Matthew Ivezaj

#Import unittest Library.
import unittest
#Import all methods from InventoryItem in the classes folder.
from classes.inventory_class import Inventory
class TestInventoryClass(unittest.TestCase):
    """
    TestCase unittest testing for 
    the TestInventoryrClass Class.
    Running the following tests: 
    assertTrue/assertFalse 
    """
    def setUp(self):
        """
        Create an instance of the Inventory class for testing all class methods.
        """
        #Creating an instance of the Validation class and adding a list.
        self.my_inventory = Inventory()
#itemname, itemprice, itemquantity, shelflife, itemcolor, itembrand", "location

    def test_invalid_item_name(self):
        """
        Test to see if address is not valid
        Tests Ran: assertFalse
        assertFalse - Checks to see whether the 
        item name passed will be contains characters that are not normally allowed,

        Such as the following:
        ! " ' @ $ % ^ & * _  = + < >  ? ; [ ] { }, if it does, return true.
        """
        #Creating a list of bad addresses
        bad_names = ["!Wrench","Wrench#","!Wrench#","$Wre#nch*","d^nut","!Donut","DONUT&"]
        #Checkings for each string in the list.
        for name in bad_names:
            #Evaluating each string.
            self.assertFalse(self.my_inventory.item_name_check(name))
    def test_valid_address_check(self):
        """
        Test to see if the address is valid
        Tests Ran: assertTrue
        assertTrue - Checks to see if The item name 
        is comprised primarily of alphanumeric characters,
        but must not contain any of the following characters: 
        ! " ' @ $ % ^ & * _  = + < >  ? ; [ ] { }
        """
        #Creating a list of good addresses
        good_names = ["Wrench","WrencH","wRenCh","WrEncH","donut","Donut","DONUT"]
        #Checkings for each string in the list.
        for name in good_names:
            #Evaluating each string.
            self.assertTrue(self.my_inventory.item_name_check(name))
    def test_invalid_price_check(self):
        """
        Test to see if the city name is invalid.
        Tests Ran: 
        assertFalse - Checks to see if the city name is not 
        in the city bad name. Tests the city names in bad_city_information 
        list as a list of bad names to see if it contains characters that are not normally allowed.
        """
        #Creating a list of bad city info.
        bad_item_price = ["a1.b22g","a1.22","1.22a","fasdfdas","1@31","!2.31","232.21%",".3123!",".$3123!",".^3123",".*&(*&!",".sdfds","fdsds.$@*#^&*"]
        #Checkings for each string in the list.
        for price in bad_item_price:
            #Evaluating each string.
            self.assertFalse(self.my_inventory.price_check(price)) 
    def test_valid_price_check(self):
        """
        Test to see if the item price is valid.
        Tests Ran: 
        assertTrue - Checks to see if the prices that is comprised of anything so it can be validated.
        Tests the prices in good_price_information list as a list of potential good prices.
        """
        #Creating a list of good city info to use in test
        good_price_information = ["1.21'","5453","342.32",".432","3.2","54.54"]
        #Checkings for each string in the list.
        for price in good_price_information:
            #Evaluating each string.
            self.assertTrue(self.my_inventory.price_check(price)) 
    def test_invalid_item_quantity_check(self):
        """
        Test to see if the quantity_heck is invalid.
        Test ran: assertTrue.
        assertFalse - Checks to see if the value is in the 
        invalid_invalid_company_name_check_list, contains characters that are not normally allowed.
        """
        #Creating a list of bad company to use in test
        invalid_quantity_list = [" ","  ","   ","    ","     ", "      ","       ","        "]
        #Calling company_name_check and passing home in the arguments
        for quantity in invalid_quantity_list:
            self.assertFalse(self.my_inventory.quantity_check(quantity.strip()))
    def test_valid_item_quantity_check(self): 
        """
        Test to see if the quantity_check is valid.
        Test ran: assertFalse.
        assertTrue - Checks to see if the value is in the valid_quantity_list,
        assertTrue returns true if it is.
        """
        valid_quantity_list = ["1","2","3","4","5","6","7","8"]
        #Calling company_name_check and passing home in the arguments
        for quantity in valid_quantity_list:
            #Evaluating the company name method.
            self.assertTrue(self.my_inventory.quantity_check(quantity))
    def test_invalid_shelf_life_check(self):
        """
        Test to see if the shelf life is invalid.
        Test ran: assertTrue - Checks to see that the shelf life
        only contains digits in days.
        """
        #Creating a list of valid names to test.
        invalid_names_list = ["1a","a1","a","453z","a321","jflsadk","342@","$54","&#@%(*$#","shdfjkhGJH$@*#&^",""," "]
        #Looping through each name in the list.
        for name in invalid_names_list:
            #Evaluating the inventory shelf life method.
            self.assertFalse(self.my_inventory.shelf_life_check(name))
    def test_valid_shelf_life_check(self):
        """
        Test to see if the inventory shelf life is valid.
        Test ran: assertTrue - Checks to see that the shelf life
        only contains ints.
        """
        #Creating a list of valid names to test.
        valid_names_list = ["1","324","32","'5645","34534","234234","01010101","143202134798423","111111111111111111111111111111"]
        #Looping through each name in the list.
        for name in valid_names_list:
            #Evaluating the inventory shelf life method.
            self.assertTrue(self.my_inventory.shelf_life_check(name))
################################NEED TO FIX TESTS BELOW THIS LINE################################
    def test_invalid_email(self): 
        """
        Test to see if the customer email is invalid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        email list or contains characters that are not normally allowed.
        """
        #Creating a list of bad emails to test.
        invalid_email_list= ["!mary123@mail.com","!mary12@#$3@()$#*&mail.com%","!mary123@mail.com%","mary123@mail.com#","mary123mailcom#","MARY!MAILCOM","#mary123mailcom!","mary!mailcom","mary!gmail.com","$mary123mailcom","^&^*&#!@",""," "]
        #Calling retail_price_check and passing home in the arguments
        for email in invalid_email_list:
            #Evaluating each email in the list.
            self.assertFalse(self.my_customer.email_check(email))
    def test_valid_email(self): 
        """
        Test to see if the customer email is valid.
        Test ran: assertFalse.
        assertTrue - Checks to see if the value is in the customer 
        email list, assertTrue returns true if it is.
        """
        #Creating a list of good emails to test.
        valid_email_list= ["mary123mail.com","mary123mail.com","marymail.com","a","i3@","3@3.com","a@","a.",".d","@d","marymailcom","1marymailcom4","4marymailcom","marymailcom6","marrymailcom","marymail","sally73@gmail.com","SALLY73@GMAIL.COM","4marymailr3242com3","9324759872395734","mary123@mail.com"]
        #Calling retail_price_check and passing home in the arguments
        for email in valid_email_list:
            #Evaluating each email in the list.
            self.assertTrue(self.my_customer.email_check(email))
    def test_invalid_phone_check(self): 
        """
        Test to see if the customer phone number is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the 
        invalid_phone_check list checks to see if it 
        contains characters that are not normally allowed.
        """
        #Creating a list of bad phone numbers to test.
        invalid_phone_check = ["212.599.6363","!2125996363","2125996363!","Tom! Petz*","##Cindy##","a2259a","aaa.bbb.cccc","&$#(&@*(&#$@&(#@*","","jkahdfjhsafkdh","&*#-#&$-#$&*"," ",'&@#($&#42343&($!#(2432&*#(@$$*',"423342432a)","f231213321","d1232(1323h","*123231231","231231213$","^231a23132","g32132123&"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in invalid_phone_check:
            #Evaluating each phone number in the list.
            self.assertFalse(self.my_customer.phone_number_check(phone))
    def test_valid_phone_check(self): 
        """
        Test to see if the customer phone number is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the 
        valid_phone_check list, assertTrue returns true if it is.
        """
        #Creating a list of good numbers
        valid_phone_check = ["212-599-6363","212-599-6363","1234567890","123-123-1234","1111111111","-1111111111-","-1112223334-","1231233212--","--1231233212","222-222-2222","7777777777"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in valid_phone_check:
            #Evaluating the phone numbers
            self.assertTrue(self.my_customer.phone_number_check(phone))
    def test_invalid_state_check(self): 
        """
        Test to see if the customer state is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        state list, assertFalse checks to see if it contains characters that are not normally allowed.
        """
        #Creating a list of bad state checks.
        invalid_state_list= ["M1","dahs","ASG","A","1M","11","!M","m1","A&","1m","!!","!M","M!","","  "," "," M","I "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.state_information_check(state))
    def test_valid_state_check(self): 
        """
        Test to see if the customer state is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the customer 
        state list, assertTrue returns true if it is.
        """
        #Creating a list of good state values.
        invalid_state_list= ["MI","mi","aZ","Az","fw"]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.state_information_check(state))
    def test_invalid_zip_code_check(self): 
        """
        Test to see if the customer zip code is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        state list, assertFalse checks to see if it contains characters that are not normally allowed..
        """
        #Creating a list of bad zip code values to test.
        invalid_state_list= ["123m","!423d","12m3","12345678","!123","123!","12!3","123","0","12","as","!","a","wq","as2d","asfd","asfdd","@#","$@#","$#@@","j#@a","j23i","2sd@","@df4","asd1",""," "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.zip_code_check(state))
    def test_valid_zip_code_check(self): 
        """
        Test to see if the customer zip code is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the customer 
        zip code list, assertTrue returns true if it is.
        """
        #Creating a list of good values to test.
        valid_zip_code_list= ["1234","4321","12345","1111","11111","1112","2111","2112","21112","31115","21314"]
        #Calling retail_price_check and passing home in the arguments
        for zip_code in valid_zip_code_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.zip_code_check(zip_code))
