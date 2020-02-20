tests=("a_example.txt"
        "b_read_on.txt"
        "c_incunabula.txt"
        "d_tough_choices.txt"
        "e_so_many_books.txt"
        "f_libraries_of_the_world.txt"
)

counter=0

for test in ${tests[@]}; do
    python3 book_shipper.py $test $test.out
done
