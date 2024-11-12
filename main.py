search_str=input("Введите строку для поиска") #инициализация переменной, которая будет содержать строку для поиска

with open('text.txt', 'r', encoding='utf-8') as file:#открытие файла для чтения
    lines=file.readlines()

matching_lines=[]#инициализация переменной 
for line in lines:#цикл for для перебора
    if search_str in line:#оператор if для поиска подхождений
        matching_lines.append(line.strip())

print(f"\nКолво найденных строк: {len(matching_lines)}")#вывод кол-ва найденных строк

for line in matching_lines:#цикл for для вывода line
    print(line)#вывод line

sorted_lines=sorted(matching_lines, key=len)#сортировка по длинне

print("\n Отсортированные строки по длине: ")#вывод строк
for line in sorted_lines:#цикл for для вывода
    print(line)#вывод строк
