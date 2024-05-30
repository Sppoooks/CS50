def main():
    x = input("What's the time? ")
    time = convert(x)
    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time <= 13.0:
        print ("Lunch time")
    elif 18.0 <= time <= 19.0:
        print ("Dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes)/60
    return time
    
main()