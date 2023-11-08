def prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_number_list(start, end):
    prime_list = []
    for number in range(start, end + 1):
        if prime_number(number):
            prime_list.append(number)
    return prime_list


n_list = list(map(int, input().split()))

prime = prime_number_list(1, max(n_list)+n_list[0])

if prime[prime.index(n_list[0]) + 1] == n_list[1]:
     print("YES")
else:
    print("NO")
    
