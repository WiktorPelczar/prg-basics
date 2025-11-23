###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f"{movie[0:21].upper()}")

# print title in small letters
print(f"{movie[0:21].lower()}")

# print how many times the vowel "e" appears in the title
gdzie_e = movie.count("e")
print(f"litera e występuje {gdzie_e} razy")

# print where in the text is the word "Lord"
position_lord = movie.find('Lord')
print(f'Słowo "Lord" zaczyna się na indeksie: {position_lord}')


# print where in the text is the word "dragon"
pozycjasmok = movie.find("dragon")
print(f"słowo dragon znajduje się w miejscu: {pozycjasmok} ")