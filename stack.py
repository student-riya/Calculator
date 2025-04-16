class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Pop an item from the stack. Returns None if stack is empty."""
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


# Taking user input for stack operations
stack = Stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Check if empty")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print(f"Popped item: {popped_item}")
    elif choice == '3':
        print("Is stack empty?", stack.is_empty())
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
