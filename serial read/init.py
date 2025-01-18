# |--- Import libraries
# |- Serial communication
from serial import Serial, SerialException

# |- Graphics library
import pygame as pg
import pygame.freetype as ft
import pygame.display as disp
import pygame.event as curr_event

# |- Settings file
from settings import *

# |- Misc libraries
import os, sys
from configparser import ConfigParser

def create_file():
    try:
        # read the config file
        config = ConfigParser()
        config.read(config_file)

        print("Using port and baud rate from configuration file")

        port = config[serial_comment]['port']
        baud_rate = config[serial_comment].getint('baud_rate')

        # check if the file is read
        print("Configuration read!")

        return port, baud_rate

    except FileNotFoundError:
        # Configure the serial port based on user request
        port = input("Port: ")
        baud_rate = input("Baud rate: ")

        with open(config_file, "x") as file:
            file.write(f"[{serial_comment}]")
            file.write(f"port={port}")
            file.write(f"baud_rate={baud_rate}")

        sys.exit()

def display_init():
    # create the window and set title
    screen = disp.set_mode(res)
    disp.set_caption("Serial Reader")

    print("Window initialized!")

    return screen

def font_init():
    # init font
    font = ft.SysFont(font_name, 25)

    print(f"Current font has been successfully initialized: {font}")

    return font