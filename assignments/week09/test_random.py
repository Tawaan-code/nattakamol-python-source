import random

def test_random():
    #สร้าง random number สุ่มระหว่าง 1-10
    random_number = random.randint(1, 10)
    print(random_number)
    guess_number = input("What is your guess number : ")
    guess_number = int(guess_number)
    if random_number == guess_number:
        print("Congrulations!")
    
    if random_number < guess_number :
        print("Too low")
    
test_random()