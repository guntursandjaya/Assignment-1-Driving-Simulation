# Print Initial
def main():
    text2 = []
    text = input().split("-")
    for i in text:
        text2.append(i[0])
    print("".join(text2).upper())
main()
