month = 4
day = 5

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Dia de semana em Abril")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("Dia de semana em Maio")
    case _:
        print("Nem um dia")