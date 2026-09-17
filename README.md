# ✈️ Multi-Destination Trip Budget Planner

## What is it?
A command-line program that helps you figure out whether a multi-stop trip is affordable. You enter your total budget, then add as many destinations as you like, each with its own transportation, accommodation, food, and entertainment costs, and the program totals everything up and tells you whether you're under, over, or exactly on budget.

## Technologies Involved
- **Python**: the entire program is written in plain Python, using built-in input/output and file handling (no external libraries needed)

## Features
- Add an unlimited number of destinations in one session
- Tracks four expense categories per destination: transportation, accommodation, food, and entertainment
- Calculates a running total across all destinations
- Compares the total against your budget and gives a clear verdict:
  - **Over budget**: tells you by how much
  - **Exactly on budget**
  - **Under budget**, with an encouraging "GO RIGHT AWAY FOR THAT TRIP!!!"
- Prints a per-destination cost breakdown to the console
- Saves a full trip summary to a text file (`Trip_summary_expenses.txt`) so you have a record afterward

## Process
The program is built around three functions, each with one job:
1. **`budget_calculator()`**: the main loop. Asks for your budget, then repeatedly asks for a destination's name and costs, storing each one in a dictionary and adding it to a list until you say you're done.
2. **`calculate_total()`**: takes the full list of destinations and adds up every expense across all of them into a single grand total.
3. **`trip_summary()`**: writes everything (per-destination costs, the total, the budget, and the final verdict) out to a text file, so the results aren't just printed and lost when the program closes.

## What I Learned
- Collecting and structuring user input into dictionaries and lists
- Using loops to let a program accept an open-ended amount of input (`while True` with a break condition)
- Writing formatted output to both the console and a file
- Breaking a program into small functions that each handle one responsibility

## How It Can Be Improved
- Validate user input (currently, entering non-numeric text for a cost would crash the program)
- Let the user edit or remove a destination after adding it, instead of only appending
- Add the ability to save/load a budget plan between sessions instead of always starting fresh
- Break costs down by category in the final summary, not just per-destination totals
- Build a simple graphical or web interface instead of the console-only version

## Running the Project
1. Install **Python**: [python.org/downloads](https://www.python.org/downloads/)
2. Save the script (e.g. `budget_planner.py`).
3. Run it from a terminal:
   ```
   python budget_planner.py
   ```
4. Follow the prompts: enter your budget, then add destinations one at a time.

## Demo Video

<img src="https://raw.githubusercontent.com/matafn09/Multi-destination-trip-budget-planner/main/Budget-trip-planner-video.gif" width="600" alt="Trip budget planner">
