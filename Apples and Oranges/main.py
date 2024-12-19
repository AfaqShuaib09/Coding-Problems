def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Counts and prints the number of apples and oranges that fall within the house range [s, t].

    Parameters:
    s (int): Start of the house range.
    t (int): End of the house range.
    a (int): Location of the apple tree.
    b (int): Location of the orange tree.
    apples (list of int): Distances at which each apple falls from the apple tree.
    oranges (list of int): Distances at which each orange falls from the orange tree.
    """
    apple_positions = [a + distance for distance in apples]
    orange_positions = [b + distance for distance in oranges]
    count_apples = sum(s <= pos <= t for pos in apple_positions)
    count_oranges = sum(s <= pos <= t for pos in orange_positions)
    print(count_apples)
    print(count_oranges)
        
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
