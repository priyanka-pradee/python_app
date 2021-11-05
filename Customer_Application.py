import tkinter as tk


LARGE_FONT = ("Verdana", 10)


class FetchCustomer(tk.Tk):
    """
    Controller calss to set all the frames
    """

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(fill=None, expand=False)

        self.var = tk.StringVar()
        self.frames = {}
        self.action = None

        for F in (MainPage, InsertDetails, UpdateCustomer, UpdateDetails, SuccessPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        self.title(cont.title)
        self.geometry(cont.geometry)
        frame = self.frames[cont]
        frame.tkraise()

    def update_action(self, action):
        self.action = action
        if action == "NEW":
            self.var.set("Customer Inserted Successfully")
        else:
            self.var.set("Customer Updated Successfully")


class MainPage(tk.Frame):
    """
    The Maon Frame of the customer Portal\
    """

    title = "Cusotmer Portal"
    geometry = "500x100"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        title = "Enter Customer Details"

        label = tk.Label(
            self,
            text="Welcome to Customer Portal!!!",
            font=LARGE_FONT,
            fg="black",
            bg="white",
        )
        label.grid(row=2, column=1, columnspan=3)
        label2 = tk.Label(
            self,
            text="Select the Below actions to Proceed",
            fg="black",
            bg="white",
        )

        label2.grid(row=3, column=1, columnspan=3)

        button1 = tk.Button(
            self,
            text="Create New Customer",
            command=lambda: (
                controller.update_action("NEW"),
                controller.show_frame(InsertDetails),
            ),
        )
        button1.grid(row=4, column=1, padx=50)
        button2 = tk.Button(
            self,
            text="Update Customer Details",
            command=lambda: (
                controller.update_action("UPDATE"),
                controller.show_frame(UpdateCustomer),
            ),
        )
        button2.grid(row=4, column=2, padx=50)


class UpdateCustomer(tk.Frame):
    """
    Frame to enter the customer ID
    """

    title = "Enter Customer Details"
    geometry = "600x100"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        title = "Enter Customer Details"
        label = tk.Label(self, text="Enter Customer ID", fg="black", bg="white")
        label.grid(row=0, column=0)

        customer_id = tk.StringVar()
        e1 = tk.Entry(self, textvariable=customer_id)
        e1.grid(row=0, column=1, padx=50)
        button = tk.Button(
            self,
            text="Fetch & Update Customer Details",
            command=lambda: controller.show_frame(UpdateDetails),
        )
        button.grid(row=0, column=2, padx=50)


class UpdateDetails(tk.Frame):
    """
    Frame to update the details of the customer
    """

    title = "Update Customer Details"
    geometry = "600x275"

    def __init__(self, parent, controller):
        title = "Update Customer Details"
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Update Customer Details!!!")
        # label.pack(pady=0, padx=0)
        # grid layout for the input frame
        # self.columnconfigure(0, weight=1)
        self.columnconfigure(0)
        var = tk.StringVar()
        var.set("Customer Inserted Successfully")
        tk.Label(self, text="First Name:").grid(column=0, row=0, sticky=tk.W)
        keyword = tk.Entry(self, width=40)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)
        tk.Label(self, text="Middle Name:").grid(column=2, row=0, sticky=tk.W)
        keyword = tk.Entry(self, width=40)
        keyword.focus()
        keyword.grid(column=3, row=0, sticky=tk.W)

        tk.Label(self, text="Surname:").grid(column=0, row=1, sticky=tk.W)
        replacement = tk.Entry(self, width=40)
        replacement.grid(column=1, row=1, sticky=tk.W)

        tk.Label(self, text="Phone:").grid(column=2, row=2, sticky=tk.W)
        replacement = tk.Entry(self, width=30)
        replacement.grid(column=3, row=2, sticky=tk.W)

        tk.Label(self, text="Address:").grid(column=0, row=2, sticky=tk.W, rowspan=4)
        # replacement = tk.Entry(self, width=25)
        replacement = tk.Text(self, height=10, width=30)
        replacement.grid(column=1, row=2, rowspan=4, sticky=tk.W)

        # Match Case checkbox
        match_case = tk.StringVar()
        match_case_check = tk.Checkbutton(
            self,
            text="Receive updates",
            variable=match_case,
            command=lambda: print(match_case.get()),
        )
        match_case_check.grid(column=2, row=3, sticky=tk.W)

        button1 = tk.Button(
            self,
            text="Home",
            command=lambda: controller.show_frame(UpdateCustomer),
        )
        button1.grid(row=9, column=2)

        button2 = tk.Button(
            self, text="UPDATE ", command=lambda: controller.show_frame(SuccessPage)
        )
        button2.grid(row=8, column=2)


class InsertDetails(tk.Frame):
    """
    Frame to insert the details of a new customer
    """

    title = "Create  New Customer Details"
    geometry = "600x275"

    def __init__(self, parent, controller):
        title = "New Customer Details"
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Update Customer Details!!!")
        # label.pack(pady=0, padx=0)
        # grid layout for the input frame
        # self.columnconfigure(0, weight=1)
        self.columnconfigure(0)
        var = tk.StringVar()
        var.set("Customer Inserted Successfully")
        tk.Label(self, text="First Name:").grid(column=0, row=0, sticky=tk.W)
        keyword = tk.Entry(self, width=40)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)
        tk.Label(self, text="Middle Name:").grid(column=2, row=0, sticky=tk.W)
        keyword = tk.Entry(self, width=40)
        keyword.focus()
        keyword.grid(column=3, row=0, sticky=tk.W)

        tk.Label(self, text="Surname:").grid(column=0, row=1, sticky=tk.W)
        replacement = tk.Entry(self, width=40)
        replacement.grid(column=1, row=1, sticky=tk.W)

        tk.Label(self, text="Phone:").grid(column=2, row=2, sticky=tk.W)
        replacement = tk.Entry(self, width=30)
        replacement.grid(column=3, row=2, sticky=tk.W)

        tk.Label(self, text="Address:").grid(column=0, row=2, sticky=tk.W, rowspan=4)
        # replacement = tk.Entry(self, width=25)
        replacement = tk.Text(self, height=10, width=30)
        replacement.grid(column=1, row=2, rowspan=4, sticky=tk.W)

        # Match Case checkbox
        match_case = tk.StringVar()
        match_case_check = tk.Checkbutton(
            self,
            text="Receive updates",
            variable=match_case,
            command=lambda: print(match_case.get()),
        )
        match_case_check.grid(column=2, row=3, sticky=tk.W)

        button1 = tk.Button(
            self,
            text="Home",
            command=lambda: controller.show_frame(UpdateCustomer),
        )
        button1.grid(row=9, column=2)

        button2 = tk.Button(
            self,
            text="Create Customer ",
            command=lambda: controller.show_frame(SuccessPage),
        )
        button2.grid(row=8, column=2)


class SuccessPage(tk.Frame):
    """
    Success page of a customer
    """

    title = "Customer Details Updated Successfully"
    geometry = "500x100"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

      label = tk.Label(self, text= "Folder Validated Successfully", font=LARGE_FONT)

        label.grid(row=0, column=1, columnspan=3, padx=100, pady=20)
        button1 = tk.Button(
            self,
            text=" Home",
            command=lambda: controller.show_frame(MainPage),
        )
        button1.grid(row=1, column=1, padx=200)

if __name__ == "__main__":
    app = FetchCustomer()
    app.mainloop()
