# Conditionals

## Booleans
- A `boolean` represents one of two values: `True` or `False`

## Boolean expressions
> - Boolean expressions are **expressions that evaluate** to either `True` or `False`
> - In this case, the word `evaluate` means to **work out** which one of two values it should be.
>
> - These expressions **make use of comparison operators**
>   - Such as `greater than (>)`, `less than (<)`, `equal to (==)`

For example:
  - `5 > 3` evaluates to `True`
  - `3 < 1` evaluates to `False`
  - `"someString" == "someString"` evaluates to `True`

| Operator |             Name             |
| -------- | ---------------------------- |
|    ==    |            Equals            |
|    !=    |          Not equals          |
|    <     |          Less than           |
|    >     |         Greater than         |
|    <=    | Less than **OR** Equal to    |
|    >=    | Greater than **OR** Equal to |


## Logical operators
> - Logical operators are used to **combine multiple boolean expressions**

| Operator |                Input                 |                         Description                         |
| -------- | ------------------------------------ | ----------------------------------------------------------- |
|   and    |   Takes **2** expressions as input   |     Evaluate to `True` if **both** expressions are true     |
|   or     |   Takes **2** expressions as input   |     Evaluate to `True` if **either** expression is true     |
|   not    | Takes **single** expression as input | Evaluates an expression normally, then reverses it's result |

For example:
  - `5 > 3 and "abc" == "abc"` evaluates to `True`
    - because both `5 > 3` **and** `"abc" == "abc"` evaluate to `True`
  
  - `5 == 5 or 5 == 3` evaluates to `True`
    - because `5 == 5` is evaluates to `True`
  
  - `not 4 == 4` evaluates to `False`
    - because `4 == 4` evaluates to `True` but then `not` flips it


## Evaluating arbitrary values

> - Some values are considered *'truthy'*, and others *'falsy'*.
>
>   - A `truthy` value is a value that is **considered true** when encountered in a **boolean context**
>
>   - And a `falsy` value is a value that is **considered false** when encountered in a **boolean context**

The `bool()` function allows you to evaluate **any value** to either `True` or `False`

For example:
  - `bool(15)` evaluates to `True`
  - `bool("")` evaluates to `False`
  - `bool("hello")` evaluates to `True`

#### What evaluates to what
- Almost any value is evaluated to `True` if it **has some sort of content**

  - All **numbers** evaluate `True`, except for `0`
  - All **strings** evaluate `True`, except empty ones
  - All **arrays** and **dicts** evaluate `True`, except empty ones

**Note**: the data-type `None` evaluates to `False`
