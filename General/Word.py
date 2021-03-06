import random

from General import Functions, KeyboardInfo


class Word:

    def __init__(self, text):

        self.text = text

        self.left_hand_key_count = self.get_hand_key_count(KeyboardInfo.left_hand_key_list)
        self.right_hand_key_count = self.get_hand_key_count(KeyboardInfo.right_hand_key_list)

        self.left_hand_key_percent = self.left_hand_key_count / len(self.text) * 100
        self.right_hand_key_percent = self.right_hand_key_count / len(self.text) * 100

    def get_hand_key_count(self, hand_key_list):
        count = 0
        for letter in self.text:
            if letter in hand_key_list:
                count += 1
        return count

    def __str__(self):
        return "w: {}\tl: {} ({}%)\tr: {} ({}%)".format(
            self.text,
            self.left_hand_key_count,
            "%.2f" % self.left_hand_key_percent,
            self.right_hand_key_count,
            "%.2f" % self.right_hand_key_percent
        )


def left_comparison(word):
    return word.left_hand_key_count


def right_comparison(word):
    return word.right_hand_key_count


def get_word_list():
    string_list = Functions.get_strings_from_txt_to_list("Source Files/10fastfingers top 200 words.txt")
    return [Word(string) for string in string_list]


def word_list_to_str(word_list):
    ret_str = ""
    for word in word_list:
        ret_str += str(word) + " | "
    return ret_str


def order_word_list_by_hand(hand_type, word_list):
    if hand_type == "left":
        return sorted(word_list, key=left_comparison)
    return sorted(word_list, key=right_comparison)


def get_left_hand_word_list(word_list, do_shuffle=True):
    left_hand_word_list = [word for word in order_word_list_by_hand("left", word_list) if
                           word.left_hand_key_percent == 100]
    if do_shuffle:
        random.shuffle(left_hand_word_list)
    return left_hand_word_list


def get_right_hand_word_list(word_list, do_shuffle=True):
    right_hand_word_list = [word for word in order_word_list_by_hand("left", word_list) if
                            word.right_hand_key_percent == 100]
    if do_shuffle:
        random.shuffle(right_hand_word_list)
    return right_hand_word_list
