print("Welcome to the match stick game! \n\n Game rules: You and computer will alternatively pick the matches \n Whosoever picks the last match loses the game. Maximum 4 matches \n can be drawn at a time\n")
nm=21
while nm>1:
    print("number of matches are: ",nm)
    w=int(input("Enter the number of matchsticks to be withrawn(1/2/3/4):"))
    nm=nm-w
    if w>4:
        print("Invalid choice\nPlease enter only(1/2/3/4) as per the game rules")
        break
    if nm in [2,7,12,17]:
        nm-=1;
        print("computer has withrawn 1 match\n")
    if nm in [3,8,13,18]:
        nm-=2;
        print("computer has withrawn 2 match\n")
    if nm in [4,9,14,19]:
        nm-=3;
        print("computer has withrawn 3 match\n")
    if nm in [5,10,15,20]:
        nm-=4;
        print("computer has withrawn 4 match\n") 
    if nm==1:
        print("\nyou lose, you have only 1 match left")

