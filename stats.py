def get_num_words(path_to_file):
    with open(path_to_file,"r") as book:
        word_bank = book.read().split()
        print(len(word_bank))


