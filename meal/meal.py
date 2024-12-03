def main():
    inputtime = input("What time is it?")

    convertedtime = convert(inputtime)

    if 7 <= convertedtime <=8:
        print ("breakfast time")

    elif 12 <= convertedtime <=13:
        print ("lunch time")

    elif 18 <= convertedtime <=19:
        print ("dinner time")

def convert(time):
    time = time.rstrip("am").strip()
    time = time.rstrip("pm").strip()

    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    minutes = minutes / 60
    return float(hours + minutes)

if __name__ == "__main__":
    main()
