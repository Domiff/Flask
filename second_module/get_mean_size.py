import sys


def get_mean_size():
    # Чтение данных из стандартного ввода
    data = sys.stdin.read()

    # Преобразуем данные в список строк
    lines = data.split('\n')

    # Пропускаем первые две строки (заголовок и строку с информацией о директории)
    file_lines = lines[2:]

    total_size = 0
    num_files = 0

    for line in file_lines:
        parts = line.split()

        # Если строка пустая или начинается с 'd' (каталог), пропускаем её
        if not parts or parts[0].startswith('d'):
            continue

        try:
            size = int(parts[4])
            total_size += size
            num_files += 1
        except ValueError:
            pass  # Игнорируем строки, где не удается преобразовать размер в число

    if num_files == 0:
        return 0

    mean_size = total_size / num_files
    print(f"Средний размер файла: {mean_size:.2f}")


# Вызываем функцию при запуске скрипта
if __name__ == "__main__":
    get_mean_size()
