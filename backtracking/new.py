collect = set()

def find_max(num_str, k, max_num):
    # Return if no swaps left
    if k == 0:
        collect.add ( num_str )
        return 

    n = len(num_str)

    # Consider every digit
    for i in range(n - 1):
        # Compare it with all digits after it
        for j in range(i + 1, n):
            # If digit at position i is less than digit at position j, swap it
            # and check for maximum number so far, then recurse for remaining swaps
            if num_str[i] < num_str[j]:
                # Convert string to list to swap characters
                num_list = list(num_str)
                # Swap num_str[i] with num_str[j]
                num_list[i], num_list[j] = num_list[j], num_list[i]
                swapped_num_str = ''.join(num_list)

                # Recurse for the other k - 1 swaps
                find_max(swapped_num_str, k - 1, max_num) 

                # Backtrack: Undo the swap for backtracking
                num_list[i], num_list[j] = num_list[j], num_list[i]

# Wrapper function to initiate the find_max function
def get_maximum_number(num_str, k):
    max_num = [num_str]
    find_max(num_str, k, max_num)
    return

# Example usage
num_str = "1234"
k = 1
print(get_maximum_number(num_str, k))
print ( collect )