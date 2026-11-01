a veryyyy simple to do list GUI built with Tkinter. you can add tasks with a priority label, complete/uncomplete it, and delete it with a confirmation prompt. utilised week 1's stuff to save in a json so the tasks persists. For the 2 extra things, firstly, i have Enter as a keybind to add the task and secondly, like previously mentioned, a priority label to be able to sort by importance. was very rushed because i have less and less time :(

pic of the GUI, with a task and a prompt asking if i wanted to delete it.
<img width="711" height="540" alt="Screenshot 2026-05-13 221108" src="https://github.com/user-attachments/assets/86c56ddb-5bf0-419b-9e94-e55f2db5e9f6" />

how to run:
1. open command prompt
2. run pip install -i https://test.pypi.org/simple/ resolution-week6-bacasss==0.0.3
3. run python -m resolution_week6_bacasss.main
4. profit!

using it:

type your task and the priority it is at then click add task

<img width="618" height="535" alt="image" src="https://github.com/user-attachments/assets/a087d58d-47fb-4144-b89e-efbd18f347c8" />

click on a task when youre done, and then click complete/incomplete to toggle its status

<img width="623" height="535" alt="image" src="https://github.com/user-attachments/assets/3f4fa21c-c41e-4581-8885-1be5e88de0e4" />

click on the task you want to delete and click delete task. it will ask for confirmation.

<img width="1063" height="537" alt="image" src="https://github.com/user-attachments/assets/ec333e38-ab1d-4cf3-b183-3b6645930264" />

clicking yes removes it from the list!

<img width="630" height="537" alt="image" src="https://github.com/user-attachments/assets/2d2254de-86b0-4cb1-a677-e979e0505ee2" />

closing it and reopening will not reset the list as the data is persisted locally

more technical descriptions:

the main window has a title and a set size (500x400). i used 5 widget types: label, entry, button, listbox and scrollbar. everything is laid out with grid(), and there are 3 frames (main_frame, input_frame and listbox_frame) to group the widgets. the add task, complete/incomplete and delete task buttons each use command= to call their own function. messageboxes: a warning if the task is empty, an error if nothing is selected, and a yes/no confirmation before deleting. tasks are saved to tasks.json with load_tasks() and save_task(), same pattern as week 1. columnconfigure/rowconfigure with weight and sticky make the layout stretch when you resize the window. the 2 extras are the priority label and the enter keybind.
