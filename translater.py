def translater():

    text = input("Type your text what you want translate to Binary:\n")
    translater = []
    if text:
        for l in text:
            translater.append("{:08b}".format(ord(l)))
        output = " ".join(translater)
        print (f" Your text to binary: :\n {output}")
    else:
        print(f"Invalid input {text}")

translater()
