class Queue:
    def __init__(self):
        self.items = []  # List to store queue elements

    def is_empty(self):
        return self.items == []  # Check if queue is empty

    def enqueue(self, e):
        self.items.append(e)  # Add element to the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the first element
        else:
            return "Queue is empty"

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.items)


# Main program to take user input
q = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check if Queue is empty")
    print("4. Display Queue")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = input("Enter element to add: ")
        q.enqueue(element)
        print(f"{element} added to the queue")
    elif choice == 2:
        print("Dequeued element:", q.dequeue())
    elif choice == 3:
        print("Is queue empty?", q.is_empty())
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
