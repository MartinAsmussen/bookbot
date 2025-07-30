import sys
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents=f.read()
    return file_contents

def main():
     return get_book_text(sys.argv[1])

from stats import sor_list
from stats import character_count
from stats import word_count
count=word_count(main())
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
big_list=sor_list(character_count(main()))
for i in big_list:
    print(f"{i["char"]}: {i["num"]}")
print("============= END ===============")