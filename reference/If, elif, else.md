---
title: 'If, elif, else'
created: '2022-09-02T14:58:48.788Z'
modified: '2022-09-02T15:25:40.660Z'
---

# If, elif, else

> - `if` statments allow you to **selectively choose** which **piece of code to run** based on some **conditions**

## Syntax and operation
```
if (condition):
  ...code
elif (condition):
  ...code
elif (condition):
  ...code
else:
  ..code
```

- An `if` statment executes code if `condition` evaluates to `True`
  - If not `True`, it checks the next `condition` in the `elif` block, and then the next.
    - If no `condition` is found to be `True`, it executes the `else` block

---

- If any condition is found to be `True`, it executes its code block
  - And then **skips** all of the remaining blocks of code.

---

- Conditions are checked from top to bottom
- The `elif` and `else` blocks are optional.
- There can be as many `elif` statments as needed.

## Nested `if` statments
> - An `if` statment can contain another `if` statment
```
if (loggedIn):
    if (isOwnerOfThing or hasAdminPermissions):
        if (confirmedToDeleteThing):
        
            deleteThing()
        
        else:
            print('please confirm you want to delete')
    else:
        print('not allowed to delete this thing')
else:
  print('please log in first')
```

- This can also be written without nesting:
```
if (loggedIn and (isOwnerOfThing or hasAdminPermissions) and confirmedToDeleteThing):

    deleteThing()

else:
  print('something went wrong')
```
- However this method has the **drawback** that you **dont know which condition failed**
  - All you know is that **at least one of them failed**








