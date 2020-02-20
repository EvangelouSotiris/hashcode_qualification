from library import Library
import pprint
import sys
import operator

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
            libs[i] = Library(i,firstline.split()[1],firstline.split()[2])
            lib_book_ids = secondline.split()
            for book in lib_book_ids:
                libs[i].add_book(int(book),int(book_scores[int(book)]))
    return books_num,days_num,book_scores,libs

def output_creator(lib_chosen, output_filename):
    with open(output_filename, "w") as myfile:
        myfile.write(str(len(lib_chosen))+"\n")
        for item in lib_chosen:
            myfile.write(str(item[0])+" "+str(item[1])+"\n")
            for i in range(item[1]):
                myfile.write(str(list(item[2].books.keys())[i])+" ")
            myfile.write("\n")


def sort_lib_books_by_score(libs):
    for i in libs:
        libs[i].sort_by_score()

if __name__ == "__main__":
    books_num,days_num,book_scores,libs = input_parser(sys.argv[1])
    sort_lib_books_by_score(libs)
    libs = [lib for lib in (sorted(libs.values(), key=operator.attrgetter('signup_days')))]

    days_left = int(days_num)
    counter = -1
    lib_chosen = []
    libs.reverse()
    while (days_left > 0):
        if ( abs(counter) > len(libs)):
            break
        library_on_signup = libs[counter]
        signup = library_on_signup.signup_days
        days_left -= int(signup)
        if (days_left <= 0):
            continue
        else:
            books_can_scan = min(days_left * int(library_on_signup.books_per_day),len(library_on_signup.books))
        lib_chosen.append((library_on_signup.index,books_can_scan,library_on_signup))
        counter -= 1
    output_creator(lib_chosen,sys.argv[2])

