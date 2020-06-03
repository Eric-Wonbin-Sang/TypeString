import os


def main():

    directory = "C:\\Users\\ericw\\Downloads\\The Office US - The Complete Season 7 [HDTV]"
    
    for count, filename in enumerate(os.listdir(directory)):

        # print(filename)

        new_filename = filename.replace(".", " ").upper().title()
        extension = "." + filename.split(".")[-1]

        temp_list = []
        for word in new_filename.split(" "):
            # if word == "1080P" or word == "Amzn" or word == "Webrip":
            #     break
            if word == "Hdtv":
                break
            # if word in "(Us)":
            #     continue
            temp_list.append(word)
        new_filename = " ".join(temp_list)
        new_filename += extension
        # new_filename = new_filename.replace(" Mkv", "")
        print(new_filename)

        # os.rename(directory + "\\" + filename, directory + "\\" + new_filename)


main()
