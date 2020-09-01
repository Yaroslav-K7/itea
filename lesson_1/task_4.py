def bank(sum_dep, years, percent):
    for m in range(1, years + 1):
        sum_dep += sum_dep * percent * 0.01
    return round(sum_dep, 2)
