from sort import sort

'''
Задание: сортировка заказов интернет-магазина.
1. По цене по возрастанию
2. По цене по убыванию
3. По дате от новых к старым
4. Сначала по статусу (по алфавиту), затем по цене (по возрастанию)

Ответ: все четыре пункта выполнимы быстрой сортировкой. Пункт 4 — только
одним проходом через составной компаратор (by=["status","price"]), потому что
быстрая сортировка нестабильна и подход "сортировать дважды" сломается.
'''


def print_orders(arr, title=""):
    if title:
        print(title)
    for o in arr:
        print(f'  #{o["id"]}  {o["price"]:>6}  {o["date"]}  {o["status"]}')
    print()


if __name__ == "__main__":
    orders = [
        {"id": 101, "price": 5300, "date": "2024-10-01", "status": "paid"},
        {"id": 102, "price": 1200, "date": "2024-01-09", "status": "new"},
        {"id": 103, "price": 7800, "date": "2024-09-01", "status": "paid"},
        {"id": 104, "price": 9900, "date": "2024-10-02", "status": "cancelled"},
    ]

    print_orders(orders, "Исходный список:")
    print_orders(sort([dict(o) for o in orders], "price"), "1) Цена по возрастанию:")
    print_orders(sort([dict(o) for o in orders], "price", reverse=True), "2) Цена по убыванию:")
    print_orders(sort([dict(o) for o in orders], "date", reverse=True), "3) Дата (новые -> старые):")
    print_orders(sort([dict(o) for o in orders], ["status", "price"]), "4) Статус, затем цена (quick):")

    # Тот же результат другим алгоритмом — меняется только algo:
    print_orders(sort([dict(o) for o in orders], ["status", "price"], algo="insert"),
                 "4') То же самое сортировкой вставками:")
