import math
import re


def get_summary_rss(file_path):

    # Регулярное выражение для преобразования числа в человекочитаемый вид
    def human_readable_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        return f"Размер потребляемой памяти {round((size_bytes / 1024) / 1024)} MB"

    total_memory = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Найдем значение в колонке RSS (обычно она идет после PID)
            rss_match = re.search(r'\d+\s+(\d+)\s+', line)
            if rss_match:
                memory_usage = int(rss_match.group(1))
                total_memory += memory_usage

    return human_readable_size(total_memory)


path_file = 'output_file.txt'
result = get_summary_rss(path_file)
print(result)

