print('Marvel Movie Character Creator\n--')
print()
spiderMan = input("Do you like 'hanging around'? Yes/No: ").upper()
if spiderMan == "NO" or 'N':
    print("Then you're not Spiderman")
    Korg = input("Do you have a 'gravelly' voice? Yes/No: ").upper()
    if Korg == "NO" or 'N':
        print("Aww, then you're not Korg")
        Marvelous = input("Do you often feel 'Marvelous'? Yes/No: ").upper()
        if Marvelous == "YES" or 'Y':
            print("Aha! You're Captain Marvel! Hi!")
        else:
            print("Oops! You're not Captain Marvel")
    else:
        print("You are Inspector Korg!")
else:
    print("You're Spiderman!")
