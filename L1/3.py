def main():
    n = int(input())    # считываем число
    print(n % 10, '- по 1р')    # вычисляем остаток от деления на 10, это будут купюры по рублю
    print(n % 100 // 10, '- по 10р')    # вычисляем остаток от деления на 100 и делоим нацело на 10 - по 10р
    print(n % 1000 // 100, '- по 100р')    # вычисляем остаток от деления на 1000 и делоим нацело на 100 - по 100р
    print(n % 100000 // 1000, '- по 1000р')    # вычисляем остаток от деления на 10000 и делоим нацело на 1000 - по 1000р
if __name__ == "__main__":
    main() 
