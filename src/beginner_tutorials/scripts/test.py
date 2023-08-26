import pygame
import time

# Initialize pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joysticks found.")
    pygame.quit()
else:
    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Joystick detected:", joystick.get_name())

    try:
        # Main loop
        while True:
            pygame.event.pump()  # Process events

            # Get the values of axes
            axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
            print("Axes:", axes)

            # Get the values of buttons
            buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
            print("Buttons:", buttons)

            # Quit the loop if the 'PS' button is pressed (button index might vary)

            if buttons[16] == 1:
                break
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    # Clean up
    joystick.quit()
    pygame.quit()