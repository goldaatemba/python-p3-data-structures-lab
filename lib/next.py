# The next() function returns the next item in an iterator.
# You can add a default return value, to return if the iterator has reached to its end.
# @params: iterator, default::optional

my_list = iter(["apple", "banana", "cherry"])
x = next(my_list, "orange")
print(x) # => apple

x = next(my_list, "orange")
print(x) # => banana

x = next(my_list, "orange")
print(x) # => cherry

x = next(my_list, "orange")
print(x) # => orange