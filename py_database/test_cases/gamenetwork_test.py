#Matthew Ivezaj

#Import unittest Library.
import unittest
#Import all methods from InventoryItem in the classes folder.
from classes.inventory_class import Inventory
class TestGameNetworkClass(unittest.TestCase):
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

    def test_invalid_check_stats(self):
        """
            T
        """
