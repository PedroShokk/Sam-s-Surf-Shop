# Write your code below:
import surfshop
import unittest 

class SurfshopTest(unittest.TestCase):
    pass

    def setUp(self):
      self.cart = surfshop.ShoppingCart()

    def test_add_surfboards_1(self):
      self.assertEqual(self.cart.add_surfboards(1), f'Successfully added 1 surfboard to cart!' )


    def test_add_surfboards_2(self):
      for i in range(2,5):
        with self.subTest(i=i):
          self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
          self.cart = surfshop.ShoppingCart()

    #@unittest.skip
    def test_shoppingCart_Size(self):
      self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    #@unittest.expectedFailure
    def test_apply_locals_discount(self):
      self.cart.apply_locals_discount()
      self.assertTrue(self.cart.locals_discount)






    
unittest.main()