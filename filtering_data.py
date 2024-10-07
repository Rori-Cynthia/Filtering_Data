characters = {
    "Mages" : ["Harry Houdini","David Blaine","Teller",],
    "Scientist" : ["Newton","Hawking","Einstein",],
    "Others" : ["Messi","Pele","Juanes",],
}

def make_great(names_list):
    for element in range(len(names_list)):
        names_list[element] = "The Great " + names_list[element]


def print_names():
    for group in characters.values():
        for name in group:
            print(name)


def run():
    print_names()
    make_great(characters["Mages"])
    print(characters["Mages"], characters["Scientist"], characters["Others"], sep="\n")


if __name__ == "__main__":
    run()