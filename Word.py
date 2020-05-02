from General import Constants


class Word:

    def __init__(self, text):

        self.text = text

        self.left_hand_key_count = self.get_hand_key_count(Constants.left_hand_key_list)
        self.left_hand_key_percent = self.left_hand_key_count / len(self.text) * 100
        self.right_hand_key_count = self.get_hand_key_count(Constants.right_hand_key_list)
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
            self.left_hand_key_percent,
            self.right_hand_key_count,
            self.right_hand_key_percent
        )


def left_comparison(word):
    return word.left_hand_key_count


def right_comparison(word):
    return word.right_hand_key_count


def word_list_to_str(word_list):
    ret_str = ""
    for word in word_list:
        ret_str += str(word) + " | "
    return ret_str
