from library import Library
import pprint
import sys

def input_parser(filename):
    with open(filename, "r") as myfile:
        line1 = myfile.readline()
        line2 = myfile.readline()
        [books_num, libs_num,  days_num] = line1.split()
        book_scores = line2.split()
        libs = dict()
        for i in range(int(libs_num)):
            firstline = myfile.readline()
            secondline = myfile.readline()

            [lib_books_num, lib_signup_days, books_per_day] = firstline.split(" ")
            libs[i] = Library(firstline.split()[0],firstline.split()[1],firstline.split()[2])
            lib_book_ids = secondline.split()
            for book in lib_book_ids:
                libs[i].add_book(int(book),int(book_scores[int(book)]))
    return books_num,days_num,book_scores,libs


if __name__ == "__main__":
    books_num,days_num,book_scores,libs = input_parser(sys.argv[1])

