for Solution A:
for this solution it seems like it relies heavily on list comprehension and the heap. it takes in a list of items needed to be sorted an breaks it down into a tuple with two differnt variables. it does list comprehension to find the frequncy of k items and then goes into the heap to compare each one to see the winner/most frequent. this does seem to be a little bit more complicated than what it needs to be though with a lot of high load stuff.

for Solution B:
solution B is somewhat similar to A but uses a lot less complications. it does not use the heap but instead jsut uses the built in sorting method within python. then it uses a lambda function to find and grab the largest. now I think A is probably going to be more accurtiate because I could not really see where it takes into account the tie case, but maybe that gets handled with sort as well.

Solution C:
Solution C is definitly going to be the slowest. it uses a lot of for loops and one main list to parse through and find the most frequent. honestly, this is probably how I would have done it. it looks to me the most "human-like" out of the three. it gets the job done but is very very rudimentary and slow.

prediction one: I would say part B is going to break as the list gets bigger. part b is jsut realing on a lambda func and a sort method for the frequncies whereas a has the heap it can lean on and c will just take forever but run.

prediction two: Honestly, C. I think it is going to have the most reliabilty out of the other two. it will defintly be slower but I think the condednsed, one list parsing, is going to be more reliable than the heap or lambda 

