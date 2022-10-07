from data import data
import time

"""
Compare two questions together, if the user gets it right, a point is added to his score
"""

score = 0
# a = data[1]
# print(a)
# print(data[1]["name"])

users = []
follow = []
d = []
c = []

for i in range(1, 6):
    names = data[i]["name"]
    users.append(names)
    followers = data[i]["follower_count"]
    follow.append(followers)
    descr = data[i]["description"]
    d.append(descr)
    country = data[i]["country"]
    c.append(country)

check = True
while check:
    i = 0
    while i < 5:
        print(f"Compare A: {users[i]}, a {d[i]}, from {c[i]}")
        A = follow[i]
        print(f"Compare B: {users[i+1]}, a {d[i+1]}, from {c[i+1]}\n")
        B = follow[i+1]
        request = input("Who has more followers? Type 'A' or 'B':\n").upper()

        if request == "A":
            if A > B:
                score += 1
                print(f"You're right! Current score is {score}")
            else:
                print(f"You're wrong! Your score is {score}")
                check = False
                break

        elif request == "B":
            if B > A:
                score += 1
                print(f"You're right! Current score is {score}")
            else:
                print(f"You're wrong! Your score is {score}")
                check = False
                break
        else:
            print("Enter a correct alphabet")
            check = True
            time.sleep(0.5)
            print()
            break

        i += 1
        print()
        time.sleep(0.5)
