isRepeat = True

while isRepeat == True:
    name = input("Enter a name:")
    print(f"Hi {name}")

    if name.lower() == "rhea":
        print("LOOP TERMINATED")
        isRepeat = False
        break