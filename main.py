search_str=input("Введите строку для поиска")

with open('text.txt', 'r', encoding='utf-8') as file:
    lines=file.readlines()

matching_lines=[]
for line in lines:
    if search_str in line:
        matching_lines.append(line.strip())

print(f"\nКолво найденных строк: {len(matching_lines)}")

for line in matching_lines:
    print(line)

sorted_lines=sorted(matching_lines, key=len)

print("\n Отсортированные строки по длине: ")
for line in sorted_lines:
    print(line)