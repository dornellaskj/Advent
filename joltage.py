# You'll need to find the largest possible joltage each bank can produce. In the above example:

# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
# In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
# In 818181911112111, the largest joltage you can produce is 92.
# The total output joltage is the sum of the maximum joltage from each bank, 
# so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357. 

# Part 2:
#Now, the joltages are much larger:

# In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
# In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
# In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
# In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
# The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

part1_total_joltage = 0
part2_total_joltage = 0

with open("joltage_data.txt", "r") as file:
    data = [line.strip() for line in file]

for line in data:
    banks = [int(ch) for ch in line]
    #find the max, then find the next max by looking at the rest of the array after finding the first max
    first_max = max(banks)
    #find the position of the first max
    first_max_index = banks.index(first_max)
    if first_max_index != len(banks) - 1:
        #split the array after the index of the first max
        banks2 = banks[first_max_index + 1:]
        second_max = max(banks2)
    else:
        second_max = max(banks)
        banks.remove(second_max)
        first_max = max(banks)
    #concat them
    combined = int(str(first_max) + str(second_max))
    #convert to int
    joltage = int(combined)
    #addd to cumulative total
    part1_total_joltage += joltage
    #part 2 - remove digits strategically to maximize the 12-digit result
    part2_banks = list(line)  # Keep as strings for easier manipulation
    
    if len(part2_banks) <= 12:
        # If we already have 12 or fewer digits, use all of them
        max_joltage = int(''.join(part2_banks)) if part2_banks else 0
    else:
        # Remove digits to maximize the result - use greedy approach
        # Remove digits where current < next (removes smaller leading digits)
        digits_to_remove = len(part2_banks) - 12
        
        i = 0
        while digits_to_remove > 0 and i < len(part2_banks) - 1:
            if part2_banks[i] < part2_banks[i + 1]:
                part2_banks.pop(i)
                digits_to_remove -= 1
                if i > 0:
                    i -= 1  # Step back to recheck
            else:
                i += 1
        
        # If we still need to remove digits, remove from the end
        while digits_to_remove > 0 and len(part2_banks) > 0:
            part2_banks.pop()
            digits_to_remove -= 1
        
        max_joltage = int(''.join(part2_banks)) if part2_banks else 0
        print(f"Part 2 - Max Joltage after removals: {max_joltage}")
    # Add this maximum joltage to our cumulative total
    part2_total_joltage += max_joltage
    
    original_length = len(line)
    result_length = len(str(max_joltage)) if max_joltage > 0 else 0
    print(f"Part 2 - Original: {original_length} digits -> Max Joltage: {max_joltage} ({result_length} digits) -> Cumulative: {part2_total_joltage}")
    
    
print(f"Part 1 - Total Output Joltage: {part1_total_joltage}")
print(f"Part 2 - Total Output Joltage: {part2_total_joltage}")



