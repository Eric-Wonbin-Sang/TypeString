import pyperclip

while True:

    new_input = input()
    new_input = " ".join(new_input.split(" ")[1:-2])

    new_input = new_input.split(" ")
    # new_input.insert(4, "-")
    new_input = " ".join(new_input)

    print(new_input)
    pyperclip.copy(new_input)
