def main():
    userI = input()
    userO = convert(userI)
    print(userO)

def convert(text):
    smill = text.replace(":)", "🙂")
    sad = smill.replace(":(", "🙁")

    return sad

main()