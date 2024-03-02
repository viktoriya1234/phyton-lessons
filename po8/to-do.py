user_list = []

file = open('list.txt', 'r')
for i in file.readlines():
    s = i.strip()
    user_list.append(s)

while True:
    print('## LIST ##')
    print("1. Add Task\n2. Edit Task\n3. Delete Task\n4. Show list\n5. Exit")

    action = int(input(': '))
    if action == 5:
        file = open('list.txt', 'w')
        for i in user_list:
            file.write('%s\n' % i)
        break
    elif action == 1:
        task = input('Input task: ')
        user_list.append(task)
    elif action == 4:
        i = 0
        for item in user_list:
            print(i, ': ', item)
            i += 1
    elif action == 3:
        delete_index = int(input('Input: '))
        # user_list.remove(delete_index)
        del user_list[delete_index]
    elif action == 2:
        edit_index = int(input('Input: '))
        new_task = input("new task: ")
        user_list[edit_index] = new_task

