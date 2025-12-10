# TODO Найдите количество книг, которое можно разместить на дискете
weight_1_book_byte = 4 * 25 * 50 * 100
perevod_mb_to_byte = 1.44 * 1024 * 1024
number_of_books = perevod_mb_to_byte // weight_1_book_byte
print("Количество книг, помещающихся на дискету:", number_of_books)
