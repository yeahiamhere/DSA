import tkinter as tk
from tkinter import ttk
import random
import math

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

    def draw(self, canvas, node=None, x=400, y=100, level=0, colors=None):
        """Draw the BST on the canvas with arrows."""
        if node is None:
            node = self.root
            # Draw BST title
            canvas.create_text(
                400, 50,
                text="Binary Search Tree Visualization",
                fill=colors['primary'] if colors else "#6c5ce7",
                font=("Segoe UI", 24, "bold")
            )

        if node is not None:
            # Node shadow effect
            canvas.create_oval(
                x - 23, y - 23, x + 27, y + 27,
                fill="#dfe6e9",
                outline=""
            )
            
            # Node circle with gradient effect
            canvas.create_oval(
                x - 25, y - 25, x + 25, y + 25,
                fill=colors['primary'] if colors else "#6c5ce7",
                outline=colors['secondary'] if colors else "#a8a5e6",
                width=2
            )
            
            # Node value
            canvas.create_text(
                x, y,
                text=str(node.value),
                fill="white",
                font=("Segoe UI", 12, "bold")
            )

            # Draw arrows instead of lines
            if node.left:
                self.draw_arrow(canvas, x, y, x - 100, y + 50, colors)
                self.draw(canvas, node.left, x - 100, y + 50, level + 1, colors)

            if node.right:
                self.draw_arrow(canvas, x, y, x + 100, y + 50, colors)
                self.draw(canvas, node.right, x + 100, y + 50, level + 1, colors)

    def draw_arrow(self, canvas, x1, y1, x2, y2, colors):
        """Draw an arrow between two points."""
        # Calculate arrow head points
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_length = 15
        arrow_angle = math.pi / 6  # 30 degrees
        
        # Arrow head points
        ax1 = x2 - arrow_length * math.cos(angle - arrow_angle)
        ay1 = y2 - arrow_length * math.sin(angle - arrow_angle)
        ax2 = x2 - arrow_length * math.cos(angle + arrow_angle)
        ay2 = y2 - arrow_length * math.sin(angle + arrow_angle)
        
        # Draw arrow line with gradient effect
        canvas.create_line(
            x1, y1, x2, y2,
            fill=colors['secondary'] if colors else "#a8a5e6",
            width=2,
            smooth=True
        )
        
        # Draw arrow head
        canvas.create_polygon(
            x2, y2, ax1, ay1, ax2, ay2,
            fill=colors['secondary'] if colors else "#a8a5e6",
            outline=colors['secondary'] if colors else "#a8a5e6"
        )

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

    def draw(self, canvas, colors=None):
        """Draw the stack on the canvas."""
        bar_width = 60
        bar_gap = 15
        y_pos = 300
        
        # Draw stack base shadow
        canvas.create_rectangle(
            52, y_pos + 32,
            752, y_pos + 42,
            fill="#dfe6e9",
            outline=""
        )
        
        # Draw stack base
        canvas.create_rectangle(
            50, y_pos + 30,
            750, y_pos + 40,
            fill=colors['secondary'] if colors else "#686de0",
            outline=colors['primary'] if colors else "#4834d4",
            width=2
        )
        
        # Draw stack title
        canvas.create_text(
            400, 50,
            text="Stack Visualization",
            fill=colors['primary'] if colors else "#4834d4",
            font=("Segoe UI", 24, "bold")
        )
        
        for i, item in enumerate(reversed(self.items)):
            # Draw shadow
            canvas.create_rectangle(
                102 + i * (bar_width + bar_gap),
                y_pos - 23,
                102 + (i + 1) * bar_width + i * bar_gap,
                y_pos + 27,
                fill="#dfe6e9",
                outline=""
            )
            
            # Draw stack element
            canvas.create_rectangle(
                100 + i * (bar_width + bar_gap),
                y_pos - 25,
                100 + (i + 1) * bar_width + i * bar_gap,
                y_pos + 25,
                fill=colors['primary'] if colors else "#4834d4",
                outline=colors['secondary'] if colors else "#686de0",
                width=2
            )
            canvas.create_text(
                100 + (i + 0.5) * bar_width + i * bar_gap,
                y_pos,
                text=str(item),
                fill="white",
                font=("Segoe UI", 12, "bold")
            )

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

    def draw(self, canvas, colors=None):
        """Draw the queue on the canvas."""
        bar_width = 60
        bar_gap = 15
        y_pos = 300
        
        # Draw queue base shadow
        canvas.create_rectangle(
            52, y_pos + 32,
            752, y_pos + 42,
            fill="#dfe6e9",
            outline=""
        )
        
        # Draw queue base
        canvas.create_rectangle(
            50, y_pos + 30,
            750, y_pos + 40,
            fill=colors['secondary'] if colors else "#686de0",
            outline=colors['primary'] if colors else "#4834d4",
            width=2
        )
        
        # Draw queue title
        canvas.create_text(
            400, 50,
            text="Queue Visualization",
            fill=colors['primary'] if colors else "#4834d4",
            font=("Segoe UI", 24, "bold")
        )
        
        for i, item in enumerate(self.items):
            # Draw shadow
            canvas.create_rectangle(
                102 + i * (bar_width + bar_gap),
                y_pos - 23,
                102 + (i + 1) * bar_width + i * bar_gap,
                y_pos + 27,
                fill="#dfe6e9",
                outline=""
            )
            
            # Draw queue element
            canvas.create_rectangle(
                100 + i * (bar_width + bar_gap),
                y_pos - 25,
                100 + (i + 1) * bar_width + i * bar_gap,
                y_pos + 25,
                fill=colors['primary'] if colors else "#4834d4",
                outline=colors['secondary'] if colors else "#686de0",
                width=2
            )
            canvas.create_text(
                100 + (i + 0.5) * bar_width + i * bar_gap,
                y_pos,
                text=str(item),
                fill="white",
                font=("Segoe UI", 12, "bold")
            )

# --- Main Visualization Application ---
class DataStructureVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Data Structure Visualizer")
        
        # Enhanced Modern Color Palette with Gradients
        self.bg_color = "#f8f9fe"  # Lighter background
        self.primary_color = "#6c5ce7"  # Vibrant purple
        self.secondary_color = "#a8a5e6"  # Soft purple
        self.accent_color = "#00cec9"  # Mint
        self.button_gradient = ["#6c5ce7", "#8171e5"]  # Button gradient
        self.button_hover_gradient = ["#8171e5", "#9085e4"]  # Hover gradient
        self.text_color = "#2d3436"  # Darker gray
        self.error_color = "#ff7675"  # Soft red
        self.success_color = "#00b894"  # Soft green
        self.font_style = ("Segoe UI", 11)
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        self.root.geometry("1300x800")
        
        # Create style for rounded Combobox
        self.style = ttk.Style()
        self.style.theme_create("rounded", parent="alt", settings={
            "TCombobox": {
                "configure": {
                    "selectbackground": self.primary_color,
                    "fieldbackground": "white",
                    "background": "white",
                    "padding": 5
                }
            }
        })
        self.style.theme_use("rounded")
        
        # Main Frame with shadow effect
        self.main_frame = tk.Frame(
            self.root,
            bg=self.bg_color,
            padx=20,
            pady=20
        )
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create widgets with enhanced styling
        self.create_canvas_frame()
        self.create_control_panel()
        
        # Initialize data structures
        self.bst = BST()
        self.stack = Stack()
        self.queue = Queue()
        self.current_structure = "BST"

    def create_canvas_frame(self):
        """Create enhanced canvas frame with shadow effect"""
        self.canvas_frame = tk.Frame(
            self.main_frame,
            bg=self.bg_color
        )
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # Canvas container with shadow and rounded corners
        self.canvas_container = tk.Frame(
            self.canvas_frame,
            bg="white",
            highlightbackground=self.secondary_color,
            highlightthickness=1,
        )
        self.canvas_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Main canvas
        self.canvas = tk.Canvas(
            self.canvas_container,
            width=900,
            height=700,
            bg="white",
            bd=0,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius, **kwargs):
        """Create a rounded rectangle"""
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    def create_rounded_button(self, parent, text, command):
        """Create a button with rounded corners and gradient effect"""
        frame = tk.Frame(parent, bg="white")
        frame.pack(pady=8)
        
        button = tk.Canvas(
            frame,
            width=250,
            height=40,
            bg="white",
            highlightthickness=0
        )
        button.pack()

        # Create gradient button with rounded corners
        self.create_rounded_rectangle(
            button,
            0, 0, 250, 40,
            radius=20,
            fill=self.button_gradient[0],
            outline="",
            tags=("button_bg",)
        )

        button.create_text(
            125, 20,
            text=text,
            fill="white",
            font=("Segoe UI", 11, "bold"),
            tags=("button_text",)
        )

        def on_click(event):
            command()

        def on_enter(event):
            button.itemconfig("button_bg", fill=self.button_hover_gradient[0])

        def on_leave(event):
            button.itemconfig("button_bg", fill=self.button_gradient[0])

        button.bind("<Button-1>", on_click)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button

    def create_control_panel(self):
        """Create enhanced control panel with modern styling"""
        self.control_panel = tk.Frame(
            self.main_frame,
            bg="white",
            width=350,
            padx=30,
            pady=30,
        )
        self.control_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10)
        
        # Title with enhanced styling
        title_frame = tk.Frame(self.control_panel, bg="white")
        title_frame.pack(fill=tk.X, pady=(0, 25))
        
        title = tk.Label(
            title_frame,
            text="Data Structure\nVisualizer",
            bg="white",
            fg=self.primary_color,
            font=("Segoe UI", 28, "bold"),
            justify=tk.CENTER
        )
        title.pack()
        
        # Subtitle
        subtitle = tk.Label(
            title_frame,
            text="Visualize and interact with data structures",
            bg="white",
            fg=self.text_color,
            font=("Segoe UI", 11),
            justify=tk.CENTER
        )
        subtitle.pack(pady=(5, 0))
        
        # Structure selector with modern styling
        selector_frame = tk.Frame(self.control_panel, bg="white")
        selector_frame.pack(fill=tk.X, pady=15)
        
        selector_label = tk.Label(
            selector_frame,
            text="Select Data Structure",
            bg="white",
            fg=self.text_color,
            font=("Segoe UI", 12, "bold")
        )
        selector_label.pack(anchor="w", pady=(0, 5))
        
        self.structure_selector = ttk.Combobox(
            selector_frame,
            values=["BST", "Stack", "Queue"],
            font=self.font_style,
            state="readonly"
        )
        self.structure_selector.set("BST")
        self.structure_selector.pack(fill=tk.X, pady=5)
        self.structure_selector.bind('<<ComboboxSelected>>', self.toggle_structure)
        
        # Create rounded buttons
        self.insert_button = self.create_rounded_button(
            self.control_panel,
            "Insert Element",
            self.insert
        )
        
        self.delete_button = self.create_rounded_button(
            self.control_panel,
            "Delete Element",
            self.delete
        )
        
        self.show_button = self.create_rounded_button(
            self.control_panel,
            "Visualize Structure",
            self.show_structure
        )
        
        self.clear_button = self.create_rounded_button(
            self.control_panel,
            "Clear Canvas",
            self.clear_canvas
        )
        
        # Enhanced status display
        self.status_frame = tk.Frame(self.control_panel, bg="white")
        self.status_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Ready to start",
            bg="white",
            fg=self.text_color,
            font=("Segoe UI", 11),
            wraplength=280
        )
        self.status_label.pack()

    def on_hover(self, event, button):
        """Enhanced hover effect for buttons."""
        button.config(bg=self.button_hover_gradient[0])

    def on_leave(self, event, button):
        """Enhanced leave effect for buttons."""
        button.config(bg=self.button_gradient[0])

    def toggle_structure(self, event):
        """Switch between data structures."""
        self.current_structure = self.structure_selector.get()
        self.clear_canvas()
        self.status_label.config(text=f"Switched to {self.current_structure}", fg=self.text_color)

    def insert(self):
        """Insert a node depending on the selected structure."""
        if self.current_structure == "BST":
            value = random.randint(1, 100)
            self.bst.insert(value)
            self.status_label.config(text=f"Inserted {value} into BST", fg=self.success_color)
            self.show_structure()
        elif self.current_structure == "Stack":
            value = random.randint(1, 100)
            self.stack.push(value)
            self.status_label.config(text=f"Pushed {value} onto Stack", fg=self.success_color)
            self.show_structure()
        elif self.current_structure == "Queue":
            value = random.randint(1, 100)
            self.queue.enqueue(value)
            self.status_label.config(text=f"Enqueued {value} into Queue", fg=self.success_color)
            self.show_structure()

    def delete(self):
        """Delete a node depending on the selected structure."""
        try:
            if self.current_structure == "BST":
                if self.bst.root:
                    value = random.choice(self.bst.inorder())
                    self.bst.delete(value)
                    self.status_label.config(text=f"Deleted {value} from BST", fg=self.success_color)
                else:
                    self.status_label.config(text="BST is empty", fg=self.error_color)
            elif self.current_structure == "Stack":
                if self.stack.items:
                    value = self.stack.pop()
                    self.status_label.config(text=f"Popped {value} from Stack", fg=self.success_color)
                else:
                    self.status_label.config(text="Stack is empty", fg=self.error_color)
            elif self.current_structure == "Queue":
                if self.queue.items:
                    value = self.queue.dequeue()
                    self.status_label.config(text=f"Dequeued {value} from Queue", fg=self.success_color)
                else:
                    self.status_label.config(text="Queue is empty", fg=self.error_color)
            
            self.show_structure()
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg=self.error_color)

    def show_structure(self):
        """Display the current data structure."""
        self.clear_canvas()
        
        # Create colors dictionary
        colors = {
            'primary': self.primary_color,
            'secondary': self.secondary_color
        }

        if self.current_structure == "BST":
            self.bst.draw(self.canvas, colors=colors)
        elif self.current_structure == "Stack":
            self.stack.draw(self.canvas, colors=colors)
        elif self.current_structure == "Queue":
            self.queue.draw(self.canvas, colors=colors)

    def clear_canvas(self):
        """Clear the canvas for a fresh drawing."""
        self.canvas.delete("all")
        self.status_label.config(text="Ready to start", fg=self.text_color)

# --- Main Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructureVisualizer(root)
    root.mainloop()