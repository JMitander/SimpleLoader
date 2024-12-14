# SimpleLoader: A Loading Bar and Spinner Utility

A simple yet effective utility for displaying a loading bar and a spinning loader across multiple programming languages. This utility is useful for indicating progress or activity in command-line applications.

## Supported Languages
- Python
- JavaScript (Node.js)
- Rust
- PHP

## Features
- **Loading Bar**: Displays a dynamic progress bar with a customizable prefix, suffix, and character fill.
- **Spinning Loader**: Displays a spinning animation with customizable spinner characters and duration.

---

## Python

### Installation
No installation required for Python. Simply copy the code into your script.

### Usage
```python
from simple_loader import SimpleLoader

# Loading Bar Example
SimpleLoader.loading_bar(total_steps=100, prefix='Downloading', suffix='Complete', length=50)

# Spinning Loader Example
SimpleLoader.spinning_loader(duration=5, message='Processing', spinner_chars='|/-\\')
```

---

## JavaScript (Node.js)

### Installation
Ensure you have Node.js installed. No additional packages required.

### Usage
```javascript
// Example usage
SimpleLoader.loadingBar(100, 'Downloading', 'Complete', 50);
SimpleLoader.spinningLoader(5, 'Processing', '|/-\\');
```

---

## Rust

### Installation
Ensure you have Rust installed. Create a new project with `cargo new simple_loader` and copy the code into `src/main.rs`.

### Usage
```rust
fn main() {
    // Loading Bar Example
    SimpleLoader::loading_bar(100, "Downloading", "Complete", 50, '█');
    
    // Spinning Loader Example
    SimpleLoader::spinning_loader(5, "Processing", "|/-\\");
}
```

---

## PHP

### Installation
Ensure you have PHP installed. You can run the PHP file directly from the command line.

### Usage
```php
// Example usage
SimpleLoader::loadingBar(100, 'Downloading', 'Complete', 50);
SimpleLoader::spinningLoader(5, 'Processing', '|/-\\');
```

---

## Customization Options

### Loading Bar:
- `totalSteps`: Number of steps for completion (used to calculate progress).
- `prefix`: Text displayed before the progress bar.
- `suffix`: Text displayed after the progress bar.
- `length`: The length of the progress bar.
- `fill`: The character used to fill the progress bar.

### Spinning Loader:
- `duration`: How long the spinner should run (in seconds).
- `message`: The message displayed alongside the spinner.
- `spinnerChars`: The characters used for the spinner animation (e.g., '|', '/', '-', '\\').

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

---

## About
This utility was created to provide a simple and effective way to show progress in command-line tools. You can use it in your scripts to improve user experience by visually indicating that a task is in progress.

For more information, visit the [GitHub repository](https://github.com/JMitander/).
```
