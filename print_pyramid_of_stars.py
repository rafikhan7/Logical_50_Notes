#print pyramid of stars
def print_pyramid_of_stars(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '* ' * (i + 1)
        print(spaces + stars)

print_pyramid_of_stars(5)