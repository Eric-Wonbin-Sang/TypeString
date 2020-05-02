import Word

from General import Functions, Constants


def get_word_list():
    string_list = Functions.get_strings_from_txt_to_list("Source Files/1000 most common words.txt")
    return [Word.Word(string) for string in string_list]


def main():

    print(Constants.left_hand_key_list)
    print(Constants.right_hand_key_list)

    word_list = get_word_list()
    left_hand_word_list = Word.order_word_list_by_hand("left", word_list)
    right_hand_word_list = Word.order_word_list_by_hand("right", word_list)

    print(Word.word_list_to_str(word_list))
    print(Word.word_list_to_str(left_hand_word_list))
    print(Word.word_list_to_str(right_hand_word_list))


main()
