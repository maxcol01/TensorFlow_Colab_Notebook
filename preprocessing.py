def get_files(filename) -> list:
    with open(filename, mode="r") as file:
        return file.readlines()


def cast_list_of_list(lst: list) -> list:
    full_list = list()
    sublist = list()
    for word in lst:
        if word.startswith("###"):
            sublist = []
        elif word.isspace():
            full_list.append(sublist)
        else:
            sublist.append(word.split("\t"))
    return full_list


def cast_into_dict(filename) -> list:
    text = get_files(filename)
    big_list = cast_list_of_list(text)
    list_dico = list()
    for i, j in enumerate(big_list):
        test_dico = {}
        length = len(big_list[i])
        counter = 0
        for item in j:
            test_dico["line_number"] = counter
            test_dico["target"] = item[0]
            test_dico["text"] = item[1].strip("\n").lower()
            test_dico["total_lines"] = length
            list_dico.append(test_dico.copy())
            counter += 1

    return list_dico
