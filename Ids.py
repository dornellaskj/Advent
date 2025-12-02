# Part 1:Since the young Elf was just doing silly patterns, you can find the invalid IDs 
# by looking for any ID which is made only of some sequence of digits repeated twice. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
# Part 2: Now, an ID is invalid if it is made only of some sequence of digits repeated
# at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 
# 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

ranges = []
invalid_ids_cumulative = 0
part2_invalid_ids_cumulative = 0
with open("Ids_data.txt", "r") as file:
    data = [line.strip() for line in file]


for line in data:
    ranges = line.split(',')
for r in ranges:
    ranges_split = []
    ranges_split = str(r).split('-')
    start = int(ranges_split[0])
    end = int(ranges_split[1])
    for i in range(start, end + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:  
            # : in the front gets the first half, colon at the end gets the second
            print(f"Invalid ID part 1: {i}")
            invalid_ids_cumulative += int(i)
            part2_invalid_ids_cumulative += int(i)
        else:
            for j in range(len(s)):
                # find the other craziness            
                if j > 0:                
                    if len(s) % int(j) == 0: # check only for j that divides length of s evenly make more faster!
                        substring = s[:j]
                        parts_array = []
                        rest = s
                        for k in range(len(s) // len(substring)):
                            if i == (len(s) // len(substring)) - 1:   # last item
                                parts_array.append(rest)
                            else:
                                parts_array.append(rest[:len(substring)])
                                rest = rest[len(substring):]
                        if  len(parts_array) > 1 and all(item == parts_array[0] for item in parts_array):
                            print(f"Part 2 - Invalid ID found: {i}")
                            print(f"Part: {parts_array[0]}")
                            part2_invalid_ids_cumulative += int(i)
                            break # break out of the loop once an invalid ID is found, we don't want to double count
                            #pause = input("Press Enter to continue...")
print(f"The sum of all invalid IDs is: {invalid_ids_cumulative}")
print(f"The sum of all Part 2 invalid IDs is: {part2_invalid_ids_cumulative}")