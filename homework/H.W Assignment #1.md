---
title: 'H.W Assignment #1'
created: '2022-08-28T13:40:21.734Z'
modified: '2022-09-02T19:15:04.234Z'
---

# H.W Assignment #1

> Note: You are allowed to use resources from the internet

## Task #1 (save as `task1.py`)
  - Ask the user to input a number
  - Consider this as the radius to a circle
>
  - Using the radius, calculate the circle's area and circumference
  - Print these values to the console
---

## Task #2 (save as `task2.py`)
Now let's try and improve our code's **reusability** with functions

  - Create a function called `calculate_area()`
    - It should take a single argument, the radius, and return area of circle
>
  - Create another function called `calculate_circumference()`
    - It should take a single argument, the radius, and return circumference of circle
>
  - Modify the code in task 1, to use the functions, instead of doing the calculations itself.
---

## Task 3 (save as `task3.py`)
Instead of doing the calculations **for a single circle**, lets modify our program to do them **for `x` amount of circles**

  - Make an empty array called `radii`
>
  - Ask the user to enter a radius, **make sure its a number**
  - Add the radius to our `radii` array
>
  - Ask the user to enter a radius, again, and then again.
  - Repeat this until the user enters 'stop'
    - Hint: use a `while` loop for this
      - search online how to exit out of a loop (hint: `break` keyword)
>
  - Now we have our `radii` array
    - Each item in this array is a radius
>

  - Use a `for` loop to loop over each item in this array
>
  - For each item, run the following code:
    - ```print(f'R: {radius}, A: {calculate_area(radius)}, C: {calculate_circumference(radius)}')```
