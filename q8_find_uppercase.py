str = input("Enter your string here: ")
def find_num_uppercase(str):
    count = 0
    for letters in str:
        if letters.isupper():
            count += 1
    return count
print(find_num_uppercase(str))
