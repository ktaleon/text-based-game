print("Hello This Is Karl's Maze Game")
print("Would you like to play?(y/n)")
option = str(input())

if option == "y":
    print("You are inside a maze and you have to find your way out!")
    print("Left of Right?(l/f)")
    option = str(input())
    if option == "l":
        option = ""
        print("Left of Right?(l/f)")
        option = str(input())
        if option == "l":
            option = ""
            print("Dead end!")
        else:
            option = ""
            print("Left of Right?(l/f)")
            if option == "l":
                option = ""
                print("Left of Right?(l/f)")
                if option == "l":
                    option = ""
                    print("Left of Right?(l/f)")
                    if option == "l":
                        option = ""
                        print("Dead end!")
                    else:
                        print("Congratulations You Got Out!")
                else:
                    print("Dead end!")
            else:
                print("Dead End!")
    elif option == "r":
        option = ""
        print("Left of Right?(l/f)")
        option = str(input())
        if option == "l":
            option = ""
            print("Dead end!")
        else:
            option = ""
            print("Left of Right?(l/f)")
            if option == "l":
                option = ""
                print("Left of Right?(l/f)")
                if option == "l":
                    option = ""
                    print("Left of Right?(l/f)")
                    if option == "l":
                        option = ""
                        print("Dead end!")
                    else:
                        print("Congratulations You Got Out!")
                else:
                    print("Dead end!")
            else:
                print("Dead End!")
else:
    print("See you next time!")
