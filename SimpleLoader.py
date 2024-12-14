
#  | A simple yet effective loading bar and spinner utility. | By https://github.com/JMitander/ | (MIT License) |  #        

import time
import threading

class SimpleLoader:
    """
    A simple yet effective loading bar and spinner utility.

    Usage:
        - Use `SimpleLoader.loading_bar()` for a progress bar.
        - Use `SimpleLoader.spinning_loader()` for a spinning loader.
        - Copy-paste into your script and start using.
    """
    import sys
    import time
    import threading

    @staticmethod
    def loading_bar(total_steps, prefix='Loading', suffix='Complete', length=50, fill='█', print_end="\r"):
        """
        Displays a progress bar.

        Args:
            total_steps (int): Total steps for completion.
            prefix (str): Prefix string.
            suffix (str): Suffix string.
            length (int): Length of the bar.
            fill (str): Bar fill character.
            print_end (str): End character for print.
        """
        def print_bar(step):
            percent = (step / total_steps) * 100
            filled_length = int(length * step // total_steps)
            bar = fill * filled_length + '-' * (length - filled_length)
            print(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}', end=print_end)

        for step in range(total_steps + 1):
            print_bar(step)
            time.sleep(0.1)  # Simulates work
        print()  # New line after completion

    @staticmethod
    def spinning_loader(duration=5, message='Processing', spinner_chars='|/-\\'):
        """
        Displays a spinning loader.

        Args:
            duration (int): Time duration in seconds.
            message (str): Message to display alongside the spinner.
            spinner_chars (str): Characters to use for the spinner.
        """
        stop_spinner = threading.Event()

        def spinner():
            while not stop_spinner.is_set():
                for char in spinner_chars:
                    print(f'\r{message} {char}', end='', flush=True)
                    time.sleep(0.1)

        spinner_thread = threading.Thread(target=spinner)
        spinner_thread.start()
        time.sleep(duration)
        stop_spinner.set()
        spinner_thread.join()
        print('\rDone!       ')  # Clear the line

# Loading bar example (remove this in your actual script)
SimpleLoader.loading_bar(total_steps=100, prefix='Downloading', suffix='Complete', length=50)

# example usage (remove this in your actual script)
SimpleLoader.spinning_loader(duration=5, message='Processing', spinner_chars='|/-\\')
