import time

def menu():
    print("Welcome to this pretty simple game of Minesweeper.")
    time.sleep(1)
    print("If you want to play press 1")
    time.sleep(1)
    answer = int(input("Otherwise press 2"))
    
    if answer == 1:
        print("Safe")
        playgame()
    elif answer == 2:
        print("Bye")
        import sys
        if 10/5 == 2:
            sys.exit()
    else:
        print("Try again idiot")
        menu()
menu()
    
