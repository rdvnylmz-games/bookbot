from stats import count_characters

def main():
    with open("books/frankenstein.txt","r") as f:
        file_contents = f.read()




    character_counts = count_characters(file_contents)
    print("Character counts:", character_counts)

if __name__ == "__main__":
    main()