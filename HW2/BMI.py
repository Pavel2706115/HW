W = int(input("Enter your weight in kg: "))
H = float(input("Enter your height in meters: "))
BMI = W / (H * H)
BMI_rounded = round(BMI, 2)
print("Your BMI is:", BMI_rounded)