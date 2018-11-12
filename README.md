# pqdict
Thread-Safe Priority Queue Dictionary for Python
[![Build Status](https://travis-ci.com/mattpaletta/pqdict.svg?branch=master)](https://travis-ci.com/mattpaletta/pqdict)

## Instalation
PQDict has no external dependencies.
To install pqdict: 
```
pip install git+git://github.com/mattpaletta/pqdict.git
```

## Getting Started
You can see example uses in `tests/`.

To create a new instance (that can hold 10 elements):
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)
```

You can put elements in/out as follows:
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)
my_dict.set(key = "cat", value = 1)
my_dict.get(key = "cat") # Returns 1
my_dict.get(key = "dog") # Returns None

my_dict.contains(key = "cat") # Returns True
my_dict.contains(key = "dog") # Returns False
```

You must specify a `max_size` when creating a new instance.  At this time, this cannot be resized.
Everytime you get/set a value, that value is automatically moved to the front of the priority-queue.
Anything that exceeds the `max_size` is automatically removed from the list.


### Computing Values
You can also use it as a function cache for any function.  Here we are calling `F` with the parameter `10` if the value does not exist in our cache.
Subsequent values will use this same value.
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

my_dict.compute_if_not_exists(key = "mouse", fun = fib, n = 10)
my_dict.compute_if_not_exists("mouse", fib, 10)
```

There are a few other methods available for computing values:
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

my_dict.compute_if_not_exists(key = "mouse", fun = fib, n = 10)
my_dict.compute_if_not_value(key = "mouse", fun = fib, value = 55, n = 10)
my_dict.compute_and_set(key = "mouse", fun = fib, n = 10)
```

- `compute_if_not_exists` will only call the functino `fun` if there is no value in the dictionary for that key
- `compute_if_not_value` will only call `fun` if the key does not exist, or the value at that key does not equal `value`.
- `compute_and_set` calls the function everytime, and caches it's value.

### Using accessors
If you use the same function throughout your program to give to the cache, there are also accessors available.
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
    
not_exists = my_dict.compute_if_not_exists_accessor(fun = fib) # Returns 55
not_value = my_dict.compute_if_not_value_accessor(fun = fib, stored_value = 55) # Returns 55 (cached)
compute_and_set = my_dict.compute_and_set_accessor(fun = fib) # Returns 55

# Now we can use our `accessors`, using the function passed in earlier.
not_exists(key = "mouse", n = 10)

# We can override stored_value (which is optional) with value.
not_value(key = "mouse", n = 10)
not_value(key = "mouse", value = 2, n = 10)

compute_and_set(key = "mouse", n = 10)
```

### Transactions
The PQDict is also thread-safe.  You can start and end transactions (atomic operations) in two ways.
```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)

with my_dict as safe_dict:
    safe_dict.set(key = "cat", value = 1)
```

```python
from pqdict import PQDict
my_dict = PQDict(max_size = 10)

my_dict.begin_transaction()
my_dict.set(key = "cat", value = 1)
my_dict.end_transaction()
```

## Information

### Questions, Comments, Concerns, Queries, Qwibbles?

If you have any questions, comments, or concerns please leave them in the GitHub
Issues tracker:

https://github.com/mattpaletta/pqdict/issues

### Bug reports

If you discover any bugs, feel free to create an issue on GitHub. Please add as much information as
possible to help us fixing the possible bug. We also encourage you to help even more by forking and
sending us a pull request.

https://github.com/mattpaletta/pqdict/issues

## Maintainers

* Matthew Paletta (https://github.com/mattpaletta)

## License

GPL-3.0 License. Copyright 2018 Matthew Paletta. http://mrated.ca