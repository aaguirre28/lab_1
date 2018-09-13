import os
import random

cat_list = [] #global variable for cat_list
dog_list = [] #global variable for dog_list

def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    #These print statements will print path of directories #DEBUG
    #print("****************************************************") #DEBUG
    #print(dir_list) #DEBUG
    #print(file_list) #DEBUG
    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    #put directoires and files into two lists
    dir_list, file_list = get_dirs_and_files(path)

    #from file_list, add to either cat_list or dog_list
    cat_list, dog_list = classify_files(file_list)

    for item in dir_list:
        #print(item) #DEBUG
        process_dir(path + "/" + item)

    return cat_list, dog_list

def classify_files(list_of_pictures):

    #decide where you will put the image
    for item in list_of_pictures:
        evaluation = classify_pic(item)
        if evaluation > .5: #if greater than .5, append to dog_list
            dog_list.append(item)
        else:
            cat_list.append(item) #if less than .5, append to cat_list

    return cat_list, dog_list

def main():
    start_path = './' # current directory
    print("This is my first lab, the lists are as follow:")
    process_dir(start_path)
    print("***********************************Cat List***********************************")
    print(cat_list)
    print("***********************************Dog List***********************************")
    print(dog_list)

main()

