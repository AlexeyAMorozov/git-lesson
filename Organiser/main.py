import sys

from organizer import storage

conn = storage.connect()
storage.initialize(conn)


def action_show_menu():
    print('''
		Ежедневник.
   Выберите действие:
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
m. Показать меню
q. Выйти''')


def action_exit():
    conn.close()
    sys.exit(0)


def action_all_tasks():
    all_tasks = storage.all_tasks(conn)
    for task in all_tasks:
        print('{task[name]} - task[text]} - {task[planned]} - {task[status]}'.format(task=task))


def action_add_task():
    task_name = input('Название задачи:\n')
    task_date = input('Дата выполнения:\n')
    text = input('Текст задачи:\n')
    storage.add_task(conn, task_name, task_date, text)

def action_update_task():
    idx = input('\nid задачи: ')
    task = storage.find_by_id(conn, idx)
    print('Название: {task[task_name]}; Дата: {task[task_date]}; Текст: {task[text]}'.format(task=task))
    task_name = input('\nНовое название задачи:')
    task_date = input('\nНовая дата выполнения:')
    text = input('Новый текст задачи:\n')
    storage.update_task(conn, task_name, task_date, text, idx)

def action_close_task():
    act = input('id: ')
    storage.close_task(conn, act)




actions = {
    '1': action_all_tasks,
    '2': action_add_task,
    '3': action_update_task,
    '4': action_close_task,
     'm': action_show_menu,
    'q': action_exit
}

if __name__ == '__main__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')