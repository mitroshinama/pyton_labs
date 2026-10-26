import sys
from lib.text import normalize, tokenize, count_freq, top_n
def main():
    t = sys.stdin.read()
    if not t.strip():
        print("Введен пустой текст.")
        return
    normalized_text = normalize(t)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for w, c in top_n(freq, 5):
        print(f"{w}:{c}")
if __name__ == "__main__":
    main()