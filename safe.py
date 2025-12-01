# The safe has a dial with only an arrow on it; around the dial 
# are the numbers 0 through 99 in order.
# So, if the dial were pointing at 11, a rotation of R8 would cause the 
# dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

# Because the dial is a circle, turning the dial left from 0 one click makes 
# it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# The dial starts by pointing at 50.
dial_position = 50
instructions = []
zero_count = 0
with open("safe_data.txt", "r") as file:
    instructions = [line.strip() for line in file]


for instruction in instructions:   
    print(instruction)
    if len(instruction) > 1:       
        direction = instruction[0]        
        movement_count = int(instruction[1:]) 
        old_position = dial_position
        
        if direction == 'R':
            new_position = (dial_position + movement_count) % 100
        else:
            new_position = (dial_position - movement_count) % 100
        
        dial_position = new_position
        
        # Count how many times we land on 0
        if dial_position == 0:
            zero_count += 1

        print(f"Dial moved from {old_position} to {dial_position}")
        print(f"Dial crossed zero {zero_count} times.")
        # pause = input("Press Enter to continue...")

print(f"Dial crossed zero {zero_count} times.")
