#!/usr/bin/env python3

'''
This is where interesting things will happen.
'''

import tkinter as tk
from tkinter import simpledialog
import datetime


ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="Please reflect on the past week's activities",
                                    prompt="What did you do, and what did you learn?")

print("Reflection ", datetime.datetime.now(), ": ", USER_INP)

# upload the user input to wordpress blog (database? better via django??)
