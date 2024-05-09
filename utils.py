import os, subprocess, time, sys, threading
from global_vars import stop_thread

TEXT_SPEED = 0.02  # Adjust this value to change the speed of the text

def clear_console():
    """
    Clears the console.
    """
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    
def print_lore(lore):
    global stop_thread  # Declare stop_thread as a global variable
    for text in lore:
        stop_thread = False  # Reset the stop_thread flag
        clear_console()
        print_thread = threading.Thread(target=print_with_delay, args=(text, TEXT_SPEED))
        print_thread.start()
        input("\nPress enter to continue...\n")  # Add a newline character at the end
        stop_thread = True  # Set the stop_thread flag to stop the print_with_delay thread
        print_thread.join()  # Wait for the print_with_delay thread to finish
        
def print_with_delay(text, delay):
    for char in text:
        if stop_thread:
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)