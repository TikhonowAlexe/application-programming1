import sys

def get_summary_rss(file_path):
    total_rss = 0
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]  # Пропускаем заголовок
        for line in lines:
            columns = line.split()
            if len(columns) > 5:
                try:
                    total_rss += int(columns[5])  # Столбец RSS
                except ValueError:
                    continue
    return format_size(total_rss * 1024)  # Переводим из КБ в байты

def format_size(size_bytes):
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024.0
        index += 1
    return f"{size_bytes:.2f} {units[index]}"

if __name__ == '__main__':
    path_to_file = 'output.txt'
    result = get_summary_rss(path_to_file)
    print(result)
