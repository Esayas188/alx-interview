def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    """Generate a list of primes up to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def mark_multiples(nums, prime):
    """Mark all multiples of prime as 0 in nums."""
    for i in range(prime * 2, len(nums), prime):
        nums[i] = 0

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = generate_primes(n + 1)
        # Create a list of consecutive integers starting from 1 up to n
        nums_list = [i for i in range(n + 1)]
        
        for prime in primes:
            if prime > n:
                break
            mark_multiples(nums_list, prime)
        
        # Count the remaining numbers in the list after marking multiples
        count = sum(1 for num in nums_list if num > 1)
        
        # Check the count to determine the winner
        if count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function with the given example
print("Winner:", isWinner(3, [4, 5, 1]))  # Output should be "Ben"
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Output should be "Ben"
