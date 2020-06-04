from General import Word


class WordAttempt:

    def __init__(self, **kwargs):

        self.time_info_dict_list = kwargs.get("time_info_dict_list")

        self.target_word = self.get_target_word()
        self.last_input = self.get_last_input()

        self.correct_cond = self.target_word.text == self.last_input

    def get_target_word(self):
        return Word.Word(text=self.time_info_dict_list[0]["current_word"])

    def get_last_input(self):
        return self.time_info_dict_list[-1]["curr_input"]

    def __str__(self):
        ret_str = "target_word: {}\tlast_input: {}\tcorrect_cond: {}".format(
            self.target_word.text,
            self.last_input,
            self.correct_cond
        )
        return ret_str
