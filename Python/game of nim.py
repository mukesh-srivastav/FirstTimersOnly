#game of nim

"""
Rules
1.You take turns with the computer to take away 1/2 coins from a stack of coins
2.Player to take last coin wins
"""

n=int(input("Enter number of coins in stack (>3):"))
print("OK! Lets Play!")
print("You get to go first ;)")
while n>0:
    taken=int(input("How many do you want to take (1/2)? :"))
    if taken not in range(1,3):
        print("Not cool...play by the rules")
        continue
    n=n-taken
    if n>0: #this if is only to check whether there are coins left for the computer
        if n%3==0:
            print("Ok..then i ll take...1!")
            n=n-1
        elif n%3==1:
            print("Ok..then i ll take...1!")
            n=n-1
        else:
            print("Ok..then i ll take...2!")
            n=n-2
        print("Number of coins left:",n)
        
if n==0:
    print("Ha Ha! I win...better luck next time ;)")
else:
    print("hmm...you win..")


"""
try and observe that whether you can win or not actually depends on the initial
number of coins you take :)

to understand this better, think about what would happen if you could
only take 1 each?
"""
        
