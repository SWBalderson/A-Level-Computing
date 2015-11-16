
phrase = ["and a Partridge in a Pear Tree.", "Turtle Doves", "French Hens", "Calling Birds", "Gold Rings", "Geese a-Laying", "Swans a-Swimming", "Maids a-Milking", "Ladies Dancing", "Lords a-Leaping", "Pipers Piping", "Drummers Drumming"]
dayname = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelth"]
day = int(input("What day of Christmas is it? (1-12) "))-1
if day == 0:
    print("On the first day of Christmas, my true love gave to me: A Partridge in a Pear Tree")
else:
    print("On the " + dayname[day] + " day of christmas, my true love gave to me: ", end=str(day+1) + " " + phrase[day])
    for i in range(day-1, -1, -1):
        if i==0:
            print(" and a Partridge in a Pear Tree.")
        else:
            print(", " + str(i+1) + " " + phrase[i], end="")
