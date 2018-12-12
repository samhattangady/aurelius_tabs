import json
import os
import random

RAW_TEXT = 'data/raw_text_gutenberg.txt'
JSON_OUT = 'data/meditations.json'

books = [
        'THE FIRST BOOK',
        'THE SECOND BOOK',
        'THE THIRD BOOK',
        'THE FOURTH BOOK',
        'THE FIFTH BOOK',
        'THE SIXTH BOOK',
        'THE SEVENTH BOOK',
        'THE EIGHTH BOOK',
        'THE NINTH BOOK',
        'THE TENTH BOOK',
        'THE ELEVENTH BOOK',
        'THE TWELFTH BOOK',
        '\n\n\nAPPENDIX'
        ]

def main():
    meditations = {}
    with open(RAW_TEXT) as o:
        data = o.read().strip()
    for i, (start, end) in enumerate(zip(books, books[1:])):
        start_index = data.index(start)
        end_index = data.index(end)
        contents = data[start_index:end_index]
        contents = contents.strip().split('\n\n')[1:]
        # remove first entry (Name of book) and prepended roman numerals
        contents = [c[c.index(' ')+1:].replace('\n', ' ') for c in contents]
        for j, c in enumerate(contents):
            meditations[f'Book {i+1} : {j+1}'] = c
    with open(JSON_OUT, 'w') as o:
        o.write(json.dumps(meditations))

if __name__ == '__main__':
    main()
