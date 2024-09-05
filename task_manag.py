import tkinter as tk

flg_run1 = False  # False - признак, что задача НЕ помечена; True - задача помечена
def add_task():    # Функция Добавления задачи
    task = task_entry.get()  # получаем слова из поля ввода
    if task:   #Если task существует - то есть, не пустой и не None
        task_listBox.insert(tk.END, task) # вставляем з-чу, назв. которуой ввели, в конец СПИСКА
                                      # tk.END - константа, указывает конец списка (в нашем случае),
                                      # и не только списка, а много чего
        task_entry.delete(0, tk.END)  #Очищаем поле для ввода!  С самого начала поля (0) и до конца

def delete_task():    # Функция Удаления задачи
    selected_task = task_listBox.curselection()   # метод получения ID (индекса) выбранного элемента из списка
                                                  # или из другого виджета
    if selected_task:
        task_listBox.delete(selected_task) # берем наш список и удаляем задачу по индексу, который хранится
                                           # в перменной selected_task

def mark_task():  # Отметить выполненную задачу
    global flg_run1 #даем понять, что хотим использовать и изменять глоб. переменную, а не создавать новую локальную
    selected_task = task_listBox.curselection()
    if selected_task and flg_run1 == False:
        task_listBox.itemconfig(selected_task, bg='sky blue')  #itemconfig - конфигурация(изменение) отдельных эл-тов в списке или холсте
        flg_run1 = True
    elif selected_task and flg_run1 == True:
        task_listBox.itemconfig(selected_task, bg='LightPink1')
        flg_run1 = False


root = tk.Tk()
root.title('Task list')
root.configure(background= 'IndianRed2')  #https://letpy.com/handbook/tkinter-colors/

text1 = tk.Label(root, text='Введите вашу задачу:', bg='IndianRed2')
text1.pack()

task_entry = tk.Entry(root, width=30, bg='DeepPink',fg='white')
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text = 'Добавить задачу', command = add_task)  #вызов функции по кнопке - обязательно без ()!!!
add_task_button.pack(pady=5)  #отступы по вертикали от соседних виджетов

delete_button = tk.Button(root,text = 'Удалить задачу', command = delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text='Отметить выполненную задачу', command = mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text='Список задач:', bg='IndianRed2')
text2.pack()

#Создадим список, в который м.б. добавлять все наши задачи - Listbox()
task_listBox = tk.Listbox(root, height=10, width=50, bg='LightPink1')
task_listBox.pack(pady=10)

root.mainloop()

