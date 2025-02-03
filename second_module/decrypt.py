def decrypt_message(encoded_string):
    result = []

    for i in range(len(encoded_string)):
        if encoded_string[i].isalpha() or encoded_string[i].isspace():
            # Если текущий символ является буквой или пробелом
            if i + 1 < len(encoded_string) and encoded_string[i + 1] == '.':
                # Если следующий символ — точка, добавляем текущую букву/пробел и пропускаем следующую итерацию
                result.append(encoded_string[i])
                i += 1
            elif i + 2 < len(encoded_string) and encoded_string[i + 1:i + 3] == '..':
                # Если следующие два символа — две точки, стираем последний добавленный символ и пропускаем две итерации
                if result:
                    result.pop()
                i += 2
            else:
                # Просто добавляем текущий символ, если нет точек сразу после него
                result.append(encoded_string[i])

    return ''.join(result)


print(decrypt_message('rwr..ffw'))