#this is for test
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False  # Прапор для перевірки, чи відбулись обміни
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Обмін елементів
                swapped = True
        if not swapped:  # Якщо не було обмінів, масив вже відсортований
            break
    return array


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i  # Індекс мінімального елемента
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j  # Знаходимо новий мінімальний елемент
        array[i], array[min_index] = array[min_index], array[i]  # Обмін елементів
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key_value = array[i]  # Елемент для вставки
        j = i - 1
        while j >= 0 and array[j] > key_value:
            array[j + 1] = array[j]  # Переміщуємо елементи, більші за key_value, вправо
            j -= 1
        array[j + 1] = key_value  # Вставляємо key_value в правильну позицію
    return array


# Приклад використання:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]

    print("Бульбашкове сортування:", bubble_sort(sample_array.copy()))
    print("Сортування вибором:", selection_sort(sample_array.copy()))
    print("Сортування вставкою:", insertion_sort(sample_array.copy()))