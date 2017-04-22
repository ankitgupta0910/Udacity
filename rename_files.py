import os

list_file =  os.listdir("/Users/ankitgupta/PycharmProjects/Udacity/prank")
os.chdir("/Users/ankitgupta/PycharmProjects/Udacity/prank")
saved_path = os.getcwd()

for i in list_file:
    os.rename(i, i.translate(None, "0123456789"))
    os.chdir(saved_path)
