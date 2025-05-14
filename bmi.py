def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height*height)
    print("BMI = ", round(bmi,2))  # Round the BMI to 2 decimal points

    if bmi < 18.5:
        print("Under weight")
        return -1
    elif bmi > 25.0:
        print("Over weight")
        return 1
    else:
        print("Normal weight")
        return 0


print("--------------------------------")
calculate_bmi(1.73, 37)  # Under weight
print("--------------------------------")
calculate_bmi(1.73, 57)  # Normal weight
print("--------------------------------")
calculate_bmi(1.73, 97)  # Over weight
print("--------------------------------")

