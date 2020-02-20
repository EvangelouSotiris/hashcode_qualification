def input_parser(filename):
    with open(filename, "r") as file:
        line1 = file.readline()
        line2 = file.readline()
        [books_num, libs_num,  days_num] = line1.split(" ")
        book_scores = line2.split(" ")
        for i in range(libs_num):
            firstline = file.readline()
            secondline = file.readline()
            [lib_books_num, lib_signup_days, books_per_day] = firstline.split(" ")
            lib_book_ids = secondline.split(" ")
    return 1
