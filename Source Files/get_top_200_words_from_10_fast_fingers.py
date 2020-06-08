import os


def get_word_list(html_path):
    word_list = []
    with open(html_path, "r", encoding='utf-8') as f:
        for part in f.read().split("\n"):
            if '<div id="words" class="row"' in part[:30].strip():
                for a_part in part.split("wordnr=")[1:]:
                    word_list.append(a_part.split(">")[1].split("<")[0].strip())
                break
    return word_list


def main():

    txt_file_path = "10fastfingers top 200 words.txt"

    os.remove(txt_file_path)

    html_path_0 = "Typing Test English - 10FastFingers.com.html"
    html_path_1 = "Typing Test English - 10FastFingers.com 1.html"

    word_list = get_word_list(html_path_0) + get_word_list(html_path_1)
    word_list = list(dict.fromkeys(word_list))

    temp_word_list = []
    for word in word_list:
        if len(word) >= 2 and word not in ["som"]:
            temp_word_list.append(word)
    word_list = temp_word_list

    print("Numbers of words found: {}".format(len(word_list)))
    for word in word_list:
        print("\t{}".format(word))

    with open(txt_file_path, "a") as txt_file:
        for i, word in enumerate(word_list):
            if i != 0:
                txt_file.write("\n")
            txt_file.write(word)


main()
