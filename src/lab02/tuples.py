def format_record(rec):
    fio, grp, gpa = rec
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA вне диапазона 0.0–5.0")
    parts = fio.split()
    fam = parts[0]
    ini = ""
    for p in parts[1:]:
        ini += p[0].upper() + "."
    return f"{fam} {ini}, гр. {grp}, GPA {gpa:.2f}"

s = eval(input())     
print(format_record(s))