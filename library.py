class Library:
    def __init__(self, index, signup_days, books_per_day):
        self.books = dict()
        self.index = index
        self.signup_days = signup_days
        self.books_per_day = books_per_day

    def add_book(self, index, score):
        self.books[index] = score
