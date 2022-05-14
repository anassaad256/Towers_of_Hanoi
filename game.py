from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack ("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
n_disks = int (input("\nHow many disks do you want to play with?\n"))
while n_disks < 3:
  print ("Enter a number greater than or equal to 3\n")
  n_disks = int (input("\nHow many disks do 3you want to play with?\n"))

for disk in reversed(range(n_disks)):
  left_stack.push(disk)

optimal_moves = (2**n_disks) - 1
print ("\nThe fastest you can solve this game is in {num} moves".format(num = optimal_moves))

#Get User Moves
def move():
    choices = []
    for stack in stacks:
        name = stack.get_name()
        letter = name[0].upper()
        choices.append(letter)
    while True:
        for i in range(len (stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print ("Enter {letter} for {name}".format (letter = letter, name = name))
        move = input("")
        if move in choices:
            for i in range (len (stacks)):
                if move == choices[i]:
                    return stacks[i]
        else: print ("\nInvalid Choice. Try Again")

#Play the Game
n_moves = 0
while right_stack.get_size() != n_disks:   
    print ("\nCurrent Stacks:")
    for stack in stacks:
        stack.print_items()
    print ("\nWhich stack do you want to move from?")
    from_stack = move()
    print ("\nWhich stack do you want to move to?")
    to_stack = move()
    if from_stack.get_size() == 0:
        print ("\nInvalid Move. You are trying to move from an empty stack. Try Again")
    elif to_stack.peek() == None or to_stack.peek() > from_stack.peek():
        to_stack.push(from_stack.peek())
        from_stack.pop()
        n_moves += 1
        print ("\nYou have made {n} moves so far".format(n = n_moves))
    else:
        print ("\nInvalid Move. You cannot move a larger disk over a smaller disk. Try Again")

print ("\nYou completed the game in {user} moves, and the optimal number of moves is {optimal}".format (user = n_moves, optimal = optimal_moves))