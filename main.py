from os import write

def hello_world():
    print("Hello World")
    return True

def get_min(my_list):
    min_value = my_list[0]
    for element in my_list:
        if min_value >= element:
            min_value = element
    return min_value

def get_max(my_list):
    max_value = my_list[0]
    for element in my_list:
        if max_value <= element:
            max_value = element
    return max_value


hello_world()