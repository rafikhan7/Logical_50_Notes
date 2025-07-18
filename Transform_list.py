from collections import Counter
from unittest import result
def Transform_list(input_list):

    """ """
    count= Counter(input_list)
    result = []
    for num in sorted(count):
        result.extend([num] * count[num])

    return result

output_example = Transform_list([0, 1, 0, 2, 0, 1, 0, 2, 0, 1])
print(output_example)  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 2, 2]