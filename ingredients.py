#The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all 
# fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.
#The Elves are trying to determine which of the available ingredient IDs are fresh. 
#Part 2: The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

# So that they can stop bugging you when they get new inventory, the Elves would like to know all of
#  the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still 
# considered fresh if it is in any range.

# Now, the second section of the database (the available ingredient IDs) is irrelevant. 
# Here are the fresh ingredient ID ranges from the above example:

# 3-5
# 10-14
# 16-20
# 12-18
# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20.
# So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

# Process the database file again. How many ingredient IDs are considered to be 
# fresh according to the fresh ingredient ID ranges?
good_ingredient_ids = []
part2_good_ingredient_count = 0
part2_ranges = []
merged_ranges = []
with open("ingredient_ranges.txt", "r") as file:
    fresh_ingerdient_ranges = [line.strip() for line in file]
with open("ingredient_ids.txt", "r") as file:
    ingredient_ids = [line.strip() for line in file]

for line in fresh_ingerdient_ranges:
    ranges = line.split('-')
    start = int(ranges[0])
    end = int(ranges[1])
    for ingredient_id in ingredient_ids:
        id_int = int(ingredient_id)
        if id_int >= start and id_int <= end:
            good_ingredient_ids.append(id_int)
            print(f"Ingredient ID {ingredient_id} is fresh (in range {start}-{end})")
    #part 2 - no need to check ingredient ids, just count all ids in the ranges
    #need to find the total number of unique ids in all ranges without brute forcing all ids into a list
    #check for overlaps and merge ranges
    #memory error will need to do subtraction after overlapping ranges are merged
   
    part2_ranges.append((start, end))
for index, r in enumerate(sorted(part2_ranges)):
    #merge these mofos
    #add the first range
    range_start, range_end = r
    if index == 0:
        merged_ranges.append((range_start, range_end))
    else:
        for merged_index, merged_range in enumerate(merged_ranges):
            last_start, last_end = merged_range
            if range_start <= last_end + 1:  # Overlap or contiguous
                #extend the exiting range
                merged_ranges[merged_index] = (last_start, max(last_end, range_end))
                print(f"Merging range {range_start}-{range_end} into existing range {last_start}-{last_end} to form {merged_ranges[merged_index]}")
                break
        else:
            #not in any existing ranges
            merged_ranges.append((range_start, range_end))
        
part2_good_ingredient_ids = []
for start, end in merged_ranges:
    part2_good_ingredient_count += end - start + 1
   
good_ingredient_ids = list(set(good_ingredient_ids))  # Remove duplicates

print(f"Total number of fresh ingredient IDs: {len(good_ingredient_ids)}")
print(f"Total number of fresh ingredient IDs (Part 2): {part2_good_ingredient_count}")