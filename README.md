# 100daysofpython
This is a repository for the projects featured in Angela Yu's '100 Days of Code' Python course.

## [Day 1](https://github.com/camjeffrey/100daysofpython/tree/main/day_1)
Day 1 begins quite simple, covering the basics of the **print()** and **input()** functions, simple errors and debugging, string concatenation, and variables.

The project for day 1 is a simple band name generator, which asks the user for two separate inputs: the name of the city they grew up in, and the name of their first pet. These inputs are each assigned to a variable and then concatenated.

Based on some knowledge I already had, I chose to use an fstring for the final output.

## [Day 2](https://github.com/camjeffrey/100daysofpython/tree/main/day_2)
Day 2 covered data types and conversion, mathematical operations, number manipulations, and f strings. This culminates in the second project - a tip calculator which takes a total bill, tip percentage, and number of splits, and outputs what each person should pay. 

I had to do some extra research into string formatting as I didn't know beforehand that Python, by default, doesn't print trailing zeroes. I was originally using the **round()** function, i.e.  

> print(f"Each person pays ${round(split, 2)}.")

so I was confused why I was getting outputs like 'Each person pays $27.9' instead of '$27.90.' Changing to {split:.2f} solved the issue.

Obviously there are no protections against a user entering a non-number when asked for input, which would break the program, but that's a little beyond the scope of what we covered today and I'm sure will be attended to in later days.
