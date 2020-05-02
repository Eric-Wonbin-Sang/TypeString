
def get_strings_from_txt_to_list(file_path):
    return [x.lower().strip() for x in open(file_path, "r").read().split("\n")]
