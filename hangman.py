from string import ascii_lowercase as suscii_lowercase
from getpass import getpass as getsus
from os import system as sustem
import sys as sus
platform = sus.platform

word = getsus("Enter Hangman word: ").lower()
word_og = word

lines = []


for letter in word:
    if letter == " ": lines.append("  ")
    else: lines.append("_")   


head1, head2, head3, head4, body1, body2, body3, body4, body5, rarm1, rarm2, larm1, larm2, lleg1, lleg2, rleg1, rleg2, leye, reye, mouth, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = " ", " ", " ", " ", " ", " ", " ", " ", " ", "   ", "   ", "   ", "   ", " ", " ", " ", " ", " ", " ", "  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 

def cls():
    if "win" in platform:
        sustem("cls")
    else:
        sustem("clear")

def loose_check():
    global errors, word_og
    if errors == 8:
        print("You loose!\nThe word was:" + word_og)
        exit()

def win_check():
    global lines, word_og
    if "".join(lines) == word_og:
        print("You win!")
        exit()

def stats():
    global head1, head2, head3, head4, body1, body2, body3, body4, body5, rarm1, rarm2, larm1, larm2, lleg1, lleg2, rleg1, rleg2, leye, reye, mouth, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    if errors == 8: mouth =  "👄" 
    if errors == 7: leye, reye = "👁", "👁"
    if errors >= 1: head1, head2, head3, head4 = r"  ___", " /   \\", f"( {leye} {reye} )", f" \{mouth} /"
    if errors == 2: body1, body2, body3, body4, body5= r"  ___", " |   |", r" |   |", r" |   |", r"  --- "
    if errors == 3: rarm1, rarm2 = "---", "---"
    if errors == 4: larm1, larm2 = "---", "---"
    if errors == 5: lleg1, lleg2 = " / /", "/ /"
    if errors == 6: rleg1, rleg2 =  "\\ \\"," \\ \\"
    return f"""{" ".join(lines)}      |Errors: {errors}|\n{a} {b} {c} {d} {e}     {head1}\n{f} {g} {h} {i} {j}     {head2}\n{k} {l} {m} {n} {o}     {head3}\n{p} {q} {r} {s} {t}     {head4}\n{u} {v} {w} {x} {y}     {body1}\n{z}             {body2}\n       {larm1}{larm2} {body3} {rarm1}{rarm2}\n              {body4}\n              {body5}\n             {lleg1} {rleg1}\n             {lleg2}  {rleg2}"""

errors = 0


print(stats())


while True:
    print("Type \"guess\" to take a guess.")
    inp = input("Letter: ").lower()
    if inp == "guess":
        inp = input("Guess: ").lower()
        if inp == word:     
            print("You Win!")
            exit()
        else:     
            errors += 1
            cls()
            print(stats())
            loose_check()
            continue

    elif inp not in suscii_lowercase or inp == "": 
        print("Invalid Character!")
        continue


    if word.find(inp) == -1: 
        errors += 1
        exec(f"{inp} = inp")
    else: 
        exec(f"{inp} = inp")
        while word.find(inp) != -1:
            found = word.find(inp)
            lines[found] = inp
            word = word.replace(inp, "|", 1)
            
    cls()
    print(stats())
    loose_check()
    win_check()
