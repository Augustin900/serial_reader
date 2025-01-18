# |- Init file
from init import *

# tell the user that initialization is being performed
print("Performing initialization...")

# init the graphics library
pg.init()

port, baud_rate = create_file()
font = font_init()
screen = display_init()

# tell the user that initialization is complete
print("Initialization complete!")

# clear terminal output
os.system("cls" if os.name == "nt" else "clear")

try:
    # Open the serial port
    ser = Serial(port, baud_rate)
    print(f"Connected to {port} at {baud_rate} baud.")

    disp.set_caption(f"Response from {port}:")

    # running variable
    running = True
        
    while running:
        # get response (if any)
        if ser.in_waiting > 0:
            response = ser.read(ser.in_waiting).decode('utf-8').strip()
        else:
            response = ""

        # draw text to screen
        text_surf, text_rect = font.render(f"{response}", white)

        # check and handle events
        for event in curr_event.get():
            # if the event corresponds to closing the window,
            if event.type == pg.QUIT:
                # we stop and close the program.
                running = False

        screen.fill(black)
        screen.blit(text_surf, text_position)
        pg.display.flip()
        
except SerialException as e:
    print(f"Serial error: {e}")

finally:
    if ser.is_open:
        ser.close()
        print(f"Serial port {port} closed.")

    pg.quit()