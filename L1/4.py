def main():
    print('Оцените развлекательный комплекс:')
    ocenka = input().lower()    # Вводится число и преобразуется в нижний регистр
    
    print('Результат анализа:', end=' ')
    print(ocenka.find('увлекательно'), end=' ')  # Выводится индекс слова увлекательный
    print(ocenka.find('весело'), end=' ')    # Выводится индекс слова весело
    print(ocenka.find('развлечения'))    # Выводится индекс слова развлечения    
if __name__ == "__main__":
    main()
