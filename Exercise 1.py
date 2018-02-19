money=input("How much money do you have?")
afford=money/15000
print("You can buy",afford,"Nintendo Wii")
remaining=money%15000
need=15000-remaining
print("You need",need,"to buy another Wii")
