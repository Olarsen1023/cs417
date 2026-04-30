three things that would be hard to change is; it seems like it would be hard to change the main data and logic of main, it seems like the cost sets are linked pretty close to the main part of the program, and then the expense report also looks tough to swtich over.

actually I feel like I was totally wrong. the only thing that was slightly diffictuly to refactor was the bulding the report. having it as a pure function so that it is way more flexibale was a little tough with how rigid the program was in the begining. other than that, parseing the CSV was pretty easy to move that stuff from a more caveman-ish code to a way sleeker looking program. it was also pretty much the same thing on the JSON

for part one: I sued a single responsibilaty stragety to tackle handling the data. this is defintly not something that could be plug in play but it works for this program.
for part two: I did a "template" pluggable parts. this allows it so if the cattigories get larger or if it needs to move to a diffent type of function, it is able to be plug right into it!
for part three: I did the same type of thing for this guy. building the report is jsut a pure building of the raw data. there is no dependency on anything else, just the data it is given.

Bulding the report and the new logic for main was probably the most idfficult part. it took me a while parse thorugh and figure out what was going on in the main and how to change what I needed to. my first attempt was to just mess with the categories and the report but I didn't even think of the CSV that needed to be loaded in in order for the data to be read properly but the other functions.

I think the future change would be making it an entire template that can be tweaked slightly for differnt operations. for the API calls, I would just change the CSV to the API but make sure it is not too tight on that certain API.