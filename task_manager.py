# import libraries you will use in the program at the top of the program
# use math to replicate the '_' to divide task sections
# use sys to exit the program
# use datetime to get the task deadline
# use datetime to get the current date
import math
import sys
import datetime
from datetime import datetime 

#● Modify the code of your previous project so that functions are used.
#Adding functions will improve the modularity of your code. Your program
#should include at least the following functions:
#    o reg_user — that is called when the user selects ‘r’ to register a user.
#    o add_task — that is called when a user selects ‘a’ to add a new task.
#    o view_all — that is called when users type ‘va’ to view all the tasks
#    listed in ‘tasks.txt’.
#    o view_mine — that is called when users type ‘vm’ to view all the
#    tasks that have been assigned to them.

# modify the function called reg_user to ensure usernames do not duplicate when adding a new user to user.txt.
# use an if statement to recognise a username that is already registered
# if the username already exists in user.txt, print out an error message
# allow the user to try and add a user with a different username
# call the register function again to restart the registration process
def reg_user():
    print(" ")
    username_request = input("Please enter new username:\t").lower()
    if username_request in user_list:
        print("That username already exists. Please enter a different name.")
        reg_user()

    password_request = input("Please enter your passsword:\t").lower()
    confirm_new_password = input("Please confirm your passsword:\t").lower()

    if password_request == confirm_new_password:
        login_details = []
        login_details.append(username_request)
        login_details.append(password_request)
        login_details_joined = ", ".join(str(item) for item in login_details)
        f = open('user.txt', 'a')
        f.write("\n")
        f.writelines("".join(login_details_joined))
        f.close()        
    
    else:
        print("\nThe request is invalid. Please try again.")

def add_task():
    task_entry = []
    whose_task = input("\nPlease enter the username the task is for:\t")
    task_entry.append(whose_task)
    task_title = input("Please enter the title of the task:\t")
    task_entry.append(task_title)
    task_description = input("Please describe the task:\t")
    task_entry.append(task_description)
    import datetime
    while True:
        task_deadline = input("Please enter the task deadline formatted as DD/MM/YYYY:\t")
        try:
            month_name = datetime.datetime.strptime(task_deadline, "%d/%m/%Y").date()
            break
        except ValueError:
            print("That entry was invalid. Please try again.")        
    deadline_formatted = month_name.strftime("%d %b %Y")
    task_entry.append(deadline_formatted)
    from datetime import datetime 
    current_date = datetime.today().strftime('%d %b %Y')
    task_entry.append(current_date)
    task_status = "No"
    task_entry.append(task_status)
    task_entry_joined = ", ".join(str(item) for item in task_entry)
    f2 = open('tasks.txt', 'a')
    f2.write("\n")
    f2.writelines("".join(task_entry_joined))
    f2.close()

def view_all():
    with open('tasks.txt', 'r') as f3:
        for line in f3:
            task_entry_list = line.split(", ")
            task_entry_list = [x.strip() for x in task_entry_list]
            print("_" * 100)
            task = task_entry_list[1]
            print(f"\nTask:\t\t{task}")
            assigned_to = task_entry_list[0]
            print(f"Assigned to:\t{assigned_to}")
            date_assigned = task_entry_list[3]
            print(f"Date assigned:\t{date_assigned}")
            due_date = task_entry_list[4]
            print(f"Due date:\t{due_date}")
            task_complete = task_entry_list[5]
            print(f"Task complete?\t{task_complete}")
            task_description = task_entry_list[2]
            print(f"Task description: \n {task_description}")
        f3.close()

# add a functionality that displays all tasks in a manner that is easy to read in view_mine()
# ensure each task can be identified by a number with a for loop
# assign a counter variable that increases by 1
# create a list from each line with split() then strip() whitespaces
def view_mine():
    f4 = open('tasks.txt', 'r')
    count = 0
    for line in f4:
        task_entry_list = line.split(", ")
        task_entry_list = [x.strip() for x in task_entry_list]
        count += 1 
        if username_request == task_entry_list[0]:
            print("_" * 100)
            task = task_entry_list[1]
            print("\nTask " + str(count) + f":\t\t{task}")
            assigned_to = task_entry_list[0]
            print(f"Assigned to:\t{assigned_to}")
            date_assigned = task_entry_list[3]
            print(f"Date assigned:\t{date_assigned}")
            due_date = task_entry_list[4]
            print(f"Due date:\t{due_date}")
            task_complete = task_entry_list[5]
            print(f"Task complete?\t{task_complete}")
            task_description = task_entry_list[2]
            print(f"Task description: \n {task_description}")            

    f4.close()
    task_edit_opt()
    
# Add the following functionality when the user selects ‘vm’ to view all the
# tasks assigned to them:
# create a function to edit a user's task    
# open the tasks.text in read & write mode so that the user_task_list will write over the previous data
# assign an empty list for a user's list of tasks
# assign a counter variable
def task_edit_opt():
    f4a = open('tasks.txt', 'r')    
    user_task_list = []
    count = 0

# use a for loop to iterate over the task details and create a list with split()
# use a for loop to strip() to remove whitespaces at the start/end of a str
# append the task entry to the user's task list
# increase the counter variable by 1
# print out the user's task list
    for line in f4a:
        task_entry_list = line.split(", ")
        task_entry_list = [x.strip() for x in task_entry_list]        
        user_task_list.append(task_entry_list)
        count += 1
    print()     

# request the user to input a task number to edit or ‘-1’ to return to the main menu
# cast the input to an int
# use if-elif-else statement for conditions according to the int
    opt_to_edit = int(input('''\nPlease enter the number of the task you want to edit.
Alternatively, enter '-1' to return to the main menu.\n:
'''))

# if the user inputs -1, call the main menu function    
    if opt_to_edit == -1:
        print()
        main_menu()

# elif the input is larger than the number of available task, print out an error message
# call the funtion to edit the task again
    elif opt_to_edit > len(user_task_list):
        print("The task number is not in the view mine list.")
        task_edit_opt()

# else the user selects a specific task, they should be able to choose to
# either mark the task as complete or edit the task
# request the user to input their selection
    else:
        idx_to_edit = int(input('''
Enter the corresponding letter for the option to edit.
1) Mark the task as complete.
2) Edit the username.
3) Edit the date for the task. \n:
'''))

# If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that
# describes whether the task has been completed or not should be changed to ‘Yes’.
# use if-elif-else statement for conditions according to the edit option selected
# if task completion was selected and the index from the task list says incomplete,
# overwrite the index to 'yes'
# deduct 1 from the option to edit as the task iterates and the value is increased by one
# use a for loop & join() to remove the list function
# remember to use '\n' to join each task and ', ' to join each entry in the task
# open the tasks.txt in write mode to write all tasks including the edited task to the document
        if (idx_to_edit == 1) and (user_task_list[opt_to_edit - 1][5] == 'No'):
            user_task_list[opt_to_edit - 1][5] = "Yes"
            user_task_list_joined = "\n".join(", ".join(item) for item in user_task_list)
            print()
            with open('tasks.txt', 'w') as f4b:                
                f4b.write(user_task_list_joined)
            f4b.close()

# elif the user selects to assign another user to the task and the task is incomplete,
# request the user to input a new username
# overwrite the variable index for the username from the task list
# use a for loop to use join() to remove the list function
# remember to use '\n' to join each task and ', ' to join each entry in the task
# open the tasks.txt in write mode to write all tasks including the edited task to the document
        elif idx_to_edit == 2 and (user_task_list[opt_to_edit - 1][5] == 'No'):
            print()
            user_task_list[opt_to_edit - 1][0] = input("Enter the username who will complete this task instead:\t")
            user_task_list_joined = "\n".join(", ".join(item) for item in user_task_list)
            with open('tasks.txt', 'w') as f4b:
                f4b.write(user_task_list_joined)
            f4b.close()
            
# elif the due date of the task can be edited if the task index says incomplete
# print out that the dates in the task list will update
# import the datetime module to get the the current date and format it with %d %b %Y
# overwrite the current date task index variable
# printout the current date
        elif idx_to_edit == 3 and (user_task_list[opt_to_edit - 1][5] == 'No'):
            print()
            print("The current date that this task alters and the new deadline will update next.")
            from datetime import datetime
            new_date_assigned = datetime.today().strftime('%d %b %Y')
            user_task_list[opt_to_edit - 1][3] = new_date_assigned
            print()
            print("The current date:", user_task_list[opt_to_edit - 1][3])
            print()            

# request the user to input the new deadline for the task
# use a try-except block as defense againt incorrect date format entry
# import the datetime module to take the date and format it with %d %m %Y
# overwrite the current deadline task index variable
# printout the new deadline
# use a for loop to join() the items to remove the list function
# remember to use '\n' to join each task and ', ' to join each entry in the task
# open the tasks.txt in write mode
# write the updated task entry to the text document
            while True:
                new_due_date = input("Please enter the new task deadline formatted as DD/MM/YYYY:\t")
                try:
                    month_name = datetime.datetime.strptime(new_due_date, "%d/%m/%Y").date()
                    break
                except ValueError:
                    print("That entry was invalid. Please try again.")
            
            print()
            import datetime
            month_name = datetime.datetime.strptime(new_due_date, "%d/%m/%Y").date()
            user_task_list[opt_to_edit - 1][4] = month_name.strftime("%d %b %Y")
            print("New deadline:", user_task_list[opt_to_edit - 1][4])
            user_task_list_joined = "\n".join(", ".join(item) for item in user_task_list)
            
            with open('tasks.txt', 'w') as f4b:
                f4b.write(user_task_list_joined)
            f4b.close()

# the task can only be edited if it has not yet been completed
# print out an error message if the task is complete
# call the funtion to choose to edit a task again
        else:
            print("This task is complete and cannot edit.")
            task_edit_opt()

# close the text document                    
    f4a.close()
    
# Add an option to generate reports to the main menu of the application.
# create a function called generate_reports
# open task_overview.txt in write mode and enter an opening statement
# The menu for the admin user should now look something like this:
#   When the user chooses to generate reports, two text files, called
#   task_overview.txt and user_overview.txt, should be generated.
#   Both these text files should output data in a user-friendly, easy to read manner.
#    o task_overview.txt should contain:  
def generate_reports():
    with open('task_overview.txt', 'w') as g:
        g.write("The following report is from data gathered on tasks created.\n")
        line = "_" * 100
        g.write(f"{line}\n\n")
        
#        ▪ The total number of tasks that have been generated and tracked using the task_manager.py.
# open tasks.txt in read mode
# assign a variable to find the length of readlines()
# write the value to task_overview.txt
        with open('tasks.txt', 'r') as t:
            total_tasks = len(t.readlines())
            g.write(f"The total number of tasks that have been generated and tracked using the task_manager.py:\n{total_tasks}\n")
            g.write("\n")

#        ▪ The total number of completed tasks.
# open tasks.txt in read mode [note: had to repeatedly use 'with open as' because doc kept closing after each subsection]
# use read() and count() to find the occurrence of yes that indicates complete
# write the value to task_overview.txt
#        ▪ The total number of uncompleted tasks.
# use read() and count() to find the occurrence of no that indicates incomplete
# write the value to task_overview.txt
        with open('tasks.txt', 'r') as t:
            read_t = t.read()
            num_of_complete = read_t.count("Yes")
            g.write(f"The total number of completed tasks:\n{num_of_complete}\n")
            g.write("\n")

            num_of_incomplete = read_t.count("No")
            g.write(f"The total number of incomplete tasks:\n{num_of_incomplete}\n")
            g.write("\n")

#        ▪ The total number of tasks that haven’t been completed and that are overdue.
# open tasks.txt in read mode
# create an empty list for tasks
# use a for loop to strip() and split() tasks
# append() the tasks to the list
        with open('tasks.txt', 'r') as t:
            t_list = []            
            for line in t:
                split_t = line.strip().split(", ")
                t_list.append(split_t)
                        
# use datetime module to fetch dates
# find current date with today() and strftime('%d %b %Y') followed by strptime() to display correct format
# use a for loop to count the occurrence of an incomplete task past its deadline
# format the dealine from the list index with strptime() so that dates can be compared with current date
# use if else statements to increase the count for overdue tasks
# write the count of overdue tasks to task_overview.txt
            from datetime import datetime
            current_date = datetime.today().strftime('%d %b %Y')
            current_date_formatted = datetime.strptime(current_date, '%d %b %Y')
            num_overdue_tasks = 0
            for entry in t_list:
                due_date = entry[4]
                due_date_formatted = datetime.strptime(due_date, '%d %b %Y')
                
                if (entry[5] == 'No'):
                    if (current_date_formatted > due_date_formatted):
                        num_overdue_tasks += 1

        g.write(f"The total number of tasks that haven’t been completed and that are overdue:\n{num_overdue_tasks}\n")
        g.write("\n")

#       ▪ The percentage of tasks that are incomplete.
# assign a variable to calculate percentage. divide the number of incomplete tasks by the total tasks and multiply by 100
# round the percentage to 2 decimals
# write the percentage to task_overview.txt
        percentage_incomplete_tasks = round((num_of_incomplete / (num_of_complete + num_of_incomplete)) * 100, 2)
        g.write(f"The percentage of tasks that are incomplete:\n{percentage_incomplete_tasks}%\n")
        g.write("\n")

#        ▪ The percentage of tasks that are overdue.
# assign a variable to calculate percentage. divide the number of overdue tasks by the total tasks and multiply by 100
# round the percentage to 2 decimals
# write the percentage to task_overview.txt
        percentage_overdue_tasks = round((num_overdue_tasks / (num_of_complete + num_of_incomplete)) * 100, 2)
        g.write(f"The percentage of tasks that are overdue:\n{percentage_overdue_tasks}%\n")
    t.close()
    g.close()
    
# open user_overview.txt in write mode
# write an opening statement
    with open('user_overview.txt', 'w') as o:
        o.write("The following report is from data gathered on users created.\n")
        line = "_" * 100
        o.write(f"{line}\n\n")

#    o user_overview.txt should contain:
#        ▪ The total number of users registered with task_manager.py.
# open user.txt in read mode
# assign a variable to find the len() of lines in text doc with readlines()
# write the value to user_overview.txt
        with open('user.txt', 'r') as u:
            num_of_users = len(u.readlines())
            o.write(f"The total number of users registered with task_manager.py:\n{num_of_users}\n")
            o.write("\n")

#        ▪ The total number of tasks that have been generated and tracked using the task_manager.py.
# open tasks.txt in read mode
# assign a variable to find the len() of lines in text doc with readlines()
# write the value to user_overview.txt
        with open('tasks.txt', 'r') as t:
            total_tasks = len(t.readlines())
            o.write(f"The total number of tasks that have been generated and tracked using the task_manager.py:\n{total_tasks}\n")
            o.write("\n")
            o.write("=" * 100)
            o.write("\n")

# ▪ For each user also describe: 
#   ▪ The total number of tasks assigned to that user.
#   ▪ The percentage of the total number of tasks have been assigned to that user
#   ▪ The percentage of the complete tasks assigned to that user 
#   ▪ The percentage of unfinished tasks assigned to the user
#   ▪ The percentage of the tasks assigned to the user that are incomplete and overdue
# open tasks.txt and user.txt in read mode and use a for loop to create a list of lines
# use split() and strip() for the list
# append to the empty lists that are outside loop to avoid error ref before assignment                
        with open('tasks.txt', 'r') as t:             
            task_entry_list = []
            for line in t:
                task_entries = line.strip().split(", ")
                task_entry_list.append(task_entries)
                
        with open('user.txt', 'r') as u:
            user_list = []
            for line in u:
                user_entries = line.strip().split(", ")
                user_list.append(user_entries)                                

# set a counter for all variables within a for loop in the range of users registered
# use the datetime module to find the current date with today()
# format the date with strftime() and strptime() to let it be comparable with other dates [cannot leave as a str]
# use an if-statement to increase the counter each time the user's tasks are found
        for user in range(0, len(user_list)):
            user_task_count = 0
            user_tasks_complete_count = 0
            user_incomplete_tasks_count = 0
            from datetime import datetime
            current_date = datetime.today().strftime('%d %b %Y')
            current_date_formatted = datetime.strptime(current_date, '%d %b %Y')
            num_user_overdue_tasks = 0

# use a nested for loop in the range of task lists
# to print data for all users check that users match to their tasks if usernames match
# note using if-elif results in incorrect % calculations - had to be if only for all
# if users have a task, increase counter by 1
# if users have completed tasks, increase counter by 1
# use an if-statement to select a user's incomplete tasks
# increase the counter by 1 if the current date is after the deadline
# format the deadline index with strptime() inside nested for loop
# use nested if-statement to increase counter by 1 for a user's overdue tasks
            for task in range(0, len(task_entry_list)):
                if user_list[user][0] == task_entry_list[task][0]:
                    user_task_count += 1
                    
                if user_list[user][0] == task_entry_list[0] and task_entry_list[task][-1] == 'Yes':
                    user_tasks_complete_count += 1
                    
                if user_list[user][0] == task_entry_list[task][0] and task_entry_list[task][-1] == 'No':
                    user_incomplete_tasks_count += 1
                                                
                if user_list[user][0] == task_entry_list[task][0] and task_entry_list[task][-1] == 'No':
                    due_date = task_entry_list[task][4]
                    due_date_formatted = datetime.strptime(due_date, '%d %b %Y')
                    if (current_date_formatted > due_date_formatted):
                        num_user_overdue_tasks += 1

# assign variables to calculate each percentage
# divide the number of user's tasks by the value of all tasks and multiply by 100
# divide the user's amount of complete tasks by the user's total tasks and multiply by 100
# divide the number of incomplete tasks by the user's total tasks and multiply by 100
# divide the number of a user's overdue tasks by the user's total tasks and multiply by 100
# round all the percentages to 2 decimals                
            percentage_user_tasks = round((user_task_count / total_tasks) * 100, 2)                                                
            percentage_of_user_tasks_complete = round((user_tasks_complete_count / user_task_count) * 100, 2)
            percentage_of_user_tasks_incomplete = round((user_incomplete_tasks_count / user_task_count) * 100, 2)
            percentage_user_overdue_tasks = round((num_user_overdue_tasks / user_task_count) * 100, 2)

# write the percentages to user_overview.txt outside the for loops
            o.write(f'''\n-{user_list[user][0]}-

The total number of tasks assigned to {user_list[user][0]}:\n{user_task_count}

The percentage of the total number of tasks assigned to {user_list[user][0]}:\n{percentage_user_tasks}%

The percentage of {user_list[user][0]}'s tasks which are complete:\n{percentage_of_user_tasks_complete}%

The percentage of {user_list[user][0]}'s tasks which are incomplete:\n{percentage_of_user_tasks_incomplete}%

The percentage of {user_list[user][0]}'s tasks that are overdue:\n{percentage_user_overdue_tasks}%
''')
            o.write("~" * 100)

# close the text documents             
    o.close()
    u.close()
    t.close()            
                            
#######################################################################################################

# open and then modify the Task19template.py, and rename it task_manager.py
# design a program that manages tasks for a small business
print('''Create a program for a small business.
It will help to manage tasks assigned to each member of the team.
''')

# open the user text file in read mode
# read the file
# create a list from the users with split and remove \n from each line
# create a login variable == false 
# use a while not loop for the login to continue the while loop if login is incorrect
# request the user to input their login details (i.e. username/password)
# use if-elif to create conditions for login
# if the username does not match a user in the list, display an error message
# elif the password does not match that in the list, display an error message
# elif the login is correct overwrite the variable to true to break the while loop
# and print a message to continue with the program
with open('user.txt', 'r') as f:
    read_users = f.read()
    user_list = read_users.replace("\n", ", ").split(", ")

login_success = False
while not login_success:
    username_request = input("\nPlease enter your username:\t").lower()
    password_request = input("Please enter your passsword:\t").lower()
    if username_request not in user_list:
        print("\nIncorrect username. Please try again.")

    elif password_request not in user_list:
        print("\nIncorrect password. Please try again.")
            
    elif username_request in user_list and password_request in user_list:
        login_success = True
        print("\nWelcome to the task manager.\n")

# use a boolean while loop to display the menu for task management
# use if-else to give an input option dependant on an admin login
# only the admin user is provided with a new menu option to display statistics
# convert input to lowercase
def main_menu():
    while True:
        if username_request != "admin":
            menu = input('''\nSelect one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        else:
            menu = input('''Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

# use if-elif-else statements for the menu options
# add a new user to the user.txt file in this block
# make registering only available to admin 
# request input of a new username
# request input of a new password
# request input of password confirmation
# check if the new password and confirmed password are the same
# create an empty list
# append the username
# append the password
# join the list and cast to str in for loop to remove []
# open user.txt in append mode to add the new user to previous users
# write user to the user.txt file by joining
# close the text file
# if the request is invalid, present a relevant message
# print out a message if a user besides admin selects 'r'
        if menu == 'r' and username_request == "admin":
            reg_user()
            print()

        elif menu == 'r' and username_request != "admin":
            print("Please see admin or select another option.")
            print()

# allow a user to add a new task to task.txt file
# create an empty list
# request the user to input task details:
# a username of the person whom the task is assigned to
# a title of a task
# a description of the task
# the due date of the task (convert month number to shorthand name format with strptime then strftime)
# use try-except block as defense for incorrect date entry for the deadline
# the current date (use today(); tasks format:date= %d; month short= %b; year full= %Y)
# convert current date to str with strftime(format)
# it is assumed the task is incomplete thus include the 'No' for task status
# append the details to the list
# join the list and cast to str in for loop to remove []
# open tasks.txt in append mode to add the task details to tasks.txt
# write task line to the tasks.txt file by joining
# close the text file
        elif menu == 'a':
            add_task()
            print()

# the program will read the tasks from task.txt file for viewing
# open task.txt in read mode
# read the file lines using a for loop
# split the line where there is comma and space
# strip \n with for loop
# print a horizontal line with '_' to divide task sections
# create varibles for the index of each detail in a line
# print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
# print the task details separately for the format
# close the text file
        elif menu == 'va':
            view_all()
            print()

# read the task from task.txt file for a specific user
# open tasks.txt in read mode
# use a for loop to iterate over lines
# split the line where there is comma and space
# strip \n with for loop
# print a horizontal line with '_' to divide task sections
# use if statement to display tasks for the user that logged in
# create varibles for the index of each detail in a line
# print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
# print the task details separately for the format
# close the text file
# call the new function to give the user the option to edit their tasks
        elif menu == 'vm':
            view_mine()
            print()

# use this section to call the function to generate reports
        elif menu == 'gr':
           generate_reports()
           print()
        
# display task statistics in this section
# open tasks.txt in read mode
# create a variable for the number of tasks
# use len() and readlines() as each task is on a new line
# print total number of tasks
# open user.txt' in read mode
# create a variable for the number of users
# use len() and readlines() as each user is on a new line
# print total number of users
# close the text files
#   ● Modify the menu option that allows the admin to display statistics so that
# the reports generated are read from task_overview.txt and user_overview.txt
# display it on the screen in a user-friendly manner
# If these text files don’t exist (because the user hasn’t selected to generate
# them yet), first call the code to generate the text files.
# call the generate_reports() function then readlines() from both text documents
# print the reports
        elif menu == 'ds':
            with open('tasks.txt', 'r') as f5:
                total_tasks = len(f5.readlines())
                print(f"\nThe total number of tasks are:\t {total_tasks}.")
                f5.close()
            with open('user.txt', 'r') as f6:
                total_users = len(f6.readlines())
                print(f"\nThe total number of users are:\t {total_users}.")
                print()
                f6.close()
            generate_reports()
            with open('task_overview.txt', 'r') as g, open('user_overview.txt', 'r') as o:
                print("-" * 100)
                print("-" * 100)
                task_overview = g.read()
                print(task_overview)
                print()
                print("-" * 100)
                print("-" * 100)
                user_overview = o.read()
                print(user_overview)
                g.close()
                o.close()
                print()

# print a statement if the user selects to exit
# use sys.exit() to end program
# close the text file
        elif menu == 'e':
            print("Goodbye!!!")
            sys.exit()
            f.close()

# print a statement if the user did not enter a menu option
# close the user.text file
        else:
            print("You have made a wrong choice. Please try again.\n")
    f.close()
main_menu()

        
        
