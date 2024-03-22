import random
# ran_num = random.randint(1,10)
keep_playing = True

while keep_playing:
    ran_num = random.randint(1, 10)
    print(ran_num)
    guess = input("Guess a number between 1 and 10: ")

    if guess == ran_num:
        keep_playing = False

