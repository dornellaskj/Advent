with open("tach_data.txt", "r") as file:
    data = [line.strip() for line in file]
print("Data loaded:", data)


def count_timelines(data):
    timeline_states = []
    indexes = []
    beam_split_counter = 0

    for index, line in enumerate(data):
        next_line_indexes = []

        if 'S' in line:
            next_line_indexes.append(line.index('S'))

        for start_index in indexes:
            if line[start_index] != '^':
                line = line[:start_index] + '|' + line[start_index+1:]
                next_line_indexes.append(start_index)
            else:  # splitter
                beam_split_counter += 1
                if start_index > 0 and start_index < len(line) - 1:
                    line = line[:start_index-1] + '|' + line[start_index] + '|' + line[start_index+2:]
                    next_line_indexes.append(start_index + 1)
                    next_line_indexes.append(start_index - 1)
                elif start_index == 0:
                    line = '|' + line[start_index+1:]
                    next_line_indexes.append(start_index + 1)
                elif start_index == len(line) - 1:
                    line = line[:start_index-1] + '|'
                    next_line_indexes.append(start_index - 1)
        timeline_states.append(list(set(next_line_indexes)))
        indexes = list(set(next_line_indexes))
        data[index] = line
    timeline_states = list(set(tuple(state) for state in timeline_states))
    print(f"Timelinestates: {timeline_states}: {line} -> Next indexes: {next_line_indexes}")
    timeline_count = 0
    for state in timeline_states:
        timeline_count += len(state)
    return {
        "beam_splits": beam_split_counter,
        "timeline_count": timeline_count -1
    }

result = count_timelines(data)
print("Beam splits:", result["beam_splits"])
print("Timeline counts:", result["timeline_count"])

#part 2 3062 too low.