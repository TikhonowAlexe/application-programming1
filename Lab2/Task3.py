import sys

def decrypt(text):
    result = []
    i = 0
    while i < len(text):
        if text[i] == '.':
            i += 1  # Пропускаем одиночную точку
        elif i + 1 < len(text) and text[i + 1] == '.':
            if i + 2 < len(text) and text[i + 2] == '.':
                if result:
                    result.pop()
                i += 3
            else:
                result.append(text[i])
                i += 2
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    encrypted = sys.stdin.read().strip()
    print(decrypt(encrypted))
