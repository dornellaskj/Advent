#The forklifts can only access a roll of paper if there are fewer than four rolls of paper
# in the eight adjacent positions. If you can figure out which rolls of paper the forklifts
# can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
#part 2 : Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper
# is removed, the forklifts might be able to access more rolls of paper, which they might also
# be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
data = []
new_data = []
cumulative_accessible_rolls = 0
with open("paper_rolls_data.txt", "r") as file:
    data = [line.strip() for line in file]


def is_accessible(line1, line2, line3):
    total_moveable_roll_count = 0
    new_line2 = line2
    for i in range(len(line2)):
        if line2[i] == '.':
            continue  # No papers here, skiparoonie
        grid = []
        # get that 1st line of the grid
        if line1 is not None:
            if i > 0:
                grid.append(line1[i - 1])
            else:
                grid.append('.')
            grid.append(line1[i])
            grid.append(line1[i + 1] if i + 1 < len(line1) else '.')
        else:
            grid.append('.')
            grid.append('.')
            grid.append('.')

        # get that 2nd line of the grid
        if i > 0:
            grid.append(line2[i - 1])
        else:
            grid.append('.')
        grid.append(line2[i + 1] if i + 1 < len(line2) else '.')

        # get that 3rd line of the grid
        if line3 is not None:
            if i > 0:
                grid.append(line3[i - 1])
            else:
                grid.append('.')
            grid.append(line3[i])
            grid.append(line3[i + 1] if i + 1 < len(line3) else '.')
        else:
            grid.append('.')
            grid.append('.')
            grid.append('.')

        # Check the number of adjacent '@'s
        #print(f"Grid around position {i} in line2: {grid}")
        if grid.count('@') < 4:
            total_moveable_roll_count += 1
            #remove the roll
            new_line2 = new_line2[:i] + '.' + new_line2[i+1:]

    new_data.append(new_line2)
    return total_moveable_roll_count


#define search grid
def do_removal_iteration(cumulative_accessible_rolls):
    for index, line in enumerate(data):
        line1 = data[index - 1] if index > 0 else None
        line3 = data[index + 1] if index < len(data) - 1 else None
        count = 0
        count = is_accessible(line1, line, line3)
        #print(f"Line {index} has {count} accessible rolls of paper.")
        cumulative_accessible_rolls += count
    return cumulative_accessible_rolls

previous_total = 0
while True:
    cumulative_accessible_rolls = do_removal_iteration(cumulative_accessible_rolls)
    data = new_data.copy()
    new_data = []
    print(f"removal iteration complete. Total accessible rolls so far: {cumulative_accessible_rolls}")
    #print(f"New data after removal iteration:{new_data}")
    if cumulative_accessible_rolls == previous_total:
        # No more rolls can be removed
        break
    else:
        previous_total = cumulative_accessible_rolls

print(f"Total accessible rolls of paper: {cumulative_accessible_rolls}")