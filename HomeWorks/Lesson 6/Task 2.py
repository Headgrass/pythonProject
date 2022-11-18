text = str(input("Введите математическое выражение: "))
list = list(text.replace(" ", ""))
print(list)

for i in range(len(list)):
    if list[i] == "*":
        temp_result = int(list[i-1]) * int(list[i+1])
        list[i] = temp_result
    if list[i] == "/":
        temp_result2 = int(list[i-1]) / int(list[i+1])
        list[i] = temp_result2

print(list)