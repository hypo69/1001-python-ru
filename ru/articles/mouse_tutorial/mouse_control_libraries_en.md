# Mouse Control in Python: Overview and Comparison of Libraries

Mouse action automation is a powerful tool for testing, scientific research, business processes, and the creation of assistive technologies. Within the Python ecosystem, several libraries exist for these purposes, each with its own strengths and use cases. In this article, we will take a detailed look at three main cross-platform libraries: `PyAutoGUI`, `pynput`, and `mouse`, and also briefly mention other specialized solutions.

## 1. PyAutoGUI Library: High-Level GUI Automation

`PyAutoGUI` is a powerful and easy-to-use cross-platform library that allows Python scripts to control the mouse and keyboard, take screenshots, and perform other GUI automation tasks. It is ideal for automating routine tasks, software testing, and bot creation. **Supports Windows, macOS, and Linux.**

### Installation

```bash
pip install pyautogui
```

### Key Features

*   **Cursor Movement**: `pyautogui.moveTo(x, y, duration=seconds)` for absolute movement and `pyautogui.move(xOffset, yOffset, duration=seconds)` for relative movement.
*   **Mouse Clicks**: `pyautogui.click()`, `pyautogui.rightClick()`, `pyautogui.doubleClick()`, `pyautogui.tripleClick()`. You can specify coordinates and the button.
*   **Drag and Drop**: `pyautogui.dragTo(x, y, duration=seconds)` or `pyautogui.drag(xOffset, yOffset, duration=seconds)`.
*   **Mouse Wheel Scrolling**: `pyautogui.scroll(amount)` (positive value scrolls up, negative scrolls down).
*   **Keyboard Interaction**: `pyautogui.write()`, `pyautogui.press()`, `pyautogui.hotkey()`.
*   **Get Cursor Position**: `pyautogui.position()`.
*   **Failsafe**: A built-in safety feature that stops the script when the mouse cursor is moved to one of the four corners of the screen.

### Usage Examples

```python
import pyautogui
import time

# Move cursor
pyautogui.moveTo(100, 150, duration=1)
print(f"Cursor moved to {pyautogui.position()}")

# Left click
pyautogui.click(200, 250)
print("Click performed.")

# Drag
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.dragTo(600, 600, duration=1)
print("Drag performed.")

# Scroll wheel
pyautogui.scroll(-100)
print("Scrolled down.")

# Type text
pyautogui.write('Hello, PyAutoGUI!', interval=0.1)
print("Text typed.")
```

### When to use PyAutoGUI?

✅ Ideal if you need a quick and easy way to automate user actions, simulate input, and take screenshots. It is excellent for high-level automation scripts where detailed control over input events is not required.

❌ Not the best choice for low-level event monitoring or input blocking.

## 2. pynput Library: Flexible Control and Monitoring

`pynput` is a modern, actively maintained tool for comprehensive monitoring and control of input devices. It provides detailed access to mouse and keyboard events, including the ability to block or modify them in real-time. **Supports Windows, macOS, and Linux.**

### Installation

```bash
pip install pynput
```

### Key Features

*   **Comprehensive Event Listeners**: `pynput.mouse.Listener` allows tracking movements, clicks, and scrolling with access to coordinates, button type, and state (pressed/released).
*   **Event Blocking**: If an event handler returns `False`, the event is not passed further to the system. This is a unique and powerful feature.
*   **Mouse Control via Controller**: `pynput.mouse.Controller` for emulating actions (positioning, relative movement, clicks, scrolling).
*   **Unified Keyboard Architecture**: Easily combine mouse and keyboard actions.
*   **Thread Safety**: Listeners operate in separate threads, providing flexible management.

### Usage Examples

```python
from pynput import mouse
from pynput.mouse import Controller, Button
import time

# Mouse control
mouse_ctrl = Controller()
print(f"Current position: {mouse_ctrl.position}")
mouse_ctrl.position = (100, 200)
mouse_ctrl.move(50, -50)
mouse_ctrl.click(Button.left, 1)
mouse_ctrl.scroll(0, 2)
print("Mouse actions performed.")

# Event listener
def on_click(x, y, button, pressed):
    print(f"Click at ({x}, {y}) with button {button}. Pressed: {pressed}")
    if not pressed:
        # Stop listener after button release
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
print("Listener active. Click the mouse.")
listener.join() # Wait for listener to finish
print("Listener finished.")
```

### When to use pynput?

✅ Ideal if you:
- Need to **analyze user behavior** (coordinates, trajectories, click frequency).
- Are creating **hotkey systems**, **input filters**, or **assistive technologies**.
- Want to **block or modify input** in real-time.
- Are conducting a **scientific experiment**, **usability testing**, or **security system**.
- Require **mouse and keyboard integration** in a single script.

❌ Not the fastest choice if you only need to record and replay actions without analysis.

## 3. mouse Library: Simplicity and Action Recording

The `mouse` library is a minimalistic but effective tool for emulating and recording sequences of mouse actions. Its main feature is built-in support for recording and playback, making it ideal for rapid macro prototyping. **Supports Windows, macOS, and Linux.**

### Installation

```bash
pip install mouse
```

### Key Features

*   **Cursor Movement**: `mouse.move(x, y, absolute=True/False)`.
*   **Mouse Clicks**: `mouse.click('left'/'right'/'middle')`.
*   **Drag and Drop**: `mouse.drag(x1, y1, x2, y2, absolute=True)`.
*   **Scroll Wheel**: `mouse.wheel(delta)`.
*   **Get Cursor Position**: `mouse.get_position()`.
*   **Check Button State**: `mouse.is_pressed(button)`.
*   **Record and Playback Events**: `mouse.record()` and `mouse.play()`. This is a unique built-in function.
*   **Simple Click Handler**: `mouse.on_click(handler)`.

### Usage Examples

```python
import mouse
import time

# Move and click
mouse.move(200, 300, absolute=True, duration=0.2)
mouse.click('left')
print("Move and click performed.")

# Record and playback (requires interactive input)
print("Start recording. Press right button to stop.")
# events = mouse.record()
# print("Recording finished. Playing back...")
# mouse.play(events[:-1]) # Play all but the last event (right button release)
# print("Playback finished.")

# Scroll
mouse.wheel(-2)
print("Scrolled down.")
```

### When to use mouse?

✅ Ideal for:
- Recording and replaying routine actions.
- Simple automation scripts without feedback.
- Educational examples and demonstrations where maximum simplicity is key.

❌ Not suitable for:
- Analyzing user behavior (handlers do not receive coordinates).
- Creating input filters or blockers.
- Keyboard integration.
- The project has not been updated since 2021, which may be a risk for long-term projects.

## 4. Other Notable Libraries

While `PyAutoGUI`, `pynput`, and `mouse` are the most versatile, other libraries exist for more specific tasks:

*   **PyDirectInput**: A specialized library designed as an alternative to `PyAutoGUI` for game automation. It can bypass issues where some games may not register input from `PyAutoGUI` due to their specific input handling mechanisms.
*   **pywinauto**: Focused on Windows user interface automation. It interacts with Windows controls using accessibility and UI Automation frameworks, making it a reliable choice for automating native Windows applications by targeting elements rather than screen coordinates.

## 5. Comparison Table

| Feature / Library        | PyAutoGUI | pynput | mouse |
|--------------------------|:---------:|:------:|:-----:|
| **Supported OS**         | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
|--------------------------|:---------:|:------:|:-----:|
| **Installation**         | `pip install pyautogui` | `pip install pynput` | `pip install mouse` |
| **Cursor Movement**      | ✅ Abs./Rel. | ✅ Abs./Rel. | ✅ Abs./Rel. |
| **Mouse Clicks**         | ✅ All types | ✅ All types | ✅ All types |
| **Drag and Drop**        | ✅ `dragTo()` | ⚠️ Manual | ✅ `drag()` |
| **Scroll Wheel**         | ✅ Yes      | ✅ Yes   | ✅ Yes  |
| **Get Position**         | ✅ Yes      | ✅ Yes   | ✅ Yes  |
| **Check Button State**   | ❌ No       | ⚠️ Via Listener | ✅ Yes  |
| **Record/Playback**      | ❌ No       | ❌ No (manual only) | ✅ Built-in |
| **Coords in Handler**    | ❌ No       | ✅ Yes   | ❌ No   |
| **Event Blocking**       | ❌ No       | ✅ Yes (`return False`) | ❌ No   |
| **Keyboard Integration** | ✅ Yes      | ✅ Yes   | ❌ No   |
| **Active Support**       | ✅ Yes      | ✅ Yes   | ❌ No (since 2021) |
| **Failsafe**             | ✅ Yes      | ❌ No    | ❌ No   |
| **API Complexity**       | Medium    | Medium/High | Low   |

## Conclusion

The choice of a Python mouse control library depends on your specific needs:

*   **PyAutoGUI**: Your default choice for high-level GUI automation when you need to simulate user actions, including keyboard and screenshots, without deep event analysis.
*   **pynput**: Ideal for projects requiring precise control over mouse (and keyboard) events, monitoring, analysis, as well as the ability to block or modify input in real-time. It is a professional tool for complex systems.
*   **mouse**: Best suited for simple tasks of macro recording and playback, where maximum simplicity and minimal code are important. However, the lack of active support should be considered.

For new projects requiring flexibility and long-term support, `pynput` is recommended. If your task is rapid automation of routine actions, `PyAutoGUI` will be an excellent choice.
