### Результати

```
Array Size: 1,000 - - - - - - - -

Data Type: random
Insertion Sort: 0.013109 seconds
Merge Sort: 0.001024 seconds
Timsort: 0.000096 seconds

Data Type: sorted
Insertion Sort: 0.000064 seconds
Merge Sort: 0.000825 seconds
Timsort: 0.000004 seconds

Data Type: reversed
Insertion Sort: 0.021523 seconds
Merge Sort: 0.000731 seconds
Timsort: 0.000005 seconds


Array Size: 5,000 - - - - - - - -

Data Type: random
Insertion Sort: 0.257353 seconds
Merge Sort: 0.004877 seconds
Timsort: 0.000358 seconds

Data Type: sorted
Insertion Sort: 0.000250 seconds
Merge Sort: 0.003815 seconds
Timsort: 0.000024 seconds

Data Type: reversed
Insertion Sort: 0.501570 seconds
Merge Sort: 0.004098 seconds
Timsort: 0.000040 seconds


Array Size: 10,000 - - - - - - - -

Data Type: random
Insertion Sort: 1.051659 seconds
Merge Sort: 0.011221 seconds
Timsort: 0.000849 seconds

Data Type: sorted
Insertion Sort: 0.000515 seconds
Merge Sort: 0.009033 seconds
Timsort: 0.000049 seconds

Data Type: reversed
Insertion Sort: 2.058507 seconds
Merge Sort: 0.008479 seconds
Timsort: 0.000053 seconds


Array Size: 50,000 - - - - - - - -

Data Type: random
Insertion Sort: 26.482961 seconds
Merge Sort: 0.064633 seconds
Timsort: 0.004703 seconds

Data Type: sorted
Insertion Sort: 0.002653 seconds
Merge Sort: 0.049556 seconds
Timsort: 0.000202 seconds

Data Type: reversed
Insertion Sort: 51.822619 seconds
Merge Sort: 0.049393 seconds
Timsort: 0.000175 seconds


Array Size: 100,000 - - - - - - - -

Data Type: random
Insertion Sort: 105.327978 seconds
Merge Sort: 0.133883 seconds
Timsort: 0.009790 seconds

Data Type: sorted
Insertion Sort: 0.004989 seconds
Merge Sort: 0.105267 seconds
Timsort: 0.000381 seconds

Data Type: reversed
Insertion Sort: 208.258041 seconds
Merge Sort: 0.109535 seconds
Timsort: 0.000402 seconds
```

### Аналіз результатів

- Insertion Sort демонструє погану продуктивність на великих та невідсортованих масивах через квадратичну складність O(n²). Однак на відсортованих масивах алгоритм працює дуже швидко.
- Merge Sort має стабільну складність `O(n log n)` і демонструє хорошу продуктивність незалежно від упорядкованості даних.
- Timsort перевершує інші алгоритми завдяки оптимізації для реальних даних та використанню сортування вставками на малих підмасивах. Він особливо швидкий на відсортованих та частково відсортованих даних.

### Висновки

Емпіричні дані підтверджують теоретичні оцінки складності алгоритмів:

- Сортування вставками не підходить для великих невідсортованих масивів, але дуже ефективне на малих або майже відсортованих даних.
- Сортування злиттям стабільне та ефективне, але може бути повільнішим через рекурсію та додаткову пам’ять.
- Timsort поєднує переваги обох алгоритмів, забезпечуючи швидке сортування на реальних даних.

Поєднання сортування злиттям та вставками робить Timsort набагато ефективнішим для широкого спектра задач сортування. Це пояснює, чому програмісти зазвичай використовують вбудовані в Python функції сортування, замість реалізації власних алгоритмів.
