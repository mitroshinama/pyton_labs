
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("data/lab04/input.txt") 
print("Прочитанный текст:", txt) # добавил print, чтобы вы видели результат
write_csv([("word","count"),("test",3)], "data/lab04/check.csv") 
