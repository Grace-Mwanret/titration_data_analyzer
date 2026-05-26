# About
This Python program examines pH readings from a chemical titration experiment to identify important changes in acidity and alkalinity.
Titration is a laboratory technique used to determine the concentration of a solution by measuring when it reaches a neutral pH of 7.
# How to run it
It is a simple python project so it can be run on any code editor just make sure a working python version is installed on it.

# What it does
This Python program analyzes pH readings collected during a chemical titration experiment.
The program:
1. Finds the minimum pH value
2. Finds the maximum pH value
3. Detects the first point where the solution becomes neutral or alkaline (pH >= 7)
4. Reports the index where the neutral point was crossed
5. Handles cases where the pH never reaches 7

# What I learned
I learned how to:
1. Use Python functions
2. use min() and max() function
3. Use loops and conditionals
4. Display organized experiment results with enumerate()
5. Unpacking

# Technologies used
Pycharm and Python

# Example input
readings = [2.1, 3.4, 5.6, 7.2, 9.1, 11.3]
# Example output
Minimum pH: 2.1
Maximum pH: 11.3
Neutral point crossed at index: 3
