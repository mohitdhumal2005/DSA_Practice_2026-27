#                 A
#               A   C
#             A       E
#           A           G
#         A               I
#       A                   K
#     A                       M
#   A B C D E F G H I J K L M N O

n = int(input("Enter the number of rows: "))

for i in range(n):
    print('  ' * (n - i + 1), end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print(chr(65 + j), end=" ")
        else:
            print(" ", end=" ")
    print()