# The safe has a dial with only an arrow on it; around the dial 
# are the numbers 0 through 99 in order.
# So, if the dial were pointing at 11, a rotation of R8 would cause the 
# dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

# Because the dial is a circle, turning the dial left from 0 one click makes 
# it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# The dial starts by pointing at 50.

# Part 2:
# "Due to newer security protocols, please use password method 0x434C49434B until further notice."
# You remember from the training seminar that "method 0x434C49434B" means you're actually supposed 
# to count the number of times any click causes the dial to point at 0, regardless of whether it 
# happens during a rotation or at the end of one.
dial_position = 50
instructions = []
zero_count = 0
point_at_zero_count = 0
with open("safe_data.txt", "r") as file:
    instructions = [line.strip() for line in file]


for instruction in instructions:   
    print(instruction)
    if len(instruction) > 1:       
        direction = instruction[0]        
        movement_count = int(instruction[1:]) 
        old_position = dial_position
        
        if direction == 'R':
            for i in range(movement_count):
                if dial_position == 99:
                    point_at_zero_count += 1
                    dial_position = -1
                dial_position = (dial_position + 1)

        else:
            for i in range(movement_count):
                if dial_position == 1:
                    point_at_zero_count += 1
                if dial_position == 0:
                    dial_position = 100
                dial_position = (dial_position - 1)
        
        # Count how many times we land on 0 (Part 1)
        if dial_position == 0:
            zero_count += 1

        print(f"Dial moved from {old_position} to {dial_position}")
        print(f"Part 1 - Dial landed on zero {zero_count} times.")
        print(f"Part 2 - Dial pointed at zero {point_at_zero_count} times.")
        # pause = input("Press Enter to continue...")

print(f"Part 1 - Dial landed on zero {zero_count} times.")
print(f"Part 2 - Dial pointed at zero {point_at_zero_count} times.")
