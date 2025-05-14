print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def calc_average():
    print("calc_average")

def get_user_input():
    print("get_user_input")
    inputstr=input()
    strlist = inputstr.split(",")
    print(strlist)
    return strlist

def calc_average(strlist):
    print("calc_average")
    total = 0.0
    for eachstr in strlist:
        total = total + float(eachstr)
    average = total / len(strlist)
    return average

def find_min_max(strlist):
    print("find_min_max")
    

def sort_temperature():
    print("sort_temperature ")

def calc_median_temperature():
    print("calc_median_temperature List Float")