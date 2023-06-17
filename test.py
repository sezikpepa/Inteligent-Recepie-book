import concurrent.futures

def calculate_maximum(segment):
    # Extract the integer value and corresponding string from each sublist
    values = [(sublist[0], sublist[1]) for sublist in segment]
    max_value = max(values, key=lambda x: x[0])
    return max_value

def calculate_maximum_in_segments(lst):
    segment_size = len(lst) // 8
    segments = [lst[i:i+segment_size] for i in range(0, len(lst), segment_size)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # Calculate maximum concurrently for each segment
        results = [executor.submit(calculate_maximum, segment) for segment in segments]

        # Get the maximum from the results
        maximums = [result.result() for result in concurrent.futures.as_completed(results)]
        final_maximum = max(maximums, key=lambda x: x[0])

    return final_maximum

# Example usage
my_list = [[2, 'abc'], [5, 'def'], [8, 'xyz'], [3, 'pqr'], [7, 'lmn'], [9, 'uvw'], [4, 'ijk'], [6, 'ghi'], [2, 'stu'], [1, 'mno']]
maximum = calculate_maximum_in_segments(my_list)
print("Maximum value:", maximum[0])
print("Associated string:", maximum[1])