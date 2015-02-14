str = input("Enter string: ")
ch = input("Enter character: ")
def count_letter(str, ch):
    letters = []
    for letter in str:
        letters.append(letter)
    return letters.count(ch)

print(count_letter(str,ch ))
