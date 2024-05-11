#Задача: Создай класс Task, который позволяет управлять задачами
#(делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и
#статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
#отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    tasks = []

    def __init__(self, description, deadline, status="не выполнено"):
        self.description = description
        self.deadline = deadline
        self.status = status
        Task.tasks.append(self)

    def mark_task(self):
        self.status = "выполнено"
        print(f'\nЗадача "{self.description}" выполнена!\n')

    @classmethod
    def get_current_tasks(cls):
        current_tasks = [task for task in cls.tasks if task.status == "не выполнено"]
        return current_tasks


# Пример использования
task1 = Task("Сделать уроки      ", "2024-05-12")
task2 = Task("Сделать презентацию", "2024-05-12")
task3 = Task("Поставить будильник", "2024-05-11")

current_tasks = Task.get_current_tasks()
print("Текущие не выполненные задачи:")
for task in current_tasks:
     print(f"   {task.description} до {task.deadline}")


task1.mark_task()

current_tasks = Task.get_current_tasks()
print("Оставшиеся не выполненные задачи:")
for task in current_tasks:
    print(f"   {task.description} до {task.deadline}")