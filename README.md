﻿# 100daysofpython
This is a repository for the projects featured in Angela Yu's '100 Days of Code' Python course, and something of a journal with my thoughts on each day.

## [Day 1](https://github.com/camjeffrey/100daysofpython/tree/main/day_01)
Day 1 begins quite simple, covering the basics of the **print()** and **input()** functions, simple errors and debugging, string concatenation, and variables.

The project for day 1 is a simple band name generator, which asks the user for two separate inputs: the name of the city they grew up in, and the name of their first pet. These inputs are each assigned to a variable and then concatenated.

Based on some knowledge I already had, I chose to use an fstring for the final output.

## [Day 2](https://github.com/camjeffrey/100daysofpython/tree/main/day_02)
Day 2 covered data types and conversion, mathematical operations, number manipulations, and f strings. This culminates in the second project - a tip calculator which takes a total bill, tip percentage, and number of splits, and outputs what each person should pay. 

I had to do some extra research into string formatting as I didn't know beforehand that Python, by default, doesn't print trailing zeroes. I was originally using the **round()** function, i.e.  

> print(f"Each person pays ${round(split, 2)}.")

so I was confused why I was getting outputs like 'Each person pays $27.9' instead of '$27.90.' Changing to {split:.2f} solved the issue.

Obviously there are no protections against a user entering a non-number when asked for input, which would break the program, but that's a little beyond the scope of what we covered today and I'm sure will be attended to in later days.

## [Day 3](https://github.com/camjeffrey/100daysofpython/tree/main/day_03)

Day 3 introduced conditionals and logic operators, applying them in a simple choose-your-own-adventure game. Obviously these elements open up a staggering amount of functionality and it's nice to get the feeling things are already ramping up. 

I think this would potentially be a good project to come back to at the end of the course because there are a lot of ideas that I haven't yet learned how to implement, that I think would make the game more interesting, such as some randomizer functionality, finding some elegent way to go back on a decision (maybe using a **while** loop?). There are probably plenty of ideas that I don't even know enough about Python yet to even imagine. It's really exciting to look ahead at everything still left to learn.

Also, I'm unsure of the convention, but I used **sys.exit()** calls in the final block, even though they're unneccessary as the program is about to terminate anyway, simply to keep consistency with every other block. That feels intuitively correct to me.

## [Day 4](https://github.com/camjeffrey/100daysofpython/tree/main/day_04)

Day 4 focused on implementing randomisation and an introduction to lists, and then creating a rock paper scissors game where the computer selects randomly. 

I didn't struggle with this too much. My original win condition code, though functional, was a bit clunky and hard to read, so I cleaned it up a bit. I also didn't really implement lists at all in the project, but they just didn't seem necessary so I didn't want to force it in. I'm still looking forward to learning the techniques to catch invalid user input.


## [Day 5](https://github.com/camjeffrey/100daysofpython/tree/main/day_05)

Day 5 was a fun one, focusing on loops and ending with the creating of a password generator program. It was really good practice in reading documentation and researching how to do things, as I had to utilise the Python docs and Stack Overflow to familiarise myself with the **string** module, and the **join()** and **random.shuffle()** functions. 

## Day 6

There's no source code or directory for day 6, as the practice and projects were done on Reeborg's World, where we focused on defining our own functions and utilising **while** loops to help a robot jump over hurdles of unpredictable heights and spacing, and to solve a maze. Initially, I was a little disappointed, as defining a **turn_right()** function with **three turn_left()** calls seemed like a pretty unsatisfying way to learn about functions. But when we got into solving the hurdles of random heights and spacing, and solving mazes, I appreciated the content of the day more as it became all about thinking algorithmically, and obviously that kind of thinking will apply to all the functions I ever define and call. It's nice to have another couple of crucial programming concepts in play now for future projects.

## [Day 7](https://github.com/camjeffrey/100daysofpython/tree/main/day_07)

Day 7 was the first big challenge, in my opinion, but it was also a lot of fun and I'm proud of my hangman project.

This was a really great way to combine everything I've learnt so far, and an excellent challenge of breaking down a larger problem into smaller ones. There are a lot of things that have to happen each time a user makes a guess, and a lot of conditions to consider, and it was challenging and fun to work through each possibility systematically and implement it into my code. I had to do some debugging as well; for instance, I originally didn't check if **guess** was in **secret_word**, and therefore I was giving the user a mistake for every single element in **secret_word** which != **guess**.

I also have finally implemented a check for valid user input and I'm thrilled that it seems to work so well. I think I've got a really good grasp on loops and was able to implement solutions which check not only if the input was a single letter in the first place, but whether it had already been guessed, and return to the input prompt correctly.

Overall, I'm very proud of this project and had tons of fun thinking through it. I also completed the project before watching any of the course material for the day, as I could see that we weren't learning anything new but rather applying things we've already learnt to a more complex project, so I wanted to see if I could do it without hints or prompting from Angela. So I'm very excited to watch through the videos now and see how she has implemented everything and see another approach.

## [Day 8](https://github.com/camjeffrey/100daysofpython/tree/main/day_08)

Day 8 expanded on functions, focusing on functions with inputs and leading up to a Caesar Cipher encryption/decryption program. I was already familiar and confident with defining functions that took inputs, as I had used them in the previous day's project, but I still enjoyed practicing more. Today, the biggest lesson was about refactoring, as I did a major rewrite after completing a first working iteration. Initially, I had two separate functions for encryption and decryption which were effectively identical, except the decryption subtracted the shift instead of adding it. The amount of code I was writing out twice, identically, was a good indication it could be cleaned up, so I ended up refactoring it into a single function with an **encrpt** flag. If that flag was false, then **shift = -shift**, which was a pretty elegant solution.

I'm also pretty proud of my forward planning in this project, for instance using two separate lists for uppercase and lowercase characters so that the user's case would be maintained, instead of just converting everything to lowercase, and how I handled different inputs such as punctuation and digits.

## [Day 9](https://github.com/camjeffrey/100daysofpython/tree/main/day_09)

Day 9 was an introduction to dictionaries, and expanded a little bit on nested dictionaries and lists (though this didn't end up playing into the project). I found the project, a silent auction program which tracks bidders and bids and awards a winner, fairly simple, even if starting out I do find the syntax concerning dictionaries a little strange. This project felt like a bit of a stp back in complexity but looking ahead, I can see a Blackjack capstone project on day 11 so I'm excited to tackle that.

## [Day 10](https://github.com/camjeffrey/100daysofpython/tree/main/day_10)

Day 10 was an introduction to functions with outputs, which I already had a bit of familiarity with. The project was a calculator, which would give the user the option of doing an entirely new calculation, or having the result of the previous calculation be the first number. I'm not gonna lie, I threw this together late at night. It works, but I'm sure there were much cleaner, clearer, more elegant ways to do it all. I was a little puzzled about handling the old result and the new result, making sure it was intgrated correctly with the **while** loop, etc., but writing out step-by-step what had to happen at each step in the code helped me figure it out.

Also, not that anybody would, but **eval()** is used here with absolutely no protections so don't ever deploy this anywhere.

## [Day 11](https://github.com/camjeffrey/100daysofpython/tree/main/day_11)

Day 11 was a culmination of almost everything covered so far, and it was a good challenge. In a similar way to the hangman project on day 7, it really challenged my ability to think algorithmically and work through everything that has to happen at each stage of the procss.

Handling the aces was something I struggled with quite a bit at first, and I had a very clunky first implementation of a score calculator. I originally had two separate functions for counting a hand, one with aces and one without. Those two functions were then called conditionally by a third function depending on whether or not there was an ace in the hand. I also had two separate counters for aces as ones, and aces as elevens, and so I had a list of possible counts and had to determine if a hand was bust by determining if any count in the list was still under 21. I hadn't even finished fully implementing that before I realised how difficult and convoluted it would be, so I had to think of another solution.

In the end, the solution was pretty simple once I stopped and thought about the game critically. In blackjack, you always want the highest score you can get without busting, so you would only count an ace as a one if you couldn't count it as an eleven. Also, even if you had two aces, you couldn't count them both as eleven as that would instantly bust. Therefore, if the player has an ace initially counted as a one, but adding 10 to their current score would not be a bust, then the ace is counted as an eleven (by simpling setting count equal to count + 10).

It's not a perfect implementation, as I can't figure out at the minute how to allow the player to play another hand after them or the dealer having blackjack at the beginning of the hand, but all in all the program works well and was a great challenge. I plan to come back to this every now and then to try and extend on it, for instance trying to solve the problem of blackjack instantly terminating the program without the chance to play anothere hand and handling split pairs etc., which will obviously add complexity, but for now I'm very happy with what I've accomplished here and how it's helped me to understand all the previous lessons more clearly.

***Update***

I had another look at my blackjack program and decided to move as much of the core game loop into functions as I possibly could, which I think made the code much cleaner and more professional. It also, I think, enhanced the readability quite a bit and should help a lot if I do decide to implement things like split pairs in the future.

I also put all of the blackjack combination checks into a function which returned a boolean value, but had to ask Claude.ai for some guidance on how to follow on from that to make the game replayable if it returned **True**. It gave me the idea of encapsulating the rest of the game loop in an **if not** statement, which was a neat idea and something I'll remember in the future! I think it would also be useful if I did implement split pairs, as I could probably do something similar to catch another abnormal game state while maintaining replayability. Something like a **player_has_pair** check which returns a boolean, and turning the **if not blackjack** statement into **if not blackjack and if not split pairs**. I'll have another look at it at some later date.


## [Day 12](https://github.com/camjeffrey/100daysofpython/tree/main/day_12)

Day 12 was substantially easier than day 11, focusing on global and local scopes and ending with a higher / lower number guessing game. There's not much to say about this one, though the content on scope did prompt me to ensure that my assignment of the answer to a random integer occured *within* my while loop, so that it was reassigned every time the while loop ran. Other than that, putting the program together only took me maybe 10 or 15 minutes and didn't present any significant challenges.

## Day 13

No code or directory for this one, as today focused on the debugging process.
