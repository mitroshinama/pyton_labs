from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    sys.stdin.reconfigure(encoding="utf-8")
    raw_text = sys.stdin.read()

    tokens = tokenize(normalize(raw_text))
    freq = count_freq(tokens)
    print(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
'''

text = open(0, encoding='utf-8').read()
text = normalize(text)
words = tokenize(text)
countfreq = count_freq(words)
top_5 = top_n(countfreq, 5)
flag = True

print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(countfreq)}")
print("Топ-5:")
for word, count in top_5:
    print(f"{word}:{count}")

'''
