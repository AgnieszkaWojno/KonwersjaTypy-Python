def convert_to_bin (digit):
    w = []
    while digit>0:
        w = [digit % 2] + w  # % - reszta z dzielenia
        digit //= 2  #część całkowita
    return w
print("liczba binarna 125=",convert_to_bin(125))
