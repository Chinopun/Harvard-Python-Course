#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║  CS50P Interactive Quiz                                  ║
║  Harvard's Introduction to Programming with Python       ║
║  10 Weeks · 35 Coding Tasks · Terminal Grader            ║
╚══════════════════════════════════════════════════════════╝

HOW IT WORKS:
  1. Pick a week or continue where you left off
  2. Read the task description
  3. Edit 'answer.py' in your editor
  4. Press Enter — the quiz runs your code with test cases
  5. Get instant feedback + hints if you're stuck
  6. Progress is saved to cs50p_progress.json
"""

import subprocess
import sys
import os
import json

# ──────────────────────────────────────────────────────────
# ANSI COLORS
# ──────────────────────────────────────────────────────────
R    = "\033[91m"
G    = "\033[92m"
Y    = "\033[93m"
B    = "\033[94m"
M    = "\033[95m"
C    = "\033[96m"
BOLD = "\033[1m"
DIM  = "\033[2m"
RST  = "\033[0m"

def red(s):     return f"{R}{s}{RST}"
def green(s):   return f"{G}{s}{RST}"
def yellow(s):  return f"{Y}{s}{RST}"
def blue(s):    return f"{B}{s}{RST}"
def magenta(s): return f"{M}{s}{RST}"
def cyan(s):    return f"{C}{s}{RST}"
def bold(s):    return f"{BOLD}{s}{RST}"
def dim(s):     return f"{DIM}{s}{RST}"

# ──────────────────────────────────────────────────────────
# QUIZ DATA  (10 weeks, 35 tasks)
# ──────────────────────────────────────────────────────────
WEEKS = [

    # ══════════════════════════════════════════════════════
    # WEEK 0 · FUNCTIONS & VARIABLES
    # ══════════════════════════════════════════════════════
    {
        "number": 0,
        "title": "Functions & Variables",
        "intro": (
            "Python's building blocks: print(), input(), variables, "
            "type conversion, f-strings, and defining your own functions."
        ),
        "tasks": [
            {
                "id": "w0t1",
                "title": "Hello, Name!",
                "concept": "print() and input()",
                "description": """\
Ask the user for their name, then print a personalised greeting.

  Input:  David
  Output: hello, David

Requirements
  • Use input() to capture the name
  • Print exactly:  hello, <name>   (lowercase 'hello', comma, space)""",
                "starter": (
                    "# Week 0, Task 1 — Hello, Name!\n"
                    "# Ask for the user's name and greet them.\n\n"
                    "name = input(\"What's your name? \")\n"
                    "print(...)  # replace ... with the greeting\n"
                ),
                "tests": [
                    {"input": "David\n",  "expected": "hello, David"},
                    {"input": "world\n",  "expected": "hello, world"},
                    {"input": "Alice\n",  "expected": "hello, Alice"},
                ],
                "hints": [
                    'Use an f-string: print(f"hello, {name}")',
                    'Or concatenation: print("hello, " + name)',
                    "Output must be exactly:  hello, <name>  — lowercase h, comma, space.",
                ],
            },
            {
                "id": "w0t2",
                "title": "Sum Two Numbers",
                "concept": "int(), type conversion",
                "description": """\
Ask the user for two numbers and print their integer sum.

  Input:  1  then  2
  Output: 3

Requirements
  • Use input() twice
  • Convert each to int with int()
  • Print the sum (no decimal point)""",
                "starter": (
                    "# Week 0, Task 2 — Sum Two Numbers\n\n"
                    "x = input(\"x: \")\n"
                    "y = input(\"y: \")\n\n"
                    "# Convert to int and print the sum\n"
                ),
                "tests": [
                    {"input": "1\n2\n",   "expected": "3"},
                    {"input": "10\n20\n", "expected": "30"},
                    {"input": "0\n0\n",   "expected": "0"},
                ],
                "hints": [
                    "Convert as you read: x = int(input('x: '))",
                    "Then: print(x + y)",
                    "Without int(), '1' + '2' == '12' (string concat) — not what we want!",
                ],
            },
            {
                "id": "w0t3",
                "title": "Title Case Greeting",
                "concept": "f-strings, str.capitalize()",
                "description": """\
Ask for a first and last name (may be lowercase), then print a title-cased greeting.

  Input:  harry   then   potter
  Output: Hello, Harry Potter

Requirements
  • Capitalise each name properly
  • Output format:  Hello, <First> <Last>""",
                "starter": (
                    "# Week 0, Task 3 — Title Case Greeting\n\n"
                    "first = input(\"First name: \")\n"
                    "last  = input(\"Last name: \")\n\n"
                    "# Print: Hello, <First> <Last>  (title case)\n"
                ),
                "tests": [
                    {"input": "harry\npotter\n",    "expected": "Hello, Harry Potter"},
                    {"input": "hermione\ngranger\n","expected": "Hello, Hermione Granger"},
                    {"input": "Alice\nSmith\n",     "expected": "Hello, Alice Smith"},
                ],
                "hints": [
                    "'harry'.capitalize() → 'Harry'",
                    'f-string: print(f"Hello, {first.capitalize()} {last.capitalize()}")',
                    "Or .title() on each name — same result for single words.",
                ],
            },
            {
                "id": "w0t4",
                "title": "Define square()",
                "concept": "def, return",
                "description": """\
Write a function square(n) that returns n squared, then use it.

  Input:  3
  Output: 9

Requirements
  • def square(n): ... return the result (don't print inside the function)
  • Read an integer from the user, print square(x)""",
                "starter": (
                    "# Week 0, Task 4 — Define a Function\n\n"
                    "def square(n):\n"
                    "    ...  # return n squared\n\n\n"
                    "x = int(input(\"Enter a number: \"))\n"
                    "print(square(x))\n"
                ),
                "tests": [
                    {"input": "3\n",  "expected": "9"},
                    {"input": "5\n",  "expected": "25"},
                    {"input": "0\n",  "expected": "0"},
                    {"input": "10\n", "expected": "100"},
                ],
                "hints": [
                    "Replace ... with:  return n * n",
                    "Or:  return n ** 2",
                    "Use return, not print, inside the function.",
                ],
            },
            {
                "id": "w0t5",
                "title": "String Methods",
                "concept": "str.strip(), str.upper()",
                "description": """\
Ask the user for a word (may have surrounding spaces), strip whitespace, print it in UPPERCASE.

  Input:  '  hello  '
  Output: HELLO""",
                "starter": (
                    "# Week 0, Task 5 — String Methods\n\n"
                    "word = input(\"Word: \")\n"
                    "# strip whitespace, convert to uppercase, then print\n"
                ),
                "tests": [
                    {"input": "  hello  \n", "expected": "HELLO"},
                    {"input": "python\n",    "expected": "PYTHON"},
                    {"input": "  CS50  \n",  "expected": "CS50"},
                ],
                "hints": [
                    "Chain methods: word.strip().upper()",
                    "Or step by step: word = word.strip(); print(word.upper())",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 1 · CONDITIONALS
    # ══════════════════════════════════════════════════════
    {
        "number": 1,
        "title": "Conditionals",
        "intro": (
            "Make decisions with if / elif / else, "
            "boolean operators (and, or), the modulo operator, and match."
        ),
        "tasks": [
            {
                "id": "w1t1",
                "title": "Compare Two Numbers",
                "concept": "if / elif / else",
                "description": """\
Ask for two integers x and y. Print their relationship.

  x=3, y=5  →  x is less than y
  x=5, y=3  →  x is greater than y
  x=4, y=4  →  x is equal to y""",
                "starter": (
                    "# Week 1, Task 1 — Compare Two Numbers\n\n"
                    "x = int(input(\"x: \"))\n"
                    "y = int(input(\"y: \"))\n\n"
                    "# if / elif / else to print the relationship\n"
                ),
                "tests": [
                    {"input": "3\n5\n", "expected": "x is less than y"},
                    {"input": "5\n3\n", "expected": "x is greater than y"},
                    {"input": "4\n4\n", "expected": "x is equal to y"},
                ],
                "hints": [
                    "if x < y: print('x is less than y')",
                    "elif x > y: print('x is greater than y')",
                    "else: print('x is equal to y')",
                ],
            },
            {
                "id": "w1t2",
                "title": "Grade Calculator",
                "concept": "chained comparisons, elif",
                "description": """\
Ask for a score (0–100) and print the letter grade.

  90–100 → A    80–89 → B    70–79 → C    60–69 → D    0–59 → F

  Input:  95  →  A
  Input:  72  →  C""",
                "starter": (
                    "# Week 1, Task 2 — Grade Calculator\n\n"
                    "score = int(input(\"Score: \"))\n\n"
                    "# Determine the letter grade\n"
                ),
                "tests": [
                    {"input": "95\n", "expected": "A"},
                    {"input": "85\n", "expected": "B"},
                    {"input": "75\n", "expected": "C"},
                    {"input": "65\n", "expected": "D"},
                    {"input": "55\n", "expected": "F"},
                ],
                "hints": [
                    "Start with the highest: if score >= 90: print('A')",
                    "Use elif for each subsequent band",
                    "Python allows chaining: if 80 <= score < 90:",
                ],
            },
            {
                "id": "w1t3",
                "title": "Odd or Even",
                "concept": "modulo operator %",
                "description": """\
Ask for an integer. Print "Even" or "Odd".

  Input: 4  →  Even
  Input: 7  →  Odd
  Input: 0  →  Even""",
                "starter": (
                    "# Week 1, Task 3 — Odd or Even\n"
                    "# Hint: the % operator gives the remainder\n\n"
                    "n = int(input(\"Number: \"))\n"
                    "# print Even or Odd\n"
                ),
                "tests": [
                    {"input": "4\n",  "expected": "Even"},
                    {"input": "7\n",  "expected": "Odd"},
                    {"input": "0\n",  "expected": "Even"},
                    {"input": "13\n", "expected": "Odd"},
                ],
                "hints": [
                    "n % 2 is 0 for even numbers, 1 for odd",
                    "if n % 2 == 0: print('Even')",
                    "else: print('Odd')",
                ],
            },
            {
                "id": "w1t4",
                "title": "Hogwarts Sorting Hat",
                "concept": "match statement",
                "description": """\
Use a match statement to sort students into houses.

  Harry | Hermione | Ron  →  Gryffindor
  Draco                   →  Slytherin
  Luna                    →  Ravenclaw
  Cedric                  →  Hufflepuff
  anything else           →  Who?

  Input: Harry  →  Gryffindor
  Input: Voldemort  →  Who?""",
                "starter": (
                    "# Week 1, Task 4 — Sorting Hat (match)\n\n"
                    "name = input(\"Name: \")\n\n"
                    "match name:\n"
                    "    case ...:\n"
                    "        ...\n"
                ),
                "tests": [
                    {"input": "Harry\n",     "expected": "Gryffindor"},
                    {"input": "Hermione\n",  "expected": "Gryffindor"},
                    {"input": "Ron\n",       "expected": "Gryffindor"},
                    {"input": "Draco\n",     "expected": "Slytherin"},
                    {"input": "Luna\n",      "expected": "Ravenclaw"},
                    {"input": "Cedric\n",    "expected": "Hufflepuff"},
                    {"input": "Voldemort\n", "expected": "Who?"},
                ],
                "hints": [
                    'case "Harry" | "Hermione" | "Ron": print("Gryffindor")',
                    'case _: print("Who?")  — the default (wildcard) case',
                    "The | symbol in match means 'or' between values.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 2 · LOOPS
    # ══════════════════════════════════════════════════════
    {
        "number": 2,
        "title": "Loops",
        "intro": "Repeat code with while and for loops, range(), lists, and break/continue.",
        "tasks": [
            {
                "id": "w2t1",
                "title": "Countdown",
                "concept": "while loop",
                "description": """\
Ask for a positive integer n. Count down from n to 1, then print "Blastoff!".

  n=3  →
    3
    2
    1
    Blastoff!""",
                "starter": (
                    "# Week 2, Task 1 — Countdown\n\n"
                    "n = int(input(\"n: \"))\n\n"
                    "# count down, then Blastoff!\n"
                ),
                "tests": [
                    {"input": "3\n", "expected": "3\n2\n1\nBlastoff!"},
                    {"input": "5\n", "expected": "5\n4\n3\n2\n1\nBlastoff!"},
                    {"input": "1\n", "expected": "1\nBlastoff!"},
                ],
                "hints": [
                    "while n > 0: print(n); n -= 1",
                    "After the loop: print('Blastoff!')",
                    "Or use a for loop: for i in range(n, 0, -1):",
                ],
            },
            {
                "id": "w2t2",
                "title": "Sum 1 to n",
                "concept": "for loop, range()",
                "description": """\
Ask for a positive integer n. Print the sum of 1 through n using a for loop.

  n=5  →  15   (1+2+3+4+5)
  n=10 →  55""",
                "starter": (
                    "# Week 2, Task 2 — Sum 1 to n\n\n"
                    "n = int(input(\"n: \"))\n"
                    "total = 0\n\n"
                    "# use for i in range(...) to accumulate the sum\n\n"
                    "print(total)\n"
                ),
                "tests": [
                    {"input": "5\n",   "expected": "15"},
                    {"input": "10\n",  "expected": "55"},
                    {"input": "1\n",   "expected": "1"},
                    {"input": "100\n", "expected": "5050"},
                ],
                "hints": [
                    "range(1, n+1) produces 1, 2, 3, …, n",
                    "for i in range(1, n+1): total += i",
                    "Bonus: print(sum(range(1, n+1))) does it in one line!",
                ],
            },
            {
                "id": "w2t3",
                "title": "FizzBuzz",
                "concept": "for loop, modulo, conditionals",
                "description": """\
Classic FizzBuzz! Ask for n, then print numbers 1 to n with substitutions:

  divisible by 3 AND 5  →  FizzBuzz
  divisible by 3 only   →  Fizz
  divisible by 5 only   →  Buzz
  otherwise             →  the number

  n=6  →
    1
    2
    Fizz
    4
    Buzz
    Fizz""",
                "starter": (
                    "# Week 2, Task 3 — FizzBuzz\n\n"
                    "n = int(input(\"n: \"))\n\n"
                    "for i in range(1, n + 1):\n"
                    "    # your conditions here\n"
                    "    pass\n"
                ),
                "tests": [
                    {"input": "15\n", "expected": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"},
                    {"input": "5\n",  "expected": "1\n2\nFizz\n4\nBuzz"},
                    {"input": "3\n",  "expected": "1\n2\nFizz"},
                ],
                "hints": [
                    "Check FizzBuzz FIRST (divisible by both), then Fizz, then Buzz.",
                    "if i % 15 == 0: print('FizzBuzz')  — or check i%3==0 and i%5==0",
                    "Remove the 'pass' line once you add real code.",
                ],
            },
            {
                "id": "w2t4",
                "title": "Validate Input Loop",
                "concept": "while True / break",
                "description": """\
Keep asking the user for a positive integer until they provide one (> 0).
Once valid, print it.

  Input: -5  (invalid — ask again)
  Input:  0  (invalid — ask again)
  Input:  3  →  3""",
                "starter": (
                    "# Week 2, Task 4 — Input Validation Loop\n\n"
                    "while True:\n"
                    "    n = int(input(\"n: \"))\n"
                    "    # break when n is valid (> 0)\n"
                    "    ...\n\n"
                    "print(n)\n"
                ),
                "tests": [
                    {"input": "-1\n0\n5\n", "expected": "5"},
                    {"input": "3\n",        "expected": "3"},
                    {"input": "-10\n-5\n0\n1\n", "expected": "1"},
                ],
                "hints": [
                    "if n > 0: break",
                    "The while True loop keeps going until you break out of it.",
                    "Remove the '...' and replace with your if statement.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 3 · EXCEPTIONS
    # ══════════════════════════════════════════════════════
    {
        "number": 3,
        "title": "Exceptions",
        "intro": "Handle errors gracefully with try / except blocks.",
        "tasks": [
            {
                "id": "w3t1",
                "title": "Safe Integer Input",
                "concept": "try / except ValueError",
                "description": """\
Ask for an integer. If the input isn't a valid integer, print "Not a valid integer."
and ask again. Repeat until valid, then print it.

  Input: cat    →  Not a valid integer.
  Input: 3.14   →  Not a valid integer.
  Input: 42     →  42""",
                "starter": (
                    "# Week 3, Task 1 — Safe Integer Input\n\n"
                    "while True:\n"
                    "    try:\n"
                    "        n = int(input(\"Integer: \"))\n"
                    "        break\n"
                    "    except ValueError:\n"
                    "        print(...)  # fill in the error message\n\n"
                    "print(n)\n"
                ),
                "tests": [
                    {"input": "cat\n42\n",  "expected": "Not a valid integer.\n42"},
                    {"input": "3.14\n7\n",  "expected": "Not a valid integer.\n7"},
                    {"input": "5\n",        "expected": "5"},
                ],
                "hints": [
                    'Replace ... with: "Not a valid integer."',
                    "The try block attempts int(input(...)). If it fails, except runs.",
                    "break exits the loop once a valid integer is entered.",
                ],
            },
            {
                "id": "w3t2",
                "title": "Safe Division",
                "concept": "try / except ZeroDivisionError",
                "description": """\
Ask for two integers x and y.
Print x / y as a float. If y == 0, print "Error: division by zero."

  x=10, y=2  →  5.0
  x=10, y=0  →  Error: division by zero.
  x=7,  y=2  →  3.5""",
                "starter": (
                    "# Week 3, Task 2 — Safe Division\n\n"
                    "x = int(input(\"x: \"))\n"
                    "y = int(input(\"y: \"))\n\n"
                    "try:\n"
                    "    ...\n"
                    "except ZeroDivisionError:\n"
                    "    print(\"Error: division by zero.\")\n"
                ),
                "tests": [
                    {"input": "10\n2\n", "expected": "5.0"},
                    {"input": "10\n0\n", "expected": "Error: division by zero."},
                    {"input": "7\n2\n",  "expected": "3.5"},
                ],
                "hints": [
                    "Replace ... with: print(x / y)",
                    "x / y in Python always returns a float (e.g. 5.0, 3.5)",
                    "ZeroDivisionError is raised automatically — your except catches it.",
                ],
            },
            {
                "id": "w3t3",
                "title": "Robust Positive Integer",
                "concept": "try / except in while loop",
                "description": """\
Keep asking until the user enters a positive integer.
Handle both non-numeric input (ValueError) and non-positive numbers silently.

  Input: "cat"  →  (ask again)
  Input: -3     →  (ask again)
  Input: 5      →  5""",
                "starter": (
                    "# Week 3, Task 3 — Robust Positive Integer\n\n"
                    "while True:\n"
                    "    try:\n"
                    "        n = int(input(\"Positive integer: \"))\n"
                    "        if n > 0:\n"
                    "            break\n"
                    "    except ValueError:\n"
                    "        pass\n\n"
                    "print(n)\n"
                ),
                "tests": [
                    {"input": "cat\n-3\n5\n",    "expected": "5"},
                    {"input": "-1\n0\n7\n",       "expected": "7"},
                    {"input": "10\n",             "expected": "10"},
                ],
                "hints": [
                    "This starter is already correct — try running it!",
                    "'pass' means 'do nothing'; the loop will restart on ValueError.",
                    "If n <= 0, neither break nor pass triggers, so the loop restarts.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 4 · LIBRARIES
    # ══════════════════════════════════════════════════════
    {
        "number": 4,
        "title": "Libraries",
        "intro": "Use Python's standard library (random, sys) and third-party packages.",
        "tasks": [
            {
                "id": "w4t1",
                "title": "Random Number",
                "concept": "import random, random.randint()",
                "description": """\
Ask for a positive integer n.
Print a random integer between 1 and n (inclusive).

  Input: 10  →  some number between 1 and 10

Requirements
  • import random
  • Use random.randint(1, n)
  • The grader checks that your output is in range, not the exact value.""",
                "starter": (
                    "# Week 4, Task 1 — Random Number\n"
                    "import random\n\n"
                    "n = int(input(\"n: \"))\n"
                    "result = random.randint(1, n)\n"
                    "print(result)\n"
                ),
                "tests": [
                    {"input": "10\n", "expected": None,
                     "validator": "range_1_to_n", "n_value": 10},
                    {"input": "1\n",  "expected": "1"},
                ],
                "hints": [
                    "import random goes at the top of the file.",
                    "random.randint(a, b) returns a random integer N where a <= N <= b.",
                    "The starter code is already correct — just run it!",
                ],
            },
            {
                "id": "w4t2",
                "title": "Coin Flip Simulation",
                "concept": "random.choice(), counters",
                "description": """\
Ask for n (number of flips). Simulate n coin flips and print the totals.

  Input: 10  →
    Heads: 6
    Tails: 4

  (Exact counts will vary — grader checks Heads + Tails == n)""",
                "starter": (
                    "# Week 4, Task 2 — Coin Flip Simulation\n"
                    "import random\n\n"
                    "n = int(input(\"Flips: \"))\n"
                    "heads = 0\n"
                    "tails = 0\n\n"
                    "for _ in range(n):\n"
                    "    flip = random.choice([\"Heads\", \"Tails\"])\n"
                    "    ...  # increment heads or tails\n\n"
                    "print(f\"Heads: {heads}\")\n"
                    "print(f\"Tails: {tails}\")\n"
                ),
                "tests": [
                    {"input": "10\n",  "expected": None,
                     "validator": "heads_tails_sum", "n_value": 10},
                    {"input": "100\n", "expected": None,
                     "validator": "heads_tails_sum", "n_value": 100},
                ],
                "hints": [
                    "if flip == 'Heads': heads += 1  else: tails += 1",
                    "Replace the ... with that if/else block.",
                    "Heads + Tails should equal n.",
                ],
            },
            {
                "id": "w4t3",
                "title": "Command-Line Args",
                "concept": "import sys, sys.argv",
                "description": """\
Write a program that reads its name argument from the command line.

  python answer.py          →  Hello, world
  python answer.py David    →  Hello, David
  python answer.py Alice    →  Hello, Alice

Requirements
  • import sys
  • Check len(sys.argv)
  • sys.argv[0] is the script name; sys.argv[1] is the first argument""",
                "starter": (
                    "# Week 4, Task 3 — sys.argv\n"
                    "import sys\n\n"
                    "if len(sys.argv) == 2:\n"
                    "    print(f\"Hello, {sys.argv[1]}\")\n"
                    "else:\n"
                    "    print(\"Hello, world\")\n"
                ),
                "tests": [
                    {"input": "", "expected": "Hello, world",  "argv": []},
                    {"input": "", "expected": "Hello, David",  "argv": ["David"]},
                    {"input": "", "expected": "Hello, Alice",  "argv": ["Alice"]},
                ],
                "hints": [
                    "sys.argv is a list: [script_name, arg1, arg2, ...]",
                    "len(sys.argv) == 1 means no arguments were given.",
                    "The starter is already correct — read it carefully!",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 5 · UNIT TESTS
    # ══════════════════════════════════════════════════════
    {
        "number": 5,
        "title": "Unit Tests",
        "intro": "Write test functions using assert to verify your code is correct.",
        "tasks": [
            {
                "id": "w5t1",
                "title": "Test square()",
                "concept": "assert, test functions",
                "description": """\
Implement square(n) AND write tests for it.

Your file must contain:
  • def square(n):  — returns n * n
  • def test_positive():  — asserts square(2)==4 and square(3)==9
  • def test_negative():  — asserts square(-2)==4
  • def test_zero():      — asserts square(0)==0
  • Call all three test functions at the bottom
  • If all pass, print "All tests passed!"

Expected output:  All tests passed!""",
                "starter": (
                    "# Week 5, Task 1 — Test square()\n\n"
                    "def square(n):\n"
                    "    return n * n\n\n\n"
                    "def test_positive():\n"
                    "    assert square(2) == 4\n"
                    "    assert square(3) == 9\n\n\n"
                    "def test_negative():\n"
                    "    assert square(-2) == 4\n"
                    "    assert square(-3) == 9\n\n\n"
                    "def test_zero():\n"
                    "    assert square(0) == 0\n\n\n"
                    "# Run all tests\n"
                    "test_positive()\n"
                    "test_negative()\n"
                    "test_zero()\n"
                    "print(\"All tests passed!\")\n"
                ),
                "tests": [
                    {"input": "\n", "expected": "All tests passed!"},
                ],
                "hints": [
                    "The starter is already complete — run it to confirm, then try editing square() to break it and see what happens.",
                    "assert condition raises AssertionError if condition is False.",
                    "(-2) * (-2) == 4, so square(-2) should return 4.",
                ],
            },
            {
                "id": "w5t2",
                "title": "Raise & Catch ValueError",
                "concept": "raise ValueError, try/except in tests",
                "description": """\
Write only_positive(n):
  • Returns n if n > 0
  • Raises ValueError("n must be positive") if n <= 0

Then in your main code:
  • Call only_positive(5)  → print the result
  • Call only_positive(-1) → catch ValueError, print "Invalid"

Expected output:
  5
  Invalid""",
                "starter": (
                    "# Week 5, Task 2 — Raise & Catch ValueError\n\n"
                    "def only_positive(n):\n"
                    "    if n > 0:\n"
                    "        return n\n"
                    "    raise ValueError(\"n must be positive\")\n\n\n"
                    "try:\n"
                    "    print(only_positive(5))\n"
                    "except ValueError:\n"
                    "    print(\"Invalid\")\n\n"
                    "try:\n"
                    "    print(only_positive(-1))\n"
                    "except ValueError:\n"
                    "    print(\"Invalid\")\n"
                ),
                "tests": [
                    {"input": "\n", "expected": "5\nInvalid"},
                ],
                "hints": [
                    "raise ValueError('message') throws an exception upward.",
                    "try/except ValueError catches it.",
                    "The starter is already correct — study it to understand the pattern.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 6 · FILE I/O
    # ══════════════════════════════════════════════════════
    {
        "number": 6,
        "title": "File I/O",
        "intro": "Read from and write to files, and work with CSV data.",
        "tasks": [
            {
                "id": "w6t1",
                "title": "Write & Read a File",
                "concept": "open(), with, read/write modes",
                "description": """\
Ask for a name, write "Hello, <name>!" to greeting.txt, then read and print it.

  Input: Alice  →  Hello, Alice!""",
                "starter": (
                    "# Week 6, Task 1 — Write & Read a File\n\n"
                    "name = input(\"Name: \")\n\n"
                    "with open(\"greeting.txt\", \"w\") as f:\n"
                    "    f.write(f\"Hello, {name}!\")\n\n"
                    "with open(\"greeting.txt\", \"r\") as f:\n"
                    "    print(f.read())\n"
                ),
                "tests": [
                    {"input": "Alice\n", "expected": "Hello, Alice!"},
                    {"input": "CS50\n",  "expected": "Hello, CS50!"},
                ],
                "hints": [
                    "open('file', 'w') creates/overwrites; 'r' reads.",
                    "Use with to auto-close: with open(...) as f: ...",
                    "f.write() writes a string; f.read() returns the whole file as a string.",
                ],
            },
            {
                "id": "w6t2",
                "title": "CSV DictReader",
                "concept": "csv.DictReader",
                "description": """\
Read a CSV file and print each row.
Your program should create the CSV itself, then read it.

CSV contents:
  name,house
  Harry,Gryffindor
  Draco,Slytherin
  Luna,Ravenclaw

Expected output:
  Harry is in Gryffindor
  Draco is in Slytherin
  Luna is in Ravenclaw""",
                "starter": (
                    "# Week 6, Task 2 — CSV DictReader\n"
                    "import csv\n\n"
                    "# Create the test CSV\n"
                    "with open(\"students.csv\", \"w\") as f:\n"
                    "    f.write(\"name,house\\n\")\n"
                    "    f.write(\"Harry,Gryffindor\\n\")\n"
                    "    f.write(\"Draco,Slytherin\\n\")\n"
                    "    f.write(\"Luna,Ravenclaw\\n\")\n\n"
                    "# Read with DictReader\n"
                    "with open(\"students.csv\") as f:\n"
                    "    reader = csv.DictReader(f)\n"
                    "    for row in reader:\n"
                    "        print(f\"{row['name']} is in {row['house']}\")\n"
                ),
                "tests": [
                    {"input": "\n", "expected": "Harry is in Gryffindor\nDraco is in Slytherin\nLuna is in Ravenclaw"},
                ],
                "hints": [
                    "csv.DictReader reads each row as a dict keyed by column header.",
                    "Access fields with row['name'] and row['house'].",
                    "The starter is correct — run it to see it work.",
                ],
            },
            {
                "id": "w6t3",
                "title": "Collect & Sort Names",
                "concept": "file append mode, sorted()",
                "description": """\
Ask for names (one per prompt) until the user presses Enter with no input.
Write each name to names.txt, then read and print them sorted alphabetically.

  Input: Charlie, Alice, Bob, (empty Enter)
  Output:
    Alice
    Bob
    Charlie""",
                "starter": (
                    "# Week 6, Task 3 — Collect & Sort Names\n\n"
                    "with open(\"names.txt\", \"w\") as f:\n"
                    "    while True:\n"
                    "        name = input(\"Name: \")\n"
                    "        if not name:\n"
                    "            break\n"
                    "        f.write(name + \"\\n\")\n\n"
                    "with open(\"names.txt\") as f:\n"
                    "    names = f.read().splitlines()\n\n"
                    "for name in sorted(names):\n"
                    "    print(name)\n"
                ),
                "tests": [
                    {"input": "Charlie\nAlice\nBob\n\n", "expected": "Alice\nBob\nCharlie"},
                    {"input": "Zara\nAmy\n\n",           "expected": "Amy\nZara"},
                ],
                "hints": [
                    "Open with 'w' to start fresh each run.",
                    "f.read().splitlines() gives a list of lines without \\n.",
                    "sorted(names) returns a new sorted list.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 7 · REGULAR EXPRESSIONS
    # ══════════════════════════════════════════════════════
    {
        "number": 7,
        "title": "Regular Expressions",
        "intro": "Search and manipulate text with the re module and pattern matching.",
        "tasks": [
            {
                "id": "w7t1",
                "title": "Validate Email",
                "concept": "re.search(), patterns",
                "description": r"""\
Ask for an email address. Print "Valid" if it matches the pattern
\S+@\S+\.\S+  (something@something.something), else "Invalid".

  malan@harvard.edu  →  Valid
  not-an-email       →  Invalid
  a@b.c              →  Valid
  missing@domain     →  Invalid""",
                "starter": (
                    "# Week 7, Task 1 — Email Validator\n"
                    "import re\n\n"
                    "email = input(\"Email: \")\n\n"
                    r'if re.search(r"^\S+@\S+\.\S+$", email):' + "\n"
                    "    print(\"Valid\")\n"
                    "else:\n"
                    "    print(\"Invalid\")\n"
                ),
                "tests": [
                    {"input": "malan@harvard.edu\n", "expected": "Valid"},
                    {"input": "not-an-email\n",       "expected": "Invalid"},
                    {"input": "a@b.c\n",              "expected": "Valid"},
                    {"input": "missing@domain\n",     "expected": "Invalid"},
                ],
                "hints": [
                    r're.search(r"^\S+@\S+\.\S+$", email) — \S+ = 1+ non-whitespace chars',
                    r"\. matches a literal dot (without backslash, . matches any char)",
                    "^ anchors to start, $ anchors to end of string.",
                ],
            },
            {
                "id": "w7t2",
                "title": "Extract & Sum Numbers",
                "concept": "re.findall()",
                "description": r"""\
Ask for a sentence. Extract all integers from it with re.findall() and print their sum.

  "I have 3 cats and 12 dogs"  →  15
  "No numbers here"            →  0
  "100 plus 200 equals 300"    →  600""",
                "starter": (
                    "# Week 7, Task 2 — Extract & Sum Numbers\n"
                    "import re\n\n"
                    "sentence = input(\"Sentence: \")\n"
                    r'numbers = re.findall(r"\d+", sentence)' + "\n"
                    "total = sum(int(n) for n in numbers)\n"
                    "print(total)\n"
                ),
                "tests": [
                    {"input": "I have 3 cats and 12 dogs\n", "expected": "15"},
                    {"input": "No numbers here\n",           "expected": "0"},
                    {"input": "100 plus 200 equals 300\n",   "expected": "600"},
                ],
                "hints": [
                    r're.findall(r"\d+", text) returns a list of digit strings.',
                    "Convert each to int before summing: [int(n) for n in numbers]",
                    "sum([]) == 0, so 'No numbers' outputs 0 automatically.",
                ],
            },
            {
                "id": "w7t3",
                "title": "Clean Phone Number",
                "concept": "re.sub()",
                "description": r"""\
Ask for a phone number in any format. Remove all non-digit characters and print it.

  (617) 495-1000  →  6174951000
  617.495.1000    →  6174951000
  6174951000      →  6174951000""",
                "starter": (
                    "# Week 7, Task 3 — Clean Phone Number\n"
                    "import re\n\n"
                    "phone = input(\"Phone: \")\n"
                    r'cleaned = re.sub(r"\D", "", phone)' + "\n"
                    "print(cleaned)\n"
                ),
                "tests": [
                    {"input": "(617) 495-1000\n", "expected": "6174951000"},
                    {"input": "617.495.1000\n",   "expected": "6174951000"},
                    {"input": "6174951000\n",      "expected": "6174951000"},
                    {"input": "617-495-1000\n",    "expected": "6174951000"},
                ],
                "hints": [
                    r're.sub(r"\D", "", phone) replaces every non-digit with "".',
                    r"\D is the complement of \d (matches anything that is NOT a digit).",
                    "re.sub(pattern, replacement, string) → returns new string.",
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 8 · OBJECT-ORIENTED PROGRAMMING
    # ══════════════════════════════════════════════════════
    {
        "number": 8,
        "title": "Object-Oriented Programming",
        "intro": "Model entities with classes, methods, properties, and special methods.",
        "tasks": [
            {
                "id": "w8t1",
                "title": "Student Class",
                "concept": "class, __init__, __str__",
                "description": """\
Create a Student class:
  • __init__(self, name, house)
  • __str__ returns "<name> from <house>"

  Input: Harry  then  Gryffindor
  Output: Harry from Gryffindor""",
                "starter": (
                    "# Week 8, Task 1 — Student Class\n\n"
                    "class Student:\n"
                    "    def __init__(self, name, house):\n"
                    "        self.name = name\n"
                    "        self.house = house\n\n"
                    "    def __str__(self):\n"
                    "        return f\"{self.name} from {self.house}\"\n\n\n"
                    "name  = input(\"Name: \")\n"
                    "house = input(\"House: \")\n"
                    "student = Student(name, house)\n"
                    "print(student)\n"
                ),
                "tests": [
                    {"input": "Harry\nGryffindor\n", "expected": "Harry from Gryffindor"},
                    {"input": "Draco\nSlytherin\n",  "expected": "Draco from Slytherin"},
                ],
                "hints": [
                    "def __init__(self, name, house): self.name = name; self.house = house",
                    'def __str__(self): return f"{self.name} from {self.house}"',
                    "__str__ is called automatically when you pass an object to print().",
                ],
            },
            {
                "id": "w8t2",
                "title": "Property with Validation",
                "concept": "@property, @setter",
                "description": """\
Add house validation to Student using @property:
  • Valid houses: Gryffindor, Slytherin, Ravenclaw, Hufflepuff
  • Raise ValueError for anything else

  Harry / Gryffindor   →  Harry from Gryffindor
  Harry / InvalidHouse →  Invalid house""",
                "starter": (
                    "# Week 8, Task 2 — Property with Validation\n\n"
                    "class Student:\n"
                    "    def __init__(self, name, house):\n"
                    "        self.name  = name\n"
                    "        self.house = house   # triggers the setter\n\n"
                    "    @property\n"
                    "    def house(self):\n"
                    "        return self._house\n\n"
                    "    @house.setter\n"
                    "    def house(self, house):\n"
                    "        if house not in [\"Gryffindor\", \"Slytherin\", \"Ravenclaw\", \"Hufflepuff\"]:\n"
                    "            raise ValueError(\"Invalid house\")\n"
                    "        self._house = house\n\n"
                    "    def __str__(self):\n"
                    "        return f\"{self.name} from {self.house}\"\n\n\n"
                    "name  = input(\"Name: \")\n"
                    "house = input(\"House: \")\n"
                    "try:\n"
                    "    s = Student(name, house)\n"
                    "    print(s)\n"
                    "except ValueError:\n"
                    "    print(\"Invalid house\")\n"
                ),
                "tests": [
                    {"input": "Harry\nGryffindor\n",  "expected": "Harry from Gryffindor"},
                    {"input": "Harry\nInvalidHouse\n","expected": "Invalid house"},
                    {"input": "Luna\nRavenclaw\n",    "expected": "Luna from Ravenclaw"},
                ],
                "hints": [
                    "@property creates a getter; @house.setter creates a setter.",
                    "Setting self.house in __init__ automatically calls the setter.",
                    "Store the validated value in self._house (private, with underscore).",
                ],
            },
            {
                "id": "w8t3",
                "title": "Class Method",
                "concept": "@classmethod",
                "description": """\
Add a class method Student.from_string(s) that parses "Name, House" and returns a Student.

  Input: "Harry, Gryffindor"  →  Harry from Gryffindor""",
                "starter": (
                    "# Week 8, Task 3 — Class Method\n\n"
                    "class Student:\n"
                    "    def __init__(self, name, house):\n"
                    "        self.name  = name\n"
                    "        self.house = house\n\n"
                    "    @classmethod\n"
                    "    def from_string(cls, s):\n"
                    "        name, house = s.split(\", \")\n"
                    "        return cls(name, house)\n\n"
                    "    def __str__(self):\n"
                    "        return f\"{self.name} from {self.house}\"\n\n\n"
                    "s = input(\"Student: \")\n"
                    "student = Student.from_string(s)\n"
                    "print(student)\n"
                ),
                "tests": [
                    {"input": "Harry, Gryffindor\n", "expected": "Harry from Gryffindor"},
                    {"input": "Draco, Slytherin\n",  "expected": "Draco from Slytherin"},
                ],
                "hints": [
                    "@classmethod takes cls (the class itself) as first param instead of self.",
                    "cls(name, house) is equivalent to Student(name, house).",
                    's.split(", ") → ["Harry", "Gryffindor"]',
                ],
            },
            {
                "id": "w8t4",
                "title": "Operator Overloading",
                "concept": "__add__, __str__",
                "description": """\
Create a Vector class with x and y. Overload + so two vectors can be added.

  v1 = Vector(1, 2),  v2 = Vector(3, 4)
  print(v1 + v2)  →  (4, 6)""",
                "starter": (
                    "# Week 8, Task 4 — Operator Overloading\n\n"
                    "class Vector:\n"
                    "    def __init__(self, x, y):\n"
                    "        self.x = x\n"
                    "        self.y = y\n\n"
                    "    def __add__(self, other):\n"
                    "        return Vector(self.x + other.x, self.y + other.y)\n\n"
                    "    def __str__(self):\n"
                    "        return f\"({self.x}, {self.y})\"\n\n\n"
                    "x1, y1 = map(int, input(\"v1 (x y): \").split())\n"
                    "x2, y2 = map(int, input(\"v2 (x y): \").split())\n"
                    "v1 = Vector(x1, y1)\n"
                    "v2 = Vector(x2, y2)\n"
                    "print(v1 + v2)\n"
                ),
                "tests": [
                    {"input": "1 2\n3 4\n",  "expected": "(4, 6)"},
                    {"input": "0 0\n5 5\n",  "expected": "(5, 5)"},
                    {"input": "-1 3\n1 -3\n","expected": "(0, 0)"},
                ],
                "hints": [
                    "__add__(self, other) is called when you write v1 + v2.",
                    "Return a new Vector — don't modify self.",
                    '__str__ should return f"({self.x}, {self.y})"',
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    # WEEK 9 · ET CETERA
    # ══════════════════════════════════════════════════════
    {
        "number": 9,
        "title": "Et Cetera",
        "intro": "Advanced Python: sets, generators, type hints, and list comprehensions.",
        "tasks": [
            {
                "id": "w9t1",
                "title": "Unique Words with Sets",
                "concept": "set(), sorted()",
                "description": """\
Ask for a comma-separated list of words. Print unique words alphabetically (one per line).

  Input:  apple, banana, apple, cherry, banana
  Output:
    apple
    banana
    cherry""",
                "starter": (
                    "# Week 9, Task 1 — Sets\n\n"
                    "words_input = input(\"Words: \")\n"
                    "words  = [w.strip() for w in words_input.split(\",\")]\n"
                    "unique = sorted(set(words))\n"
                    "for word in unique:\n"
                    "    print(word)\n"
                ),
                "tests": [
                    {"input": "apple, banana, apple, cherry, banana\n",
                     "expected": "apple\nbanana\ncherry"},
                    {"input": "cat, dog, cat\n", "expected": "cat\ndog"},
                    {"input": "one\n",            "expected": "one"},
                ],
                "hints": [
                    "set() removes duplicates; sorted() returns an alphabetically sorted list.",
                    '.split(",") splits on commas; .strip() removes surrounding spaces.',
                    "The starter is already correct — read it to understand the pattern.",
                ],
            },
            {
                "id": "w9t2",
                "title": "Generator Function",
                "concept": "yield, generators",
                "description": """\
Write a generator squares_up_to(n) that yields perfect squares (1, 4, 9, …) up to n.

  n=20  →  1  4  9  16   (each on its own line)
  n=25  →  1  4  9  16  25
  n=1   →  1""",
                "starter": (
                    "# Week 9, Task 2 — Generator\n\n"
                    "def squares_up_to(n):\n"
                    "    i = 1\n"
                    "    while i * i <= n:\n"
                    "        yield i * i\n"
                    "        i += 1\n\n\n"
                    "n = int(input(\"n: \"))\n"
                    "for square in squares_up_to(n):\n"
                    "    print(square)\n"
                ),
                "tests": [
                    {"input": "20\n", "expected": "1\n4\n9\n16"},
                    {"input": "25\n", "expected": "1\n4\n9\n16\n25"},
                    {"input": "1\n",  "expected": "1"},
                    {"input": "3\n",  "expected": "1"},
                ],
                "hints": [
                    "yield pauses the function and hands a value to the caller each time.",
                    "A function with yield is a 'generator function'.",
                    "while i * i <= n: yield i * i; i += 1",
                ],
            },
            {
                "id": "w9t3",
                "title": "Type Hints & List Comprehension",
                "concept": "type annotations, list comprehension",
                "description": """\
Write two annotated functions:
  def greet(name: str) -> str:         returns "Hello, <name>!"
  def double_all(nums: list[int]) -> list[int]:  returns each number doubled

Then:
  • Ask for a name → print greet(name)
  • Ask for space-separated numbers → print double_all(nums)

  Input: Alice, then 1 2 3
  Output:
    Hello, Alice!
    [2, 4, 6]""",
                "starter": (
                    "# Week 9, Task 3 — Type Hints\n\n"
                    "def greet(name: str) -> str:\n"
                    "    return f\"Hello, {name}!\"\n\n\n"
                    "def double_all(nums: list[int]) -> list[int]:\n"
                    "    return [n * 2 for n in nums]\n\n\n"
                    "name = input(\"Name: \")\n"
                    "print(greet(name))\n\n"
                    "raw = list(map(int, input(\"Numbers: \").split()))\n"
                    "print(double_all(raw))\n"
                ),
                "tests": [
                    {"input": "Alice\n1 2 3\n", "expected": "Hello, Alice!\n[2, 4, 6]"},
                    {"input": "Bob\n5 10\n",    "expected": "Hello, Bob!\n[10, 20]"},
                ],
                "hints": [
                    "Type hints (param: type, -> return) are documentation only — no runtime effect.",
                    "[n * 2 for n in nums] is a list comprehension.",
                    "map(int, ...) converts each element to int; list() materialises it.",
                ],
            },
        ],
    },
]

# ──────────────────────────────────────────────────────────
# ENGINE CONSTANTS
# ──────────────────────────────────────────────────────────
PROGRESS_FILE = "cs50p_progress.json"
ANSWER_FILE   = "answer.py"
TOTAL_TASKS   = sum(len(w["tasks"]) for w in WEEKS)


# ──────────────────────────────────────────────────────────
# PROGRESS  (JSON)
# ──────────────────────────────────────────────────────────
def load_progress() -> dict:
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "score": 0}

def save_progress(progress: dict) -> None:
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


# ──────────────────────────────────────────────────────────
# DISPLAY HELPERS
# ──────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""
{BOLD}{C}╔══════════════════════════════════════════════════════════╗
║  CS50P Interactive Quiz                                  ║
║  Harvard's Introduction to Programming with Python       ║
╚══════════════════════════════════════════════════════════╝{RST}""")

def progress_bar(progress: dict):
    done  = len(progress["completed"])
    width = 40
    fill  = int(width * done / TOTAL_TASKS) if TOTAL_TASKS else 0
    bar   = "█" * fill + "░" * (width - fill)
    pts   = progress.get("score", 0)
    print(f"\n{BOLD}Progress:{RST} [{green(bar)}] {done}/{TOTAL_TASKS} tasks  |  {yellow(str(pts) + ' pts')}\n")


# ──────────────────────────────────────────────────────────
# TEST RUNNER
# ──────────────────────────────────────────────────────────
def outputs_match(actual: str, expected: str) -> bool:
    """
    Compare actual vs expected output, tolerating input() prompt noise.

    When Python pipes stdin, input("prompt") writes the prompt to stdout on the
    SAME line as the following print() output, e.g.:
        actual:   "x: y: 3"     expected: "3"
        actual:   "n: 3\\n2\\n1\\nBlastoff!"  expected: "3\\n2\\n1\\nBlastoff!"

    Strategy: the last N actual lines should match the N expected lines,
    where the FIRST matched line may have a prompt prefix (ending in ': ' or '? ').
    """
    actual   = actual.strip()
    expected = expected.strip()
    if actual == expected:
        return True

    actual_lines   = actual.split("\n")
    expected_lines = expected.split("\n")
    n = len(expected_lines)
    if n > len(actual_lines):
        return False

    tail = actual_lines[-n:]
    # First line may have a prompt prefix — check it ends with the expected line
    if not tail[0].endswith(expected_lines[0]):
        return False
    # The prefix (noise) must look like a prompt (ends with ': ' or '? ')
    prefix = tail[0][: len(tail[0]) - len(expected_lines[0])]
    if prefix and not (prefix.endswith(": ") or prefix.endswith("? ")):
        return False
    # Remaining lines must match exactly
    return tail[1:] == expected_lines[1:]

def run_test(test: dict, extra_argv: list | None = None) -> tuple[str, str, int]:
    cmd = [sys.executable, ANSWER_FILE] + (extra_argv or [])
    try:
        res = subprocess.run(
            cmd,
            input=test.get("input", ""),
            capture_output=True,
            text=True,
            timeout=10,
        )
        return res.stdout.strip(), res.stderr.strip(), res.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT — your program ran for >10 s.", 1
    except Exception as exc:
        return "", str(exc), 1

def grade_task(task: dict) -> tuple[int, int, list[dict]]:
    passed, failures = 0, []
    for test in task["tests"]:
        validator = test.get("validator")

        if validator == "range_1_to_n":
            stdout, stderr, rc = run_test(test)
            n_val = test["n_value"]
            if rc == 0 and stdout.lstrip("-").isdigit() and 1 <= int(stdout) <= n_val:
                passed += 1
            else:
                failures.append({
                    "input": test["input"],
                    "expected": f"A number between 1 and {n_val}",
                    "got": stdout or stderr,
                })
            continue

        if validator == "heads_tails_sum":
            stdout, stderr, rc = run_test(test)
            n_val = test["n_value"]
            ok = False
            lines = stdout.split("\n")
            if len(lines) == 2:
                try:
                    h = int(lines[0].split(": ")[1])
                    t = int(lines[1].split(": ")[1])
                    ok = (h + t == n_val)
                except (IndexError, ValueError):
                    pass
            if ok:
                passed += 1
            else:
                failures.append({
                    "input": test["input"],
                    "expected": f"Heads: X\\nTails: Y  where X+Y=={n_val}",
                    "got": stdout or stderr,
                })
            continue

        # Normal test (optionally with extra argv)
        argv   = test.get("argv")
        stdout, stderr, rc = run_test(test, argv)
        expected = (test.get("expected") or "").strip()
        if outputs_match(stdout, expected):
            passed += 1
        else:
            failures.append({
                "input":    test.get("input", ""),
                "expected": expected,
                "got":      stdout,
                "stderr":   stderr,
            })

    return passed, len(task["tests"]), failures


# ──────────────────────────────────────────────────────────
# TASK INTERACTION
# ──────────────────────────────────────────────────────────
def show_task(week_number: int, task: dict):
    print(f"\n{BOLD}{B}━━━ Week {week_number} · {task['title']} ━━━{RST}")
    print(f"{dim('Concept: ' + task['concept'])}\n")
    print(task["description"])
    print()

def attempt_task(week: dict, task: dict, progress: dict) -> bool:
    """Return True if task was passed."""
    show_task(week["number"], task)

    # Write starter code
    with open(ANSWER_FILE, "w") as f:
        f.write(task["starter"])

    hints      = task.get("hints", [])
    hint_idx   = 0
    attempts   = 0

    print(f"{Y}📝  Edit '{ANSWER_FILE}' in your editor, then press Enter when ready.{RST}")
    print(f"{dim('   (Starter code written for you)')}\n")

    while True:
        try:
            input(f"{BOLD}Press Enter to test…{RST} ")
        except KeyboardInterrupt:
            print(f"\n{dim('Interrupted. Returning to menu.')}")
            return False

        if not os.path.exists(ANSWER_FILE):
            print(red(f"❌  '{ANSWER_FILE}' not found — make sure you saved it."))
            continue

        print(f"\n{dim('Running tests…')}")
        passed, total, failures = grade_task(task)
        attempts += 1

        # ── PASS ──
        if passed == total:
            print(f"\n{BOLD}{G}✅  {passed}/{total} tests passed — great work!{RST}")
            if task["id"] not in progress["completed"]:
                progress["completed"].append(task["id"])
                # Points: more for fewer attempts
                pts = max(1, 4 - attempts)
                progress["score"] = progress.get("score", 0) + pts
                total_pts = progress["score"]
                print(dim(f"   +{pts} point(s)  (total: {total_pts})"))
            save_progress(progress)
            try:
                input(f"\n{dim('Press Enter to continue…')}")
            except KeyboardInterrupt:
                pass
            return True

        # ── FAIL ──
        print(f"\n{R}❌  {passed}/{total} tests passed.{RST}\n")
        for i, fail in enumerate(failures[:3], 1):
            inp = fail.get("input", "").strip()
            print(f"  {BOLD}Test {i}{RST}")
            if inp:
                print(f"    Input    : {yellow(repr(inp))}")
            print(f"    Expected : {green(repr(fail['expected']))}")
            print(f"    Got      : {red(repr(fail['got']))}")
            if fail.get("stderr"):
                snippet = fail["stderr"].splitlines()[-1][:120]
                print(f"    Error    : {red(snippet)}")
        print()

        # Action prompt
        h_label = f"[{BOLD}h{RST}]int" if hint_idx < len(hints) else dim("[h]int (none left)")
        try:
            action = input(
                f"  [{BOLD}r{RST}]etry  {h_label}  [{BOLD}s{RST}]kip  [{BOLD}q{RST}]uit : "
            ).strip().lower()
        except KeyboardInterrupt:
            return False

        if action == "h":
            if hint_idx < len(hints):
                print(f"\n  {Y}💡 Hint {hint_idx+1}/{len(hints)}: {hints[hint_idx]}{RST}\n")
                hint_idx += 1
            else:
                print(f"\n  {dim('No more hints.')}\n")
        elif action == "s":
            print(f"\n{dim('Skipping…')}")
            return False
        elif action == "q":
            save_progress(progress)
            print(f"\n{Y}Progress saved. Bye!{RST}\n")
            sys.exit(0)
        # else: retry


# ──────────────────────────────────────────────────────────
# WEEK / MENU
# ──────────────────────────────────────────────────────────
def run_week(week_number: int, progress: dict):
    week = next((w for w in WEEKS if w["number"] == week_number), None)
    if not week:
        print(red(f"Week {week_number} not found."))
        return

    done_set = set(progress["completed"])
    print(f"\n{BOLD}{M}{'━'*50}{RST}")
    print(f"{BOLD}{M}  Week {week['number']}: {week['title']}{RST}")
    print(f"{M}  {week['intro']}{RST}")
    print(f"{BOLD}{M}{'━'*50}{RST}\n")

    for task in week["tasks"]:
        if task["id"] in done_set:
            print(f"  {green('✓')} {task['title']} {dim('(already completed)')}")
        else:
            attempt_task(week, task, progress)


def find_next_task(progress: dict):
    done_set = set(progress["completed"])
    for week in WEEKS:
        for task in week["tasks"]:
            if task["id"] not in done_set:
                return week, task
    return None, None


def menu(progress: dict) -> str:
    done_set = set(progress["completed"])
    print(f"{BOLD}Select a Week:{RST}\n")
    for week in WEEKS:
        ids   = [t["id"] for t in week["tasks"]]
        done  = sum(1 for i in ids if i in done_set)
        total = len(ids)
        tick  = green(f"✓ {done}/{total}") if done == total else yellow(f"  {done}/{total}")
        print(f"  {BOLD}[{week['number']}]{RST}  Week {week['number']}: {week['title']:30s} {tick}")

    print()
    print(f"  {BOLD}[a]{RST}  Auto-continue from next incomplete task")
    print(f"  {BOLD}[q]{RST}  Quit\n")

    try:
        return input("Choose: ").strip().lower()
    except KeyboardInterrupt:
        return "q"


# ──────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────
def main():
    clear()
    banner()
    progress = load_progress()

    while True:
        progress_bar(progress)

        if len(progress["completed"]) == TOTAL_TASKS:
            print(f"{BOLD}{G}🎉  You've completed all {TOTAL_TASKS} CS50P tasks!{RST}")
            print(f"    Final score: {yellow(str(progress.get('score', 0)))} points\n")
            sys.exit(0)

        choice = menu(progress)

        if choice == "q":
            print(f"\n{Y}Progress saved. See you next time!{RST}\n")
            sys.exit(0)

        elif choice == "a":
            week, _ = find_next_task(progress)
            if week:
                run_week(week["number"], progress)
            else:
                print(green("All done!"))
                sys.exit(0)

        elif choice.isdigit() and 0 <= int(choice) <= 9:
            run_week(int(choice), progress)

        else:
            print(red("Enter 0–9, 'a', or 'q'."))

        clear()
        banner()


if __name__ == "__main__":
    main()
