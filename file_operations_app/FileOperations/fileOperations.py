import glob
import os
import tkinter as tk
import tkinter.filedialog
from collections import defaultdict
from tkinter import messagebox
from zipfile import ZipFile

import csv_processing as process_csv
import output_generation as output_gen

LARGE_FONT = ("Verdana", 10)


class MainPage(tk.Frame):
    """
    The Main Frame of the File Validation
    """

    title = "File Operation App"
    geometry = "500x150"

    def validate_input(self, controller):
        zip_file = glob.glob(self.dirname.get() + "/*.zip")
        if not self.dirname.get():
            messagebox.showerror("Error Dialog", "Input Folder cannot be blank")
            return
        if not self.output_dirname.get():
            messagebox.showerror("Error Dialog", "Output  Folder cannot be blank")
            return
        zip_file = glob.glob(self.dirname.get() + "/*.zip")
        if not zip_file:
            messagebox.showerror(
                "Error Dialog", "Input Folder does not contain any zip files"
            )
            return
        else:
            self.process(controller, zip_file)

    def process(self, controller, zip_file):

        # load all zip files in folder
        for filename in zip_file:

            zip_file = ZipFile(filename)
            csv = [
                text_file.filename
                for text_file in zip_file.infolist()
                if text_file.filename.endswith("customer.csv")
                or text_file.filename.endswith("structure.csv")
            ]

            if len(csv) == 2:
                for text_file in csv:
                    validation_errors = process_csv.do_csv_validation(
                        zip_file, text_file
                    )

                    print(validation_errors)
                    print(type(controller.errors))
                    controller.errors[text_file] = validation_errors
                    print(controller.errors)
            elif len(csv) == 0:
                controller.errors[filename] = [
                    "No CSVs ending with structure and customer found"
                ]
            else:
                controller.errors[filename] = ["More than 2 CSV found"]
            print(controller.errors)
        controller.output_dirname = self.output_dirname.get()
        output_gen.generate_error(controller.errors, controller.output_dirname)

        controller.show_frame(SuccessPage)

    def get_dirname(self):
        dname = tk.filedialog.askdirectory()
        if dname:
            self.dirname.set(dname)

    def get_output_dirname(self, filepath, controller):
        dname = tk.filedialog.askdirectory(initialdir=filepath)
        if dname:
            self.output_dirname.set(dname)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = "Enter Customer Details"
        self.dirname = tk.StringVar()

        labelFile = tk.Label(self, text="Select Input Folder")
        labelFile.grid(row=0, column=0)
        lbl1 = tk.Entry(self, textvariable=self.dirname, width=50)
        lbl1.grid(row=1, column=0, padx=10)  #
        button1 = tk.Button(self, text="Browse", command=lambda: self.get_dirname())
        button1.grid(row=1, column=1)
        self.output_dirname = tk.StringVar()
        self.output_dirname.set(os.path.dirname(os.path.realpath(__file__)))
        outputLabel = tk.Label(self, text="Select Output Folder")
        outputLabel.grid(row=2, column=0)
        lbl2 = tk.Entry(self, textvariable=self.output_dirname, width=50)
        lbl2.grid(row=3, column=0)  #
        button1 = tk.Button(
            self,
            text="Browse",
            command=lambda: self.get_output_dirname(
                self.output_dirname.get(), controller
            ),
        )
        button1.grid(row=3, column=1)
        button2 = tk.Button(
            self,
            text="Proceed and Validate my data",
            command=lambda: self.validate_input(controller),
        )
        button2.grid(row=4, column=0)


class SuccessPage(tk.Frame):
    """
    Success page
    """

    title = "Folder Validated  Successfully"
    geometry = "500x150"

    def open_window(self, controller):
        command = "explorer.exe " + controller.output_dirname
        os.system(command)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Folder and Files Validated Successfully", font=LARGE_FONT
        )

        label.grid(row=0, column=1, columnspan=3, padx=100, pady=20)
        button1 = tk.Button(
            self,
            text=" Home",
            command=lambda: controller.show_frame(MainPage),
        )
        button1.grid(row=1, column=1, padx=200)

        label1 = tk.Button(
            self,
            text="Open Output Folder",
            command=lambda: self.open_window(controller),
        )
        label1.grid(row=3, column=1, padx=200)


class FileOperation(tk.Tk):
    """
    Controller calss to set all the frames
    """

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(fill=None, expand=False)

        self.output_dirname = None
        self.frames = {}
        self.errors = dict()
        for F in (MainPage, SuccessPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        self.title(cont.title)
        self.geometry(cont.geometry)
        frame = self.frames[cont]
        frame.tkraise()
