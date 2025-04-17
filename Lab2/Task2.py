import sys

def get_mean_size():
    lines = sys.stdin.readlines()[1:]  # Пропускаем заголовок
    sizes = []

    for line in lines:
        parts = line.split()
        if len(parts) < 5 or parts[0].startswith('d'):
            continue  # Пропускаем директории
        try:
            sizes.append(int(parts[4]))
        except ValueError:
            continue

    if not sizes:
        return 0
    return sum(sizes) // len(sizes)

if __name__ == '__main__':
    print(get_mean_size())
