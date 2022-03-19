//coded by harish rane


s = input("Enter the string")
words = s.split(",")

for w in words:
    if s.count(w)==1:
        print(w)
