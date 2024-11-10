

### booklover.py

import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})

    # Method 1
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [book_rating]
        })
        if self.book_list.empty:
            self.book_list['book_name'] = pd.Series(dtype='object')  

        if self.book_list[self.book_list['book_name'].str.contains(book_name, na=False)].empty:
            if 0 <= book_rating <= 5:
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            else:
                print('Please enter a rating from 0-5')
        else:
            print(f'{book_name} has already been added to this list')

    # Method 2
    def has_read(self, book_name):
        if self.book_list['book_name'].dtype != 'object':
            self.book_list['book_name'] = self.book_list['book_name'].astype(str)

        return not self.book_list[self.book_list['book_name'].str.contains(book_name, na=False)].empty
    # Method 3    
    def num_books_read(self):
        return len(self.book_list)

    # Method 4
    def fav_books(self):
        fav_book_count = self.book_list['book_rating'].apply(lambda x: x > 3).sum()
        return fav_book_count

    # Method 5
    def print_book_list(self):
        return self.book_list
    
################################################################################


