import random

def generate_random_chars():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))

st = input("Enter message: ")
words = st.split(" ")  # words are split into a list
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding == "1") else False
print(coding)

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = generate_random_chars()
            r2 = generate_random_chars()
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # reversing the string
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
