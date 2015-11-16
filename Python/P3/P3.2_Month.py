month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

Do quit = input("If you want to quit, type 'exit', if not, press enter: ") while quit != exit:
    monthIn = int(input("Type the number you want to know the corresponding month to: "))
    if monthIn >= 1 and monthIn <= 12:
        print(month[monthIn-1])
    else:
        print("Please enter a valid number!")
    
print("Thanks for using me!")
    

