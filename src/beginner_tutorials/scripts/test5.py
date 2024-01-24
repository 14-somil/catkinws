import pygame
import time
import sys

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("PS4 Controller Input")

# Initialize the joystick
if (pygame.joystick.get_count() == 0):
    print('No joystick found.')
    sys.exit()
# joystick = None
# for i in range(pygame.joystick.get_count()):
#     if "Wireless Controller" in pygame.joystick.Joystick(i).get_name():  # Adjust the name as needed
#         joystick = pygame.joystick.Joystick(i)
#         joystick.init()
joystick = pygame.joystick.Joystick(0)
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if joystick:
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
        hats = [joystick.get_hat(i) for i in range(joystick.get_numhats())]

        # Adjust the index for the D-pad (hat) based on your controller
        d_pad = joystick.get_hat(0)

        print("Axes:", axes)
        print("Buttons:", buttons)
        print("Hats:", hats)
        print("D-pad:", d_pad)
        time.sleep(0.01)

    # Clear the screen
    # screen.fill((0, 0, 0))
    # pygame.display.flip()

# Quit pygame
pygame.quit()
