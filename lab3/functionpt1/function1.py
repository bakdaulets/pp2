#1
def gr_to_oun(a):
    return 28.3495231 * a
gramms = 10
print(gr_to_oun(gramms))

#2
def second(F):
    return (5 / 9) * (F - 32)

temp = 451
print(second(temp))

#3
def solve(numheads, numlegs):
    for i in range(numheads + 1):
        a = numheads - i
        if 2 * i + 4 * a == numlegs:
            return i , a
    else:
        print("No solution")
print(solve(35, 94))

#4
def isPrime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 0
        else:
            return 1
    else:
        return 0
def onlyprimes(list):
    for i in list:
        if not isPrime(i):
            list.remove(i)
            onlyprimes(list)
list1 = list(map(int, input().split()))
onlyprimes(list1)
print(list1)

#5
from itertools import permutations
def print_permutations(input_string):
    perm_list = permutations(input_string)
    for perm in perm_list:
        print(''.join(perm))
user_input = input("Enter a string: ")
print_permutations(user_input)

#6
def revstr(a):
    return a[::-1]
a = str(input())
b = revstr(a)
print(b)

#7
def has_33(nums):
    before = -1
    for i in nums:
        if before == i:
            return True
        else:
            before = i
    else:
        return False
list1 = [1,3,3]
print(has_33(list1))

#8
def volume(R):
    return (4/3) * R**3 * 3.14 
r = int(input())
print(volume(r))

#9
def uniqlist(list):
    uniqlist1 = []
    for i in list:
        if not (i in uniqlist1):
            uniqlist1.append(i)
    return uniqlist1
list1 = []
print(uniqlist(list1))

#10
def check(a):
    if a == a[::-1]:
        return True
    else:
        return False
s = str(input())
print(check(s))

#11
def printer(a):
    for i in a:
        print("*" * i)
    
star = []
printer(star)

#12
import random
def Guess_Number(n, true, count):
    if n == true:
        print("Good job, KBTU! You guessed my number in", count, "guesses!")
        return 0
    elif n < true:
        n = int(input("Your guess is too low.\nTake a guess.\n"))
        Guess_Number(n, true, count + 1)
    elif n > true:
        n = int(input("Your guess is too high.\nTake a guess.\n"))
        Guess_Number(n, true, count + 1)
name = input("Hello! What is your name?\n")
n = int(input("Well, " + name + ", I am thinking of a number between 1 and 20.\nTake a guess.\n"))
true = random.randint(1, 20)
count = 1
Guess_Number(n, true, count)
