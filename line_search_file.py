import os
import random
import json


# Define a string to int function


def make_int(string):
    string = string.strip()
    return int(string) if string else 0


# Define variables and set them to user's input


path_folder = input("FOLDER_PATH")
filentype = input("FILE.TXT")
json_file = input("JSON_PATH.json")


# Add default value in case of lack of input


if path_folder == "":
    path_folder = "/home/p1m5/Downloads/package/messages"
if filentype == "":
    filentype = "messages.csv"
if json_file == "":
    json_file = "/home/p1m5/Downloads/package/messages/index.json"


# Define arrays


lines = []
folders = []


# Sort directories


for f in sorted(os.listdir(path_folder)):
    folders.append(f)


# Remove index.json file from directory array (last file)*


folders.pop(folders.index("index.json"))


# Choose a random folder and return the folder name


def rand_f():
    randfolder = folders[random.randrange(0, len(folders))]
    return randfolder


# Set new path for the file using the folder path and the randomly selected folder to enter


path_file = path_folder + "/" + rand_f() + "/" + filentype


# Open file and read through every line then add them to the array


with open(path_file, 'r') as infile:
    for line in infile:
        lines.append(line)


# Open the JSON file and load it then return the value corresponding to the provided to the function id


def return_from_fid(e_id):
    with open(json_file, 'r') as jsonfile:
        lines_j = json.load(jsonfile)
        return lines_j[e_id]


# Fix error if the value is null


fname = return_from_fid(rand_f())
if fname is None:
    fname = "null"


# Choose a random line from the file then replace the id with the value


def print_line():
    randline = lines[random.randrange(1, len(lines))]
    line_out = randline.replace(randline[0:18], fname)
    return line_out


# Call and print function


print(print_line())
