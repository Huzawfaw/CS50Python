def convert(a):
    a=a.replace(":)" , "🙂")
    a=a.replace(":(" , "🙁")
    print(a)

def main():
    text=input("Write some text with emotions:")
    convert(text)

main()
