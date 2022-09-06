# H.W Assignment #3: Loops

## Task #1
> Consider the following array:
>   - `[2, 5, 11, 93, 22, 122]`

- Write some code to **calculate** the **sum of all items** in the array

- Expected output: `255`

## Task #2
> Consider the following array:
>   - `[4, 11, 1, 3, 2, 6]`

- Write some code to **multiply** **each element** of the array **with `3`**
- **Save** these **calculated values** in a **new array**, and **print** that array
>
- Expected output: `[12, 33, 3, 9, 6, 18]`

## Task #3
> Consider the following arrays:
>   - `['red', 'green', 'orange', 'yellow', 'blue', 'black']`
>   - `['white', 'brown', 'purple', 'red', 'grey', 'maroon']`

- Write some code to **check** if the array **contains an element** with the value: `orange`

  - If found, print: `Found value 'orange' at index: {}`
  - If not found, print: `This array does not contain the value 'orange'`
>
- Run your code for **both** the arrays

  - Array1 expected output: `Found value 'orange' at index: 2`
  - Array2 expected output: `This array does not contain the value 'orange'`

# Task #4
- Consider the following code:
```python
# This code asks the user to enter their birth month (as a number).
# Since there are 12 months in a year, the only valid numbers are 1 to 12.
# So if the user enters something like 14, it is considered invalid.

# The code checks for this: if the month is invalid, throw an error and exit.

month = input('Please enter your birth month (as a number): ')

if (month < 1) or (month > 12):
    
    print('Error: Invalid month specified. Only values from 1 — 12 are allowed.')
    exit()
```
- While the code above works fine, it **abruptly exits** when given invalid data.
- It **would be better** if we **notify the user** of the error, but then instead of exiting, we **ask the user for input again**

#### Modify the code above, to keep asking the user for input, until they get it right.
