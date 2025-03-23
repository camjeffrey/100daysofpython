# 100daysofpython
This is a repository for the projects featured in Angela Yu's '100 Days of Code' Python course, and something of a journal with my thoughts on each day.

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

## [Day 3](https://github.com/camjeffrey/100daysofpython/tree/main/day_3)

Day 3 introduced conditionals and logic operators, applying them in a simple choose-your-own-adventure game. Obviously these elements open up a staggering amount of functionality and it's nice to get the feeling things are already ramping up. 

I think this would potentially be a good project to come back to at the end of the course because there are a lot of ideas that I haven't yet learned how to implement, that I think would make the game more interesting, such as some randomizer functionality, finding some elegent way to go back on a decision (maybe using a **while** loop?). There are probably plenty of ideas that I don't even know enough about Python yet to even imagine. It's really exciting to look ahead at everything still left to learn.

Also, I'm unsure of the convention, but I used **sys.exit()** calls in the final block, even though they're unneccessary as the program is about to terminate anyway, simply to keep consistency with every other block. That feels intuitively correct to me.

## [Day 4](https://github.com/camjeffrey/100daysofpython/tree/main/day_4)

Day 4 focused on implementing randomisation and an introduction to lists, and then creating a rock paper scissors game where the computer selects randomly. 

I didn't struggle with this too much. My original win condition code, though functional, was a bit clunky and hard to read, so I cleaned it up a bit. I also didn't really implement lists at all in the project, but they just didn't seem necessary so I didn't want to force it in. I'm still looking forward to learning the techniques to catch invalid user input.


## [Day 5](https://github.com/camjeffrey/100daysofpython/tree/main/day_5)

Day 5 was a fun one, focusing on loops and ending with the creating of a password generator program. It was really good practice in reading documentation and researching how to do things, as I had to utilise the Python docs and Stack Overflow to familiarise myself with the **string** module, and the **join()** and **random.shuffle()** functions. 
