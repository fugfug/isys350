'''
Serendipity Booksellers has a book club that awards points to its customers
based on the number of books purchased each month.
The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 6 points.
• If a customer purchases 2 books, he or she earns 16 points.
• If a customer purchases 3 books, he or she earns 32 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter
the number of books that he or she has purchased this month and
displays the number of points awarded.
'''

POINTS_0_BOOKS = 0 # number of points awarded if 0 books bought
POINTS_1_BOOKS = 6
POINTS_2_BOOKS = 16
POINTS_3_BOOKS = 32
POINTS_4_BOOKS = 60 # number of points awarded if >= 4 books bought

books_purchased = int(input('Enter the number of books purchased this month: '))
points = 0
if books_purchased == 0:
    points = POINTS_0_BOOKS
elif books_purchased == 1:
    points = POINTS_1_BOOKS
elif books_purchased == 2:
    points = POINTS_2_BOOKS
elif books_purchased == 3:
    points = POINTS_3_BOOKS
elif books_purchased >= 4:
    points = POINTS_4_BOOKS

print("Number of points awarded:", points)
