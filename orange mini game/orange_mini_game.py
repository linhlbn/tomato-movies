import os
# rule: give the player many images, ask them to arrange them into a meaningful message!
# this function will solve that problem!
def orange_game() :
    #1. get file names from a folder
    file_list = os.listdir(r"D:\testoriginalfile")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Worrking Direction is "+saved_path)
    os.chdir(r"D:\testoriginalfile")
    #2. for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
orange_game()
