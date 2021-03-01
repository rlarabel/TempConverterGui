import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # To change default window size, you can add code below:
        # “self.main_window” is the variable name of the main window.
        # self.main_window.geometry("250x150")
        # Create two frames: one for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='F to C', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='C to F', variable=self.radio_var, value=2)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()

        # Create a prompt label, an entry widget for temperature input,
        # and another label that is tied to a StringVar object and will
        # display the converted temperature after conversion is performed.
        # See StringVar example in "kilo_converter2.py"
        self.prompt_label = tkinter.Label(self.middle_frame, text='Enter a Temperature you want to convert:')
        self.conv_entry = tkinter.Entry(self.middle_frame, width=10)
        self.descr_label = tkinter.Label(self.middle_frame, text='Converted temp:')
        # to store a string of blank characters.
        self.value = tkinter.StringVar()
        self.output_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # Pack labels and entry widgets
        self.prompt_label.pack(side='left')
        self.conv_entry.pack(side='left')
        self.descr_label.pack(side='left')
        self.output_label.pack(side='left')

        # Create a Convert button and a Quit button.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method below is the callback function for the Convert
    # button. F to C and C to F conversions are performed depending on value
    # in Entry widget. If value is 0 (i.e. user selects Convert button
    # without selecting a radio button), display an appropriate message in
    # an info message box.
    # NOTE: METHOD SOULD BE IN YOUR GUI CLASS!
    def convert(self):
        if self.radio_var.get() == 1:
            old_temp = float(self.conv_entry.get())
            new_temp = (old_temp - 32) * (5 / 9)
        elif self.radio_var.get() == 2:
            old_temp = float(self.conv_entry.get())
            new_temp = old_temp * (9/5) + 32
        else:
            tkinter.messagebox.showinfo('You made no conversion selection\nor something else went wrong')
            new_temp = -999

        self.value.set(new_temp)


Temp_conv = MyGUI()
