Which section gave you a bug mypy caught that you wouldn’t have caught by reading the code? Be specific — what was the error message, what was the underlying mistake, and why is that kind of mistake easy to make in Python?

I probably would not have seen the annotation error! that is something when I read the orignal make_badge func I would not have thought of. but running it in the strict setting was cool to see it find it! the other was the type with the key lookup. it showed me exactly what was wrong where if I had to try and debug it myself would've taken me at least a little bit longer.


Runtime cost. Type hints don’t run at runtime — Python ignores them. Mypy is a separate tool you choose to run. What’s the cost and benefit of that design choice? What would change if Python enforced types at runtime the way Java does?

The cost of running mypy is effiency and computation data for coder but it gives a really good idea of how the code looks and does such a deep dive into all the nitty gritty that I think it's worth it. If python was like Java, mypy would be obsulete in my opion because it forces to check it on runtime, so mypy would have no use to my understnading.

TypedDict vs plain dict. A dict can play two roles: a record with a fixed set of named fields (like Lab 18’s roster row), or a mapping from variable keys to values (like Lab 20’s completed dict that maps submission IDs to results). For each of these two cases, would you reach for TypedDict or dict[K, V], and why?

for lab 18s scenario I would go for a dict. this allows for dynamic typing so that I am able to have some more varibality within the dict. lab 20, I would go for a Typedict because I know what is being returned. a set list of numbers to check on.
