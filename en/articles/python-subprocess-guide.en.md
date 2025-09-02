## Working with the `subprocess` library in Python


### 1. **What is `subprocess` and why is it needed?**

The `subprocess` module in Python provides an interface for creating new processes,
connecting to their input/output/error streams, and getting their return codes.
It allows Python scripts to run and manage other programs,
written in any language, whether they are system utilities, shell scripts, or other executables.

**Historical context:**

Before the advent of `subprocess`, functions from the `os` module, such as `os.system()`, `os.spawn*()`, and the `commands` module (in Python 2) were used to run external processes. These approaches had a number of disadvantages:
*   `os.system()`: Runs a command through the system shell, which is insecure when working with user input and less flexible in managing streams.
*   `os.spawn*()`: More flexible, but difficult to use and platform-dependent.
*   The `popen2` module (and its variations): Provided access to streams, but was complex and had problems with deadlocks.

The `subprocess` module was introduced in Python 2.4 (PEP 324) as a unified and more secure way to interact with child processes. It encapsulates the best functionality of previous modules and provides a cleaner API.

**Main tasks solved with `subprocess`:**

*   Executing operating system commands (e.g., `ls`, `dir`, `ping`).
*   Running external utilities for data processing (e.g., `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Integration with version control systems (`git`, `svn`).
*   Running compilers or interpreters of other languages.
*   Automating system administration.
*   Organizing interaction between different programs.

---

### 2. Main functions and classes

The `subprocess` module offers several ways to run processes:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   This is the **recommended** high-level API, introduced in Python 3.5.
    *   Runs a command, waits for it to complete, and returns a `CompletedProcess` object.
    *   Suitable for most cases where you just need to execute a command and get the result.

    ```python
    import subprocess

    # Simple run
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # If check=True and the command returned non-zero, CalledProcessError will be raised
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   This is the main class for creating and managing child processes.
    *   Provides maximum flexibility: non-blocking execution, detailed control of I/O streams, the ability to send signals to the process.
    *   The `run()` function uses `Popen` internally.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Process started with PID: {process.pid}")
    # ... can do other work ...
    process.wait() # Wait for completion
    print(f"Process finished with code: {process.returncode}")
    ```

*   **Deprecated, but still encountered functions (were the main API before Python 3.5):**
    *   `subprocess.call(args, ...)`: Executes a command and waits for it to complete. Returns the return code. Similar to `os.system()`, but safer if `shell=False`.
    *   `subprocess.check_call(args, ...)`: Like `call()`, but raises `CalledProcessError` if the return code is not 0.
    *   `subprocess.check_output(args, ...)`: Executes a command, waits for completion, and returns its standard output (stdout) as a byte string. Raises `CalledProcessError` if the return code is not 0.

    Although these functions still work, `subprocess.run()` provides a more convenient and unified interface for the same tasks.

---

### 3. Key arguments of the `run()` and `Popen()` functions

These arguments allow you to fine-tune the launch and interaction with the child process:

*   **`args`**:
    *   The first and mandatory argument.
    *   Can be a list of strings (recommended) or a single string (if `shell=True`).
    *   The first element of the list is the name of the executable file, the rest are its arguments.
    *   Example: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**:
    *   Define how the standard input, output, and error streams of the child process will be handled.
    *   Possible values:
        *   `None` (default): Inherited from the parent process.
        *   `subprocess.PIPE`: A pipe is created through which data can be exchanged. `process.stdin`, `process.stdout`, `process.stderr` become file-like objects.
        *   `subprocess.DEVNULL`: Redirects the stream to "nowhere" (analogous to `/dev/null`).
        *   An open file descriptor (an integer).
        *   An existing file object (e.g., an open file `open('output.txt', 'w')`).

*   **`capture_output=True` (for `run()`):**
    *   A convenient option, equivalent to setting `stdout=subprocess.PIPE` and `stderr=subprocess.PIPE`.
    *   The result will be available in `result.stdout` and `result.stderr`.

*   **`text=True` (or `universal_newlines=True` for compatibility):**
    *   If `True`, the `stdout` and `stderr` streams (as well as `stdin`, if a string is passed) will be opened in text mode using the default encoding (usually UTF-8). Decoding/encoding occurs automatically.
    *   If `False` (default), the streams are treated as bytes.
    *   Since Python 3.7, `text` is the preferred alias for `universal_newlines`. You can also specify a specific encoding via `encoding` and an error handler via `errors`.

*   **`shell=False` (default):**
    *   If `False` (recommended for security and predictability), `args` must be a list. The command is run directly.
    *   If `True`, `args` is passed as a string to the system shell (e.g., `/bin/sh` on Unix, `cmd.exe` on Windows) for interpretation. This allows you to use shell features (variables, substitutions, pipelines), but is **DANGEROUS** if `args` contains untrusted user input (risk of command injection).

*   **`cwd=None`:**
    *   Sets the current working directory for the child process. By default, it is inherited from the parent.

*   **`env=None`:**
    *   A dictionary that defines the environment variables for the new process. By default, the environment of the parent process is inherited. If specified, it completely replaces the inherited environment. To add/change variables while keeping the rest, you must first copy `os.environ` and then modify it.

*   **`timeout=None`:**
    *   The maximum time in seconds allotted for the execution of the command. If the process does not complete within this time, a `subprocess.TimeoutExpired` exception will be raised. `Popen.communicate()` also accepts a `timeout`.

*   **`check=False` (for `run()`):**
    *   If `True` and the process exits with a non-zero return code, a `subprocess.CalledProcessError` exception will be raised.

---

### 4. Working with results and errors

**The `CompletedProcess` object (the result of `run()`):**

```python
import subprocess

try:
    # Trying to execute a command that may fail
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - a typo to demonstrate an error
        capture_output=True,
        text=True,
        check=True, # Will raise an exception if returncode != 0
        timeout=10
    )
    print("Command executed successfully.")
    print("Return code:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Usually empty on success

except subprocess.CalledProcessError as e:
    print(f"Error executing command (CalledProcessError):")
    print(f"  Command: {e.cmd}")
    print(f"  Return code: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # May contain output before the error
    print(f"  Stderr: {e.stderr}") # Usually contains error information
except subprocess.TimeoutExpired as e:
    print(f"Command did not complete in {e.timeout} seconds.")
    print(f"  Command: {e.cmd}")
    if e.stdout: print(f"  Stdout (partial): {e.stdout.decode(errors='ignore')}") # stdout is bytes
    if e.stderr: print(f"  Stderr (partial): {e.stderr.decode(errors='ignore')}") # stderr is bytes
except FileNotFoundError:
    print("Error: command or program not found.")
except Exception as e:
    print(f"Another error occurred: {e}")
```

**`CompletedProcess` attributes:**
*   `args`: The arguments used to launch the process.
*   `returncode`: The return code of the process. 0 usually means success.
*   `stdout`: The standard output of the process (bytes or a string if `text=True` and `capture_output=True`).
*   `stderr`: The standard error stream of the process (bytes or a string if `text=True` and `capture_output=True`).

**Exceptions:**
*   `subprocess.CalledProcessError`: Raised if `check=True` (for `run()`) or `check_call()`, `check_output()` are used and the command exits with a non-zero code. Contains `returncode`, `cmd`, `output` (or `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: If the timeout has expired. Contains `cmd`, `timeout`, `stdout`, `stderr` (partial output, if any).
*   `FileNotFoundError`: If the executable file is not found.

**Interacting with a `Popen` object:**

The `Popen` class gives more control:

```python
import subprocess
import time

# Run a process in the background
process = subprocess.Popen(["sleep", "5"])
print(f"Process PID: {process.pid} started.")

# Non-blocking status check
while process.poll() is None: # poll() returns None if the process is still running
    print("Process is still running...")
    # You can read the output as it arrives (be careful, it can block!)
    # line = process.stdout.readline()
    # if line: print(f"Output: {line.strip()}")
    time.sleep(1)

# Wait for completion and get all output/errors
# stdout_data, stderr_data = process.communicate(timeout=10) # Safe way

# If communicate() was not used, after poll() != None you can read the rest
if process.stdout:
    for line in process.stdout:
        print(f"Final output: {line.strip()}")

print(f"Process finished with code: {process.returncode}")

# If you need to force termination
# process.terminate() # Sends SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # If it has not terminated
#     process.kill()      # Sends SIGKILL
```

*   `process.poll()`: Checks if the child process has terminated. Returns the return code or `None`. Non-blocking.
*   `process.wait(timeout=None)`: Waits for the child process to terminate. Returns the return code. Blocking.
*   `process.communicate(input=None, timeout=None)`:
    *   The safest way to interact with a process when using `PIPE`.
    *   Sends data to `stdin` (if `input` is specified), reads all data from `stdout` and `stderr` to the end, and waits for the process to terminate.
    *   Returns a tuple `(stdout_data, stderr_data)`.
    *   Helps to avoid deadlocks that can occur with direct reading/writing to `process.stdout`/`process.stdin` if the buffers overflow.
*   `process.terminate()`: Sends the `SIGTERM` signal to the process (soft termination).
*   `process.kill()`: Sends the `SIGKILL` signal to the process (hard termination).
*   `process.send_signal(signal)`: Sends the specified signal to the process.
*   `process.stdin`, `process.stdout`, `process.stderr`: File-like objects for pipes, if they were created with `PIPE`.

---

### 5. Advanced usage scenarios

**Redirecting the output of one command to the input of another (pipelines):**

Emulating `ps aux | grep python`:

```python
import subprocess

# Run the first command, its stdout will be a PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Run the second command, its stdin will be the stdout of the first command
# The stdout of the second command is also a PIPE to read the result
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Link stdout from ps to stdin for grep
    stdout=subprocess.PIPE,
    text=True
)

# Important! Close the stdout of the first command in the parent process,
# so that grep receives EOF when ps finishes.
if ps_process.stdout:
    ps_process.stdout.close()  

# Get the output from grep
stdout_data, stderr_data = grep_process.communicate()

print("Pipeline result:")
print(stdout_data)

if stderr_data:
    print("Grep errors:", stderr_data)

# Make sure both processes have finished
ps_process.wait()
# grep_process.wait() # communicate() has already waited
print(f"ps return code: {ps_process.returncode}")
print(f"grep return code: {grep_process.returncode}")
```
*Note:* For simple pipelines, `subprocess.run("ps aux | grep python", shell=True, ...)` may be simpler, but less secure and flexible.

**Asynchronous process execution:**

`Popen` is non-blocking by nature. You can run multiple processes and manage them in parallel.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Command with an error
]

processes = []
for cmd_args in commands:
    print(f"Running: {' '.join(cmd_args)}")
    # For asynchronicity, it is better to redirect stdout/stderr,
    # so as not to interfere with each other or the parent's console.
    # DEVNULL if the output is not needed, PIPE if it is needed later.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Do other work or wait for completion
while any(p.poll() is None for p in processes):
    print("Waiting for all processes to complete...")
    time.sleep(0.5)

print("\nResults:")
for i, p in enumerate(processes):
    print(f"Command '{' '.join(commands[i])}' finished with code: {p.returncode}")
```

**Interactive interaction with a process:**

This is a complex task that requires careful management of streams to avoid deadlocks. `communicate()` is good for a one-time exchange. For a long interactive session, you may need to read/write directly to `p.stdin`, `p.stdout`, `p.stderr` using non-blocking I/O or separate threads.

```python
import subprocess

# Example: starting an interactive python session
process = subprocess.Popen(
    ['python', '-i'], # -i for interactive mode
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Line buffering for stdout/stderr (for interactivity)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Important!

def read_output():
    # Reading the output can be tricky, as you need to know when to stop.
    # This is a very simplified example. For real tasks, more robust solutions are needed.
    # For example, read until a certain pattern (the command line prompt).
    output = ""
    # Read stdout. In a real application, this should be done in a non-blocking way or in a separate thread.
    # Here we assume that after the command there will be some output immediately.
    # This is a very fragile assumption for the general case!
    try:
        # Popen does not have a readline with a timeout, this is one of the difficulties
        # You can use select on process.stdout.fileno()
        # or read character by character/line by line in a separate thread
        # For simplicity, this is not here
        while True: # Be careful, it can block!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Primitive prompt detector
                output += line
                break
            output += line
    except Exception as e:
        print(f"Read error: {e}")
    return output.strip()

# Initialization: read the initial prompt
initial_output = ""
# Reading the Python welcome message
# This is very simplified, as we do not know exactly how many lines to read
for _ in range(5): # Let's try to read a few lines
    try:
        # Popen stdout has no timeout, you need to read carefully
        # stdout.readline() can block.
        # In real applications, select or threads are needed here.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Found the prompt
    except BlockingIOError:
        break # If there was non-blocking reading
print(f"Initial output:\n{initial_output.strip()}")


send_command("a = 10")
# For interactive interaction, reading the output is the most difficult part.
# communicate() is not suitable, as it closes the streams.
# You need to carefully read from process.stdout and process.stderr, 
# possibly in separate threads, so as not to block the main one.
# This example is NOT production-ready for complex interactivity.
# print(read_output()) # This read_output is very primitive

send_command("print(a * 2)")
# print(read_output())

# Terminate the process
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Wait for completion and collect the rest

print("\nFinal stdout:")
print(stdout_data)
if stderr_data:
    print("\nFinal stderr:")
    print(stderr_data)

print(f"Python process finished with code: {process.returncode}")

# For real interactive interaction, pty (pseudo-terminals) are often used
# via the `pty` module on Unix-like systems, or libraries like `pexpect`.
```
*Warning*: Direct interactive interaction with `Popen` via `stdin`/`stdout`/`stderr` is difficult due to deadlocks and buffering. For reliable interactivity, libraries like `pexpect` (for Unix) or similar are often used, which work with pseudo-terminals (pty).

**Working with encodings:**
*   Use `text=True` (or `universal_newlines=True`) for automatic decoding/encoding.
*   If necessary, you can specify `encoding="your-encoding"` and `errors="error-handler"` (e.g., `replace`, `ignore`).
*   If `text=False` (default), `stdout` and `stderr` will be byte strings. You will need to decode them manually: `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Security and best practices

*   **Risks of `shell=True` and command injection:**
    *   **Never** use `shell=True` with commands constructed from untrusted user input. This opens the way for command injection.
    *   Example of a vulnerability:
        ```python
        # DANGEROUS!
        filename = input("Enter a filename to delete: ") # The user enters "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   If `shell=True` is absolutely necessary (e.g., to use pipes `|` or wildcards `*` directly in the command line), carefully escape all parts of the command formed from the outside using `shlex.quote()` (since Python 3.3).

*   **Validation and escaping of user input:**
    *   Even if `shell=False`, if the command arguments are formed from user input, they should be validated. For example, if a filename is expected, make sure it is a valid filename and not something like `../../../etc/passwd`.

*   **Passing arguments as a list (when `shell=False`):**
    *   This is the safest way. Each argument is passed as a separate element of the list, and the operating system handles them correctly, without trying to interpret them as part of a shell command.
    *   Example: `subprocess.run(["rm", filename_from_user])` — here `filename_from_user` will always be treated as a single argument (filename), even if it contains spaces or special characters.

*   **Handling errors and return codes:**
    *   Always check the `returncode` or use `check=True` (for `run()`) / `check_call()` / `check_output()` to make sure the command executed successfully.
    *   Handle possible exceptions (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Resource management:**
    *   If you open pipes (`PIPE`), make sure they are eventually closed. `Popen.communicate()` does this automatically. If you are working with `p.stdin/stdout/stderr` directly, you may need to close them explicitly.
    *   In long-running applications, make sure that child processes terminate correctly and do not become "zombies". Use `p.wait()` or `p.communicate()`. If necessary, use `p.terminate()` or `p.kill()`.

*   **Encodings:** Be careful with encodings when using `text=True` or when manually decoding byte strings. Encoding problems are a common source of errors.

---

### 7. Practical examples

**1. Executing a simple command and checking the return code:**
```python
import subprocess

try:
    # Run 'ls' for an existing directory
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Command 'ls /tmp' executed, return code: {result.returncode}")

    # Run 'ls' for a non-existent directory
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # This line will not be executed if check=True, as an exception will be raised
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e.cmd}")
    print(f"Return code: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Capturing the output of a command:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Specify the current directory as the working directory for git
    )
    print("Git status:")
    print(result.stdout)
except FileNotFoundError:
    print("Error: 'git' command not found. Is Git installed and in the PATH?")
except subprocess.CalledProcessError as e:
    print(f"Git error: {e.stderr}")
```

**3. Sending data to the input of a process (using `communicate`):**
```python
import subprocess

# Send text to 'grep' for searching
input_text = "hello world\npython is fun\nhello python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep found matches
        print("Found lines:")
        print(stdout_data)
    elif process.returncode == 1: # grep found no matches
        print("No matches for 'python' found.")
    else: # other grep error
        print(f"Grep error (code {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep did not respond in time.")
    process.kill() # Kill the process if it hangs
    process.communicate() # Collect the remaining output/errors
```

**4. Creating a pipeline (`ls -l | wc -l`) without `shell=True`:**
(A more detailed example was in section 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Make sure stdout exists
    ls_proc.stdout.close()  # Allows wc_proc to receive EOF when ls_proc finishes

output, _ = wc_proc.communicate()
print(f"Number of files/directories: {output.strip()}")
```

**5. Using `timeout`:**
```python
import subprocess

try:
    # A command that will run for 5 seconds
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Command 'sleep 5' completed (should not have with timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Command '{e.cmd}' did not complete in {e.timeout} seconds.")
```

---

### 8. Conclusion and useful resources

The `subprocess` module is an indispensable tool for any Python developer who needs to interact with external programs or the system environment. It offers a balance between ease of use (via `subprocess.run()`) and powerful flexibility (via `subprocess.Popen()`).

**Key points:**
*   Prefer `subprocess.run()` for most tasks.
*   Use `subprocess.Popen()` for asynchronous execution or complex stream management.
*   **Avoid `shell=True`**, especially with user input, due to security risks. Pass commands as a list of arguments.
*   Always handle return codes and possible exceptions.
*   Be careful with encodings when working with text output (`text=True` or manual decoding).
*   `communicate()` is your friend for safe data exchange via `PIPE`.

**Useful resources:**
*   Official Python documentation for the `subprocess` module: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - A New Process Module: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)


