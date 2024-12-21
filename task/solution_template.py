def find_primes(n):
    return [x for x in range(2, n + 1) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]

if __name__ == "__main__":
    import sys
    input_data = int(sys.stdin.read())  # Чтение данных из stdin и преобразование в целое число
    print(find_primes(input_data))       # Вывод результата через stdout