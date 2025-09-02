# Banner Game: Text Banner Creation


The program creates a text banner from user-entered text. It greets the user, prompts for text, and outputs it as a formatted banner.
The code demonstrates basic principles of working with functions, input/output, and conditional statements in Python.

---

## **How the program works**

The program consists of two main parts:
1. **`create_banner(text)` function** – responsible for creating and displaying the text banner.
2. **Main part of the program** – user interaction: greeting, text request, and input validation.

---

## **Program code**

```python
# Banner Game: Text Banner Creation

# Function to create a banner
def create_banner(text):
    """
    Creates a text banner from the entered text.
    :param text: The string to convert into a banner.
    :return: None
    """
    # Determine banner width (text length + 4 characters for the border)
    banner_width = len(text) + 4

    # Print the top border of the banner
    print("*" * banner_width)

    # Print the text with a border
    print(f"* {text} *")

    # Print the bottom border of the banner
    print("*" * banner_width)

# Main part of the program
if __name__ == "__main__":
    # Greet the user
    print("Welcome to the Banner game!")
    print("Enter text, and I will create a text banner for you.")

    # Prompt the user for text
    user_text = input("Enter text: ")

    # Check that the text is not empty
    if user_text.strip() == "":
        print("You did not enter text. Please try again.")
    else:
        # Create and display the banner
        print("\nYour banner is ready:")
        create_banner(user_text)
```

---

## **Code operation description**

### **1. `create_banner(text)` function**
- **Accepts:** `text` string – the text to convert into a banner.
- **Performs:**
  - Calculates the banner width, adding 4 characters for the border (`*` and spaces).
  - Prints the top and bottom borders of the banner using the `*` character.
  - Prints the text surrounded by a border.

### **2. Main part of the program**
- **Greets** the user and explains what the program does.
- **Prompts** the user for text to create a banner.
- **Checks** that the text is not empty:
  - If the user entered an empty string, the program reports an error and asks to try again.
  - If text is entered, the program outputs the created banner.

---

## **Program example**

If the user entered the text `"Hello"`, the program will output:
```
*********
* Hello *
*********
```

---


## **How the interpreter parses the code**

### **Order of operator execution in Python**
- Python reads code line by line, starting from the top and moving down.
- Each line is executed sequentially, unless it is part of a function, condition, or loop.

### **Function definition**
- Functions are defined using the `def` keyword.
- Defining a function does not execute its code, but only creates a "template" for future calls.

### **Function calls**
- When a function is called, Python jumps to its definition and executes the code within it.
- After the function finishes executing, control returns to the place from which it was called.

### **Conditional statements (if, else)**
- Conditional statements check a condition and execute the code within the block if the condition is true.
- If the condition is false, Python skips the block and moves to the next line.

### **Loops (for, while)**
- Loops allow repeating the execution of a code block multiple times.
- Python checks the loop condition before each iteration.

### **Assignment operators (=)**
- Assignment operators store a value in a variable.
- This happens before other operations, such as function calls or conditional statements, are executed.

### **Expressions and calculations**
- Expressions (e.g., `len(text) + 4`) are evaluated before their result is used in other parts of the code.

---

## **Summary**

This program demonstrates the basic principles of working with functions, input/output, and conditional statements in Python. It can be useful for beginners learning the language and understanding how the Python interpreter works.
