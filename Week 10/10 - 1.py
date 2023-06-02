def sum_series_n_minus_1(n):
    if n <= 1:
        return n
    else:
        return 1/n + sum_series_n_minus_1(n-1)

print(sum_series_n_minus_1(7))