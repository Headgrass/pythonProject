# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_decode.txt', 'w') as data:
    data.write('HHHHOOOOMMMMEEEEWWWWOOOORRRRKKKKK')

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode_message(our_message):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

def display():
    with open('file_decode.txt', 'r') as data:
        our_message = data.readline()
    encoded_message = encode_message(our_message)
    with open('file_encode.txt', 'w') as file:
        file.write(encoded_message)
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message +"]")

display()
