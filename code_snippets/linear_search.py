def linear_search(arr, target):
    """
    Perform linear search on a list.
    
    Parameters:
    arr (list): List of elements to search
    target: Element to find
    
    Returns:
    int: Index of target if found, otherwise -1
    """

    for index in range(len(arr)):
        if arr[index] == target:
            return index   # Target found

    return -1   # Target not found


# Example usage
if __name__ == "__main__":
    numbers = [10, 25, 33, 47, 52]
    key = 33

    result = linear_search(numbers, key)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")