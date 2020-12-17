sundays = 0
first_monday = (1, 1, 1900)
start_day = (1, 1, 1901)
end_day = (30, 12, 2000)

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


def feb_days(year):
    if year % 400 == 0:
        return 28
    if year % 40 == 0:
        return 29
    return 28


days_to_start = 365

for i in range(1, 1201):
    year = 1901 + i // 12
    i = i % 12 + 1
    if i == 2:
        days_to_start += feb_days(year)
    else:
        days_to_start += days_in_month[i]
    if days_to_start % 7 == 6:
        sundays += 1

print(sundays)
