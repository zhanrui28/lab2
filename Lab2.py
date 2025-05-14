print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_MAIN_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()   # Read the number sequence entered by user.
    
    # Separate the numbers sequence into short strings, using the split() function
    strlist = inputstr.split(",")
    print("After split:", strlist)

    # Convert every element in the strlist from string to float.
    floatlist = []    # Create an empty list
    for eachstr in strlist:
        floatlist.append(float(eachstr))   # Append element to the floatlist
    print("Data List:", floatlist)
    return floatlist

def calc_average(datalist):
    print("calc_average")
    total = 0.0
    for eachstr in datalist:
        total = total + float(eachstr)
    average = total / len(datalist)
    return average

def find_min_max(datalist):
    print("find_min_max")
    floatlist = datalist.copy()   # make a copy
    floatlist.sort()
    print("MIN = ", floatlist[0])
    print("MAX = ", floatlist[-1])
    return (floatlist[0], floatlist[-1])

def sort_temperature(originalList):
    print("sort_temperature ")
    floatlist = originalList.copy()   # make a copy
    floatlist.sort()
    print("Sorted list = ", floatlist)
    return floatlist

def calc_median_temperature(datalist):
    print("calc_median_temperature List Float")
    sortedlist = sort_temperature(datalist)
    listLen = len(sortedlist)
    if listLen % 2 == 1:   # Odd number, just take the middle data
        median = sortedlist[listLen//2]
    else:  # Even number, take the average of the two data at the middle
        median = (sortedlist[listLen//2 - 1] + sortedlist[listLen//2])/2
    return median

def main():
    print("*** ET0735 Lab 2 Ex3")
    display_main_menu()
    resultlist = get_user_input()

    avg = calc_average(resultlist)
    print("*** Average is ", avg)

    minimum, maximum = find_min_max(resultlist)
    print("*** Minimum is ", minimum)
    print("*** Maximum is ", maximum)

    medianTemp = calc_median_temperature(resultlist)
    print("*** Median is ", medianTemp)   
    print("*** End of program")


if __name__ == "__main__":
    main()