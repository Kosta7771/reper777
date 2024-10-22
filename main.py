import pandas as pd
import numpy as np
in in
# Чтение Excel файла
file_path = 'expert_opinion.xlsx'
df = pd.read_excel(file_path, index_col=0)

# Исключаем итоговую строку из расчетов
df_clean = df.drop('Итог')

# 1. Метод суммы рангов
# Присваиваем ранги для каждого эксперта (строки без итогов)
ranks_corrected = df_clean.rank(ascending=False)

# Суммируем ранги по строкам
sum_ranks_corrected = ranks_corrected.sum(axis=1)

# Коэффициент весомости для метода суммы рангов
weights_sum_rank_corrected = sum_ranks_corrected / sum_ranks_corrected.sum()

# 2. Метод медианы рангов
median_ranks_corrected = ranks_corrected.median(axis=1)

# Коэффициент весомости для метода медианы рангов
weights_median_rank_corrected = median_ranks_corrected / median_ranks_corrected.sum()

# 3. Построение ряда неубывания (не возрастания)
sorted_df_non_decreasing = df_clean.apply(sorted, axis=1)  # Ряд неубывания
sorted_df_non_increasing = df_clean.apply(lambda x: sorted(x, reverse=True), axis=1)  # Ряд невозрастания

# Объединяем результаты в один DataFrame
results = pd.DataFrame({
    'Сумма рангов': sum_ranks_corrected,
    'Коэффициент (сумма рангов)': weights_sum_rank_corrected,
    'Медиана рангов': median_ranks_corrected,
    'Коэффициент (медиана рангов)': weights_median_rank_corrected
})

# Выводим результаты
print("Результаты расчетов:")
print(results)

print("\nРяд неубывания:")
print(sorted_df_non_decreasing)

print("\nРяд невозрастания:")
print(sorted_df_non_increasing)
