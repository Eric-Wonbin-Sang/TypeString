
def main():

    left_hand_keys = [x.lower().strip() for x in open("Source Files/left_hand_keys.txt", "r").read().split("\n")]
    right_hand_keys = [x.lower().strip() for x in open("Source Files/right_hand_keys.txt", "r").read().split("\n")]

    print(left_hand_keys)
    print(right_hand_keys)


main()
