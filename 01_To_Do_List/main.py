import json
from typing import List, Dict

TODO_FILE = "todo_list.json"

def load_tasks() -> List[Dict[str, str]]:
    """Загружает список задач из JSON-файла."""
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks: List[Dict[str, str]]) -> None:
    """Сохраняет список задач в JSON-файл."""
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def add_task(description: str) -> None:
    """Добавляет новую задачу."""
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "description": description, "done": False})
    save_tasks(tasks)
    print("Задача добавлена!")

def list_tasks() -> None:
    """Выводит список всех задач."""
    tasks = load_tasks()
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f"{task['id']}. {task['description']} {status}")

def complete_task(task_id: int) -> None:
    """Отмечает задачу как выполненную."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Задача выполнена!")
            return
    print("Задача не найдена.")

def delete_task(task_id: int) -> None:
    """Удаляет задачу по ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Задача удалена!")


if __name__ == "__main__":
    add_task("Купить молоко")
    add_task("Написать код")
    list_tasks()
    complete_task(1)
    list_tasks()
    delete_task(2)
    list_tasks()