def is_prime(num):
    for i in range(2, int(num**1/2)+1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
non_prime_numbers = []
for i in range(1, 20):
    if is_prime(i + 1):
        prime_numbers.append(i+1)
    else:
        non_prime_numbers.append(i+1)

print(prime_numbers)
print(non_prime_numbers)