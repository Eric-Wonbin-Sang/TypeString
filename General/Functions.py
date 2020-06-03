
def get_strings_from_txt_to_list(file_path):
    return [x.lower().strip() for x in open(file_path, "r").read().split("\n")]


def str_to_length(data_str, length):
    return data_str[:length] + " " * (length - len(data_str))


def format_datetime(datetime_object):
    return datetime_object.strftime("%Y.%m.%d %H.%M")
