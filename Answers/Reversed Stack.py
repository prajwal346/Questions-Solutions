class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def reverse_stack(stack):
    if stack.is_empty():
        return
    # Pop the top element
    top = stack.pop()
    # Reverse the remaining stack
    reverse_stack(stack)
    # Insert the popped element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        # Pop all items
        temp = stack.pop()
        # Insert the item at the bottom
        insert_at_bottom(stack, item)
        # Push the popped items back
        stack.push(temp)

# Example usage:
if __name__ == "__main__":
    s = Stack()
    for i in range(1, 6):
        s.push(i)
    
    print("Original stack:", s)
    reverse_stack(s)
    print("Reversed stack:", s)
