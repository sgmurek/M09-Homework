### booklover_test.py 

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def setUp(self):
        self.booklover1 = BookLover('Shawn G', 'wsr7qr@virginia.edu', 'Thriller')
        self.booklover2 = BookLover('James G', 'xxxxxx@virginia.edu', 'Romance')
        self.booklover3 = BookLover('Sarah P', 'XXXXXX@virginia.edu', 'History')

    def test_1_add_book(self): 
        self.booklover1.add_book('The Hobbit', 4)
        self.assertTrue(self.booklover1.has_read('The Hobbit'))

    def test_2_add_book(self):
        self.booklover1.add_book('The Hobbit', 3)
        self.assertEqual(self.booklover1.print_book_list()['book_name'].str.count('The Hobbit').sum(), 1)

    def test_3_has_read(self): 
        self.booklover1.add_book('The Hobbit', 4)
        self.assertTrue(self.booklover1.has_read('The Hobbit'))

    def test_4_has_read(self): 
        self.assertFalse(self.booklover1.has_read('It'))

    def test_5_num_books_read(self): 
        self.booklover1.add_book('The Hobbit', 4)
        self.booklover1.add_book('The Fellowship of the Ring', 5)
        self.booklover1.add_book('The Two Towers', 3)
        self.assertEqual(self.booklover1.num_books_read(), 3)

    def test_6_fav_books(self):
        self.booklover3.add_book('History of the Ancient World', 5)
        self.booklover3.add_book('Sapiens', 5)
        self.booklover3.add_book('How to Hide an Empire', 4)
        self.booklover3.add_book('Twilight', 2)
        self.booklover3.add_book('Harry Potter', 3)
        self.assertEqual(self.booklover3.fav_books(), 3)

if __name__ == '__main__':
    unittest.main(verbosity=3)

################################################################################


