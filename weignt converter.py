weight = float(input("Enter the weight: "))
unit = input("(L)bs or (K)g: ").strip().upper()

if unit == "L":
    converted = 0.45 * weight
    print(f"The weight is: {converted:.2f} kilograms")
elif unit == "K":
    converted = weight / 0.45
    print(f"The weight is: {converted:.2f} pounds")
else:
    print("Invalid unit entered. Please use 'L' for pounds or 'K' for kilograms.")
