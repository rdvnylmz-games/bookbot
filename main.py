import sys
from stats import count_characters,count_words



def sort_on_num(item):
    return item["num"]

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <book-path>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
   
    try:
        with open(f"{book_path}","r") as f:
            file_contents = f.read()
           
    except FileNotFoundError:
        print(f"Error: File '{book_path} not found.")
        sys.exit(1)

    character_counts = count_characters(file_contents)
    word_counts = count_words(file_contents)

    char_list = [{"char":k,"num":v} for k,v in character_counts.items() if k.isalpha()]
    char_list.sort(key=sort_on_num,reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")

    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()