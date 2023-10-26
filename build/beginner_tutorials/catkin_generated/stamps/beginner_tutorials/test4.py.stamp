from pynput import keyboard

def on_key_press(key):
    try:
        # Handle key press event
        print(f'Key pressed: {key.char}')

    except AttributeError:
        # Some special keys don't have a `char` attribute
        print(f'Special key pressed: {key}')

def on_key_release(key):
    # Handle key release event
    print(f'Key released: {key}')

# Create a listener that listens for both key presses and key releases
with keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release) as listener:
    listener.join()