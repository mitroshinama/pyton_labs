def format_record(q):
    if not isinstance(q, tuple) or len(q) != 3:
        return "TypeError (в кортеже должно быть 3 элемента )"
    if not isinstance(q, tuple):
        raise TypeError("Должен быть кортеж")
    f, g, p = q
    if not isinstance(f, str) or not isinstance(g, str):
        return "TypeError (ФИО и группа должны быть строками)"
    if not isinstance(p, (int, float)):
        return "TypeError (GPA должен быть чеслом)"

    fio = " ".join(f.split()).split()
    gro = g.strip()

    if not fio:
        return "ValueError (ФИО не пустое)"
    if not gro:
        return "ValueError (группа не пустая)"
    if not (0.0 <= p <= 5.0):
        return "ValueError (GPA должен быть от 0.0 до 5.0)"

    
    s = fio[0].capitalize()
    i = ""
    for n in fio[1:]:
        if n:
            i += n[0].upper() + "."

    ps = "{:.2f}".format(p)
    res = s + " " + i + ", " + gro + ", GPA " + ps
    return res


print(f'''
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')

print('("Сидоров Иван Иванович", "BIVT-26", 8.1) ->', format_record(("Сидоров Иван Иванович", "BIVT-26", 8.1)))
print('("Ивахненко Анастасия Ивановна", "  ", 1.7) ->', format_record(("Ивахненко Анастасия Ивановна", "  ", 1.7)))
print('("Кузнецов Артем Иванович", "BBI-25", "12.5") ->', format_record(("Кузнецов Артем Иванович", "BBI-25", "12.5")))
