def format_record(rec: tuple[str, str, float]) -> str:              
    if len(rec) != 3:
        raise ValueError('в кортеже должно быть 3 элемента')
    if len(rec[0].strip().split()) != 3 and len(rec[0].strip().split()) != 2:
        raise ValueError('не полное ФИО')
    if not len(rec[1].strip()):
        raise ValueError('группа не может быть пустой')

    if not isinstance(rec, tuple):
        raise TypeError('должен быть кортеж')
    if not isinstance(rec[0], str):
        raise TypeError('имя должно быть строкой')
    if not isinstance(rec[1], str):
        raise TypeError('группа должна быть строкой')
    if not isinstance(rec[2], (float, int)):
        raise TypeError('оценка должна быть числом')
    ff = 0
    name = []
    for w in rec[0].strip('" ').split():
        w = w.strip()
        if len(w) and ff:
            name.append(w[0].capitalize() + '.')
            ff = 1

        if len(w) and not (ff):
            name.append(w[0].capitalize() + w[1:] + ' ')
            ff = 1

    return f"{''.join(name)}, гр. {rec[1]}, GPA {rec[2]:.2f}"



print(f'''
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')

print(f'([Иванов Иван Иванович], "IKBO-12", 4.6) -> {format_record(([Иванов, Иван, Иванович], "IKBO-12", 4.6))}')