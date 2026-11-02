# TO-DO CLI APPLICATION --> -->
	Building a task management cli app 

### CORE FEATURES
- Add task
- Delete task
- Mark task as completed
- Edit task
- View pending tasks
- View completed tasks
- Assign priority
- Add due dates
- Save tasks
- Load tasks

### LEARNING OBJECTIVES
- JSON
- File persistence
- CRUD operations
- Functions
- Data structures
- Date/time handling
- Input validation
- Modular code organization

## WHAT IS THE PROJECT ABOUT
	The project is about creating a cli app that is used for keeping record of the task u want to do, you ate doing and completed.

## STAGES
- Stage 1 — Data structure
    Start here
    Decide how one task will be represented and how multiple tasks will be stored.
- Stage 2 — Basic task operations
    Add, view, complete, edit, and delete tasks.
- Stage 3 — Better task management
    Priorities, due dates, pending/completed filters, and input validation.
- Stage 4 — Saving and loading
    Use JSON and file handling so tasks remain available after the program closes.
- Stage 5 — Program structure
    Organise functions, separate responsibilities, and test the complete application.

## Stage 1:  Data streucture
	this is how the data us structued in other to avoid conflict in the code
### step1: Data Design
    Before writing any code, let's think about the information a single task needs.

#### For example, a task might have:
- id — a unique identifier
- title — what needs to be done
- description — extra details
- completed — whether the task is finished
- priority — its importance
- due_date — when it should be completed
