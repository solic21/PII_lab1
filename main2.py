import numpy as np
import skfuzzy as fuzz

# Дефініція наборів нечітких множин

headache = fuzz.trimf(np.arange(0, 10), [0, 2, 5])
fever = fuzz.trimf(np.arange(0, 10), [3, 6, 9])
cough = fuzz.trimf(np.arange(0, 10), [4, 7, 10])

# Введення даних від користувача

headache_level = float(input("Введіть рівень головного болю (від 0 до 10): "))
fever_level = float(input("Введіть рівень температури (від 0 до 10): "))
cough_level = float(input("Введіть рівень кашлю (від 0 до 10): "))

# Обчислення нечіткої оцінки

headache_membership = fuzz.membership(headache, headache_level)
fever_membership = fuzz.membership(fever, fever_level)
cough_membership = fuzz.membership(cough, cough_level)

# Обчислення нечіткої оцінки діагнозу

diagnosis = fuzz.and_or(headache_membership, fever_membership, cough_membership)

# Виведення результату

print("Нечітка оцінка діагнозу:", diagnosis)

# Класифікація діагнозу

if diagnosis > 0.8:
    print("Діагноз: грип")
elif diagnosis > 0.5:
    print("Діагноз: застуда")
else:
    print("Діагноз: не визначено")
