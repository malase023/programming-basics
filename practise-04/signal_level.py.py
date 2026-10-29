signal = int(input("Введіть інтенсивність сигналу (0–100): "))

if signal < 20:
    level = "Слабкий сигнал"
elif signal < 60:
    level = "Робочий діапазон"
elif signal < 95:
    level = "Сильний сигнал"
else:
    level = "Насичення фотоприймача"

mode = "Потрібна увага" if signal < 20 or signal >= 95 else "Звичайний режим"

print("Рівень сигналу:", level)
print("Режим:", mode)