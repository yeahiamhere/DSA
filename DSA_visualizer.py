import tkinter as tk
from tkinter import ttk
import random

# --- Node and BST Implementation ---
class Node:
    """Represents a node in the Binary Search Tree (BST)."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree (BST) class."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper function to insert a value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """Helper function to delete a value from the BST."""
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        """Get the node with the minimum value."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Return the inorder traversal of the tree."""
        return self._inorder(self.root)

    def _inorder(self, node):
        """Helper function for inorder traversal."""
        return self._inorder(node.left) + [node.value] + self._inorder(node.right) if node else []

    def draw(self, canvas, node=None, x=400, y=50, level=0):
        """Draw the BST on the canvas."""
        if node is None:
            node = self.root

        if node is not None:
            # Draw the node
            canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#3498db", outline="#2980b9", width=2)
            canvas.create_text(x, y, text=str(node.value), fill="white", font=("Arial", 12))

            # Draw the left and right branches
            if node.left:
                canvas.create_line(x, y, x - 100, y + 50, fill="#2980b9", width=2)
                self.draw(canvas, node.left, x - 100, y + 50, level + 1)

            if node.right:
                canvas.create_line(x, y, x + 100, y + 50, fill="#2980b9", width=2)
                self.draw(canvas, node.right, x + 100, y + 50, level + 1)

# --- Stack Visualization ---
class Stack:
    """Visualize Stack with bars."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if self.items:
            return self.items.pop()

    def draw(self, canvas):
        """Draw the stack on the canvas."""
        bar_width = 30
        bar_gap = 10
        y_pos = 300
        for i, item in enumerate(reversed(self.items)):
            canvas.create_rectangle(100 + i * (bar_width + bar_gap), y_pos - 20,
                                    100 + (i + 1) * (bar_width + bar_gap), y_pos + 20,
                                    fill="#3498db", outline="#2980b9")
            canvas.create_text(100 + (i + 0.5) * (bar_width + bar_gap), y_pos, text=str(item), fill="white", font=("Arial", 12))

# --- Queue Visualization ---
class Queue:
    """Visualize Queue with bars."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove an item from the queue."""
        if self.items:
            return self.items.pop(0)

    def draw(self, canvas):
        """Draw the queue on the canvas."""
        bar_width = 30
        bar_gap = 10
        y_pos = 300
        for i, item in enumerate(self.items):
            canvas.create_rectangle(100 + i * (bar_width + bar_gap), y_pos - 20,
                                    100 + (i + 1) * (bar_width + bar_gap), y_pos + 20,
                                    fill="#3498db", outline="#2980b9")
            canvas.create_text(100 + (i + 0.5) * (bar_width + bar_gap), y_pos, text=str(item), fill="white", font=("Arial", 12))

# --- Main Visualization Application ---
class DataStructureVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Data Structure Visualizer")

        # Color Palette
        self.bg_color = "#ecf0f1"
        self.primary_color = "#3498db"
        self.secondary_color = "#2980b9"
        self.button_color = "#2ecc71"
        self.button_hover_color = "#27ae60"
        self.text_color = "#2c3e50"
        self.font_style = ("Helvetica", 12)

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left canvas for drawing structures
        self.canvas_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Control panel (right side)
        self.control_panel = tk.Frame(self.main_frame, bg=self.bg_color, width=250, padx=20, pady=20)
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)

        # Data structures
        self.bst = BST()
        self.stack = Stack()
        self.queue = Queue()

        # Current structure
        self.current_structure = "BST"  # Default

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange UI components."""
        # Structure Selector Dropdown
        self.structure_selector_label = tk.Label(self.control_panel, text="Select Data Structure", bg=self.bg_color, font=("Helvetica", 14, "bold"), fg=self.text_color)
        self.structure_selector_label.pack(pady=15)

        self.structure_selector = tk.StringVar(value="BST")
        self.structure_menu = tk.OptionMenu(self.control_panel, self.structure_selector, "BST", "Stack", "Queue", command=self.toggle_structure)
        self.structure_menu.config(font=self.font_style, width=18, relief="flat", highlightthickness=0)
        self.structure_menu.pack(pady=5)

        # Buttons for operations
        self.operation_frame = tk.Frame(self.control_panel, bg=self.bg_color)
        self.operation_frame.pack(pady=20)

        self.insert_button = self.create_button(self.operation_frame, "Insert", self.insert)
        self.insert_button.grid(row=0, column=0, padx=10, pady=10)

        self.delete_button = self.create_button(self.operation_frame, "Delete", self.delete)
        self.delete_button.grid(row=1, column=0, padx=10, pady=10)

        self.show_button = self.create_button(self.operation_frame, "Show Structure", self.show_structure)
        self.show_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = self.create_button(self.operation_frame, "Clear", self.clear_canvas)
        self.clear_button.grid(row=3, column=0, padx=10, pady=10)

        # Status label for feedback
        self.status_label = tk.Label(self.control_panel, text="Ready to start", bg=self.bg_color, font=self.font_style, fg=self.text_color)
        self.status_label.pack(pady=20)

    def create_button(self, parent, text, command):
        """Helper function to create a styled button with hover effects."""
        button = tk.Button(parent, text=text, command=command, font=self.font_style, fg="white", bg=self.button_color, relief="flat", width=20, height=2, borderwidth=0)
        button.bind("<Enter>", lambda event, btn=button: self.on_hover(event, btn))
        button.bind("<Leave>", lambda event, btn=button: self.on_leave(event, btn))
        button.config(activebackground=self.button_color, activeforeground="white")
        return button

    def on_hover(self, event, button):
        """Handle hover effect for buttons."""
        button.config(bg=self.button_hover_color)

    def on_leave(self, event, button):
        """Reset button color when hover ends."""
        button.config(bg=self.button_color)

    def toggle_structure(self, structure):
        """Switch between data structures."""
        self.current_structure = structure
        self.clear_canvas()
        self.status_label.config(text=f"Switched to {structure}", fg=self.text_color)

    def insert(self):
        """Insert a node depending on the selected structure."""
        if self.current_structure == "BST":
            value = random.randint(1, 100)
            self.bst.insert(value)
            self.status_label.config(text=f"Inserted {value} into BST", fg=self.button_color)
            self.show_structure()
        elif self.current_structure == "Stack":
            value = random.randint(1, 100)
            self.stack.push(value)
            self.status_label.config(text=f"Pushed {value} onto Stack", fg=self.button_color)
            self.show_structure()
        elif self.current_structure == "Queue":
            value = random.randint(1, 100)
            self.queue.enqueue(value)
            self.status_label.config(text=f"Enqueued {value} into Queue", fg=self.button_color)
            self.show_structure()

    def delete(self):
        """Delete a node depending on the selected structure."""
        if self.current_structure == "BST":
            if self.bst.root:
                value = random.choice(self.bst.inorder())
                self.bst.delete(value)
                self.status_label.config(text=f"Deleted {value} from BST", fg=self.button_color)
                self.show_structure()

    def show_structure(self):
        """Display the current data structure."""
        self.clear_canvas()

        if self.current_structure == "BST":
            self.bst.draw(self.canvas)
        elif self.current_structure == "Stack":
            self.stack.draw(self.canvas)
        elif self.current_structure == "Queue":
            self.queue.draw(self.canvas)

    def clear_canvas(self):
        """Clear the canvas for a fresh drawing."""
        self.canvas.delete("all")
        self.status_label.config(text="Ready to start", fg=self.text_color)

# --- Main Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructureVisualizer(root)
    root.mainloop()
