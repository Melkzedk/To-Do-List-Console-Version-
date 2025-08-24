tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        print("\n📋 Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, task)
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("🗑️ Task deleted!")
        else:
            print("Invalid task number")
    elif choice == "4":
        break
