from os import write

def hello_world():
    print("Hello World")
    return True
hello_world()

def get_min(my_list):
    x=my_list[0]
    for element in my_list:
        if x <= element:
            x = element
    return x