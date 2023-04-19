import pandas as pd

data = pd.read_csv("database/abalone.data", sep=",")


def chart(column_name, column_name2):
    pass  # To znaczy, że kod zostanie dodany później


# Średnia
def mean_value(column_name):
    return data[column_name].mean()


# Odchylenie standardowe
def std_value(column_name):
    return data[column_name].std()


# Mediana
def median_value(column_name):
    return data[column_name].median()


# Min
def min_value(column_name):
    return data[column_name].min()


# Max
def max_value(column_name):
    return data[column_name].max()


# Moda
def mode_value(column_name):
    return data[column_name].mode()


# Korelacja między dwoma podanymi kolumnami // Trzeba sprawdzić jak to w ogóle działa
def correlation(column_name1, columne_name2):
    return data[column_name1].corr(data[columne_name2])

# Podstawowe dane statystyczne:
# - średnia
# - wartość min
# - wartość max
# - wariancja
# - odchylenie standardowe
# - moda
# - mediana
