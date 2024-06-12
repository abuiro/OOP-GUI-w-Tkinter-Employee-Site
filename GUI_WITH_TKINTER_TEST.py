import tkinter as tk
from tkinter import ttk
import csv

class AddUser(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller

        self.the_name = tk.StringVar()
        self.emp_name = tk.StringVar()
        self.employee_name = tk.StringVar()


        self.check_working = tk.IntVar()
        self.temp_message = tk.StringVar()

        self.create_add_user_widgets()

    def create_add_user_widgets(self):
        self.left = tk.Frame(self)
        self.left.grid(row=0, column=0)

        self.right = tk.Frame(self)
        self.right.grid(row=0, column=1)

        self.enter_name = ttk.Label(self.left, text="Enter an Employee name:")
        self.enter_name.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.emp_name)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5)

        self.enter_name = ttk.Label(self.left, text="What is the employees level?(Associate, Supervisor, or Executive): ")
        self.enter_name.grid(row=2, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=3, column=0, padx=5, pady=5)

        self.enter_name = ttk.Label(self.left, text="What date was the employee hired?(Year-Month-Day): ")
        self.enter_name.grid(row=4, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.employee_name)
        self.name_entry.grid(row=5, column=0, padx=5, pady=5)

        self.enter_name = ttk.Label(self.left, text="What is the employees pay?: ")
        self.enter_name.grid(row=6, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=7, column=0, padx=5, pady=5)

        self.enter_name = ttk.Label(self.left, text="What is the employees job position?: ")
        self.enter_name.grid(row=8, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=9, column=0, padx=5, pady=5)

        self.enter_name = ttk.Label(self.left, text="What is the project this employee is workng: ")
        self.enter_name.grid(row=10, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=11, column=0, padx=5, pady=5)


        self.enter_name = ttk.Label(self.left, text="What date did the employee depart if they did?: ")
        self.enter_name.grid(row=12, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=13, column=0, padx=5, pady=5)

        self.click_btn = ttk.Button(self.left, text="Add User", command=lambda: self.controller.show_frame(MainPage))
        self.click_btn.grid(row=14, column=0, padx=5, pady=5)


        # level = input("What is the employees level?(Associate, Supervisor, or Executive): ")
        # date_hired = input("What date was the employee hired?(Year-Month-Day): ")
        # pay = input("What is the employees pay?: ")
        # job_position = input("What is the employees job position?: ")
        # project = input("What is the project this employee is workng: ")
        # date_departed = input("What date did the employee depart if they did?: ")

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.the_name = tk.StringVar()
        self.check_working = tk.IntVar()
        self.temp_message = tk.StringVar()


        self.create_label()

    def create_label(self):
        
        self.left = tk.Frame(self)
        self.left.grid( row=0, column=0)

        self.right = tk.Frame(self)
        self.right.grid( row=0, column=1)
        
        self.enter_name = ttk.Label(self.left, text="Here are the Menu Options:")
        self.enter_name.grid(row=0, column=0, padx=5, pady=5)

        self.log = tk.Listbox(self.right, width=30)
        self.log.grid(row=1, column=1, padx=5, pady=5)
        for item in self.controller.employees:
            if(item.employee=="Name"):
                print(item.employee)
            else:
                self.log.insert(tk.END, item.employee)


        self.employee_list()

    def employee_list(self):

        self.click_btn = ttk.Button(self.left, text="Add new employee", command=lambda: self.controller.show_frame(AddUser))
        self.click_btn.grid(row=1, column=0, padx=5, pady=5)

        self.click_btn = ttk.Button(self.left, text="Delete employee", command=lambda: self.click_delete())
        self.click_btn.grid(row=2, column=0, padx=5, pady=5)

        self.click_btn = ttk.Button(self.left, text="Save Employees to a csv file")
        self.click_btn.grid(row=3, column=0, padx=5, pady=5)

        self.click_btn = ttk.Button(self.left, text="Quit Application")
        self.click_btn.grid(row=4, column=0, padx=5, pady=5)

    def create_widgets(self):
        self.left = tk.Frame(self)
        self.left.grid(row=0, column=0)

        self.right = tk.Frame(self)
        self.right.grid(row=0, column=1)

        self.enter_name = ttk.Label(self.left, text="Enter a name:")
        self.enter_name.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.left, width=12, textvariable=self.the_name)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5)

        self.click_btn = ttk.Button(self.left, text="Add to list", command=self.click_me)
        self.click_btn.grid(row=1, column=1, padx=5, pady=5)

        self.tk_button = tk.Button(self.left, text="Delete Last", command=self.click_delete)
        self.tk_button.grid(row=2, column=1, padx=5, pady=5)

        self.log = tk.Listbox(self.right, width=30)
        self.log.grid(row=1, column=1, padx=5, pady=5)
        for item in ['top', 'next']:
            self.log.insert(tk.END, item)

        self.help_button = tk.Button(self.right, text='Help', command=lambda: self.controller.show_frame(HelpPage))
        self.help_button.grid(row=2, column=2)

    def click_me(self):
        if self.name_entry.get():  # same as != ''
            self.log.insert(tk.END, self.name_entry.get())

    def click_delete(self):
        print('TK END: ' + tk.END)
        self.log.delete(tk.START)
        
class Application(tk.Tk):

    employees = []


    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.title(title)
        #self.geometry("600x400+450+300")
        

        self.load_employees()
        print(self.employees[1].employee)

        self.main_container = tk.Frame(self)    # include self???
        self.main_container.grid(row=0, column=0)

        self.window_config = {    
            'MainPage' : ('Main Page', "600x400+450+300"),
            'AddUser' : ('Add User Page', "")

        }
        self.all_frames = {} #organizes frames for switching
        for each_frame in (MainPage,AddUser,DeleteUser):
            frame = each_frame(self.main_container, self)  # self is the CONTROLLER
            self.all_frames[each_frame] = frame
            frame.grid(row=0, column=0, sticky='nsew')  #  sticky='nsew' overlaps the other frame
        self.show_frame(MainPage)
        #self.create_label()

    def show_frame(self, the_page):
        if the_page == MainPage:
            self.set_title_geometry(self.window_config['MainPage'][0], self.window_config['MainPage'][1])
        elif the_page == AddUser:
            print("In the Add User elif statement")
            self.set_title_geometry(self.window_config['AddUser'][0], self.window_config['AddUser'][1])
        
        
        self.all_frames[the_page].tkraise()

    def set_title_geometry(self, title, geometry, resize=True):
        self.title(title)
        self.geometry(geometry)
        self.resizable(resize, resize)

    def load_employees(self):
        with open('tiny.csv','r') as f:
            employee_file = csv.reader(f)
            for Name,Level,Project,Date_Hired,Pay,Job_Position,Date_Departed in employee_file:
                self.employees.append(Employee(Name,Level,Project,Date_Hired,Pay,Job_Position,Date_Departed))

    def DeleteEmployee(self,name):
        #Deletes the employee that the user wishes to delete
        for emp in self.employees:
            if emp.employee == name:
                self.employees.remove(emp)
    


    

class Employee():
    
    """
    purpose: Initializes the member/levels/sections of an employee in the list
    
    attributes: employee ;; str
                level ;; str
                project ;; str
                date_hired ;; str
                pay ;; str
                job_position ;; str
                date_departed ;; str
    """

    #Initialization of the employee class
    def __init__(self,employee,level,project,dateHired,pay,jobPosition,dateDeparted):
        #initializing the members
        self.employee = employee
        self.level = level
        self.project = project
        self.dateHired = dateHired
        self.pay = pay
        self.jobPosition = jobPosition
        self.dateDeparted = dateDeparted

    




class DeleteUser(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller

        self.delete_user_widgets()


    def delete_user_widgets(self):

        self.user_detail_frame = ttk.LabelFrame(self, text="Enter Employee Details")
        




        

   



my_app = Application('Acme Employee List')
my_app.mainloop()

