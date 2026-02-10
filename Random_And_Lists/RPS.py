# Rock, Paper, Scissors

print("What do you choose? 0 for rock, 1 for paper, 2 for scissors")
choice = input()

match choice:
    case "0":
        print("You chose rock!")
    case "1":
        print("You chose paper!")
    case "2":
        print("You chose scissors!")
