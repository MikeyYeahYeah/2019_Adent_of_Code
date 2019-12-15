# 2019 Advent of Code Challenge
Code for each day lives within branches IE day1_p1

## Setup
**Note:** Requires that you have python-pip installed on your machine

1. Create a virtual environment using `python3 -m venv env`
2. Activate the environment using `. env/bin/activate`
3. Install dependencies using `pip install -r requirements.txt`

## Tests
Run tests using `python -m pytest`

## Lessons Learned

### Day 1 Part 2
I really wanted to use a recursive approach to solve this problem originally.  I knew it was the right use case but I really struggled trying to create the function using recursion.  This was mostly the result of inexperience with recursion.  Interestingly enough, my silly method was able to past the test cases provided in the exercise but when I actually implemented it I was short by ~20.  After banging my head against the keyboard for way too long, I decided to look for the answer and found the answer implemented in Golang using recursion and it was sooooo much more clean.  I think I learned a valuable lesson from this experience.   