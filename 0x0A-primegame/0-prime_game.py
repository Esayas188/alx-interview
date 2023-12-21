def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x: The number of rounds.
        nums: An array of values for n in each round.

    Returns:
        The name of the player who won the most rounds, or None if the winner cannot be determined.
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Tie

def play_round(n):
    """
    Simulates a single round of the game.

    Args:
        n: The upper bound of the set of integers.

    Returns:
        The name of the winner of the round.
    """

    remaining_numbers = set(range(1, n + 1))
    current_player = "Maria"

    while remaining_numbers:
        prime = find_optimal_prime(remaining_numbers)
        if prime is None:
            return current_player  # Other player loses

        remaining_numbers -= remove_multiples(prime, remaining_numbers)
        current_player = "Ben" if current_player == "Maria" else "Maria"

    return None  # Tie

def find_optimal_prime(numbers):
    """
    Finds the optimal prime number to choose from the set.

    Args:
        numbers: The set of remaining numbers.

    Returns:
        The optimal prime number to choose, or None if none exist.
    """

    # Implement optimal prime-picking strategy here
    # Consider factors like:
    # - Removing the most numbers
    # - Preventing the opponent from getting a good move
    # - Corner cases (e.g., when only a few numbers remain)

    # Placeholder for now:
    primes = [num for num in numbers if is_prime(num)]
    return primes[0] if primes else None

def remove_multiples(prime, numbers):
    """
    Removes the prime number and its multiples from the set.

    Args:
        prime: The prime number to remove.
        numbers: The set of numbers to modify.

    Returns:
        A new set with the prime number and its multiples removed.
    """

    return {num for num in numbers if num % prime != 0}

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """

    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
