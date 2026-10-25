import re
def normalize(t, *, casefold=True, yo2e=True):
    if yo2e:
        t = t.replace('ё', 'е').replace('Ё', 'Е')
    t = t.casefold() if casefold else t.lower()
    t = re.sub(r'\s+', ' ', t)
    return t.strip()


def tokenize(t: str):
    return re.findall(r"\w+(?:-\w+)*", t)

def count_freq(tokens: list[str]):
    m = dict()
    for i in range(len(set(tokens))):
        m[sorted(list(set(tokens)))[i]] = tokens.count(sorted(list(set(tokens)))[i])
    return m

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


if __name__ == '__main__':
    print('normalize')
    print(f'  "привет\\nмир\\t" → {repr(normalize("привет\nмир\t"))} (casefold + схлопнуть пробелы)')
    print(f'  "ёжик, Ёлка" (yo2e=True) → {repr(normalize("ёжик, Ёлка", yo2e=True))}')
    print(f'  "Hello\\r\\nworld" → {repr(normalize("Hello\r\nworld"))}')
    print(f'  "  двойные  пробелы  " → {repr(normalize("  двойные  пробелы  "))}')

    print('tokenize')
    print(f'  "привет мир" → {tokenize("привет мир")}')
    print(f'  "hello,world!!!" → {tokenize("hello,world!!!")}')
    print(f'  "по-настоящему круто" → {tokenize("по-настоящему круто")}')
    print(f'  "2025 год" → {tokenize("2025 год")}')
    print(f'  "emoji 😊 не слово" → {tokenize("emoji 😊 не слово")} (эмодзи выпадают)')

    print('count_freq + top_n')
    t = ['a', 'b', 'a', 'c', 'b', 'a']
    f = count_freq(t)
    r = top_n(f, 2)
    print(f'  Токены {t} → частоты {f};')
    print(f'  top_n(..., n=2) → {r}')

    t = ['bb', 'aa', 'bb', 'aa', 'cc']
    f = count_freq(t)
    r = top_n(f, 2)
    print(f'  При равенстве частот: токены {t} → частоты {f};')
    print(f'  top_n(..., n=2) → {r} (алфавитная сортировка при равенстве).')