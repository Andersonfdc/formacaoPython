month = int(input())

months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if 1 <= month <= 12:
    month_name = months_dict[month]
    print(month_name)
else:
    print("Mês inválido. O valor deve estar entre 1 e 12.")