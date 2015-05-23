# Memo for Final Project

### Quick pitch

Parents of Chicago Public School students need a clearer, more comprehensive tool to check on the status of recent health inspections.

### The old way

Chicago publishes its food inspections for food institutions of all kinds -- from retaurants to food trucks to school cafeterias -- in an open data forum online. It is updated frequently and often, and from what I can tell, it's largely accurate. 

There is no conneciton, however, between that data dump and getting inforamtion to parents about their school cafeterias (arguably the most interesting, as they involve cute little kids, CPS funding has been in the toilet for years, and often the hot food provided at school for low income kids is a large portion of their daily nutrition). While schools may be technically required to send notifications to parents on the status of these health inspections, and whether or not they are going on at all, many do not. 

News media outlets (particularly in recent months) have done a nice job of highlighting this problem -- both that schools are getting major violations and that parents don't know about it. Check out a recent report (here)[http://chicago.cbslocal.com/2015/02/09/2-investigators-more-failed-food-inspections-at-schools/]. 

The Chicago Tribune, which has an awesome data component, (built a great tool)[http://www.chicagotribune.com/ct-chicago-daycare-food-service-inspections-20150514-htmlstory.html] related exclusively to daycare inspections that cross-referenced all the liscenced day cares in the city with the food inspection list, finding that there were several missing. They whipped it up into a great tool to see the issues around 2014 data... and to my mind, an even better tool (though similar to this one) should also be built for the larger category of schools. 

Parents of children in CPS want a few things, at the core: 
1. They want to know when their school is being inspected for food and why (or why not)
2. They want to know the results of those inspections, including detailed violations

Some additional information they may be interested in knowing, though I have to do more research:
1. Which schools are historically worst, and is my school among them?
2. Which schools are not getting the inspections they need, or being overlooked all together?
3. Which schools are best? And how does their track record look?

### The new way

_My tool for making this happen will do the following:_
- gather the data on all CPS liscenced schools, to see how many total for the years 2010 to 2015
- cross-reference that data over the food inspection data from 2010-2015
- with that data cross-referenced on the back end, users can type in the name of their school (even with just keywords) and receive a visualized "timeline" between 2010 and 2015
- I picture that this will look like a small line, with colored points on it between the years of 2010 and 2015 (green for pass, red for fail, etc.) -- this will show a visual history of how frequently the school has been visited and how well it has done. Then, the user can click on each of the dots to expand the list of violations or notes from that particular inspection
- Something I may add: a series of high level summaries for the "most visited schools" or the "best performing schools" over the years, as an additional tool for parents to see that, outside just the search bar
- Oooh, and in an ideal world, you can pull up a few and compare them at the same time!!! (I would have to think about how I could feasibly design that, but it'd be great.)

### My data will come from:
Chicago open data sets, as found from the city's website. They have listed all the CPS liscenced schools as well as the food inspection data. These are all downloadable CSV files, which makes my life easy on the front-end, in being abe to digest the gist of the data.

### Necessary cleaning:
Making sure that the data can be properly cross referenced will likely present a challenge. I need to make sure that repeating names, capital letters, etc do not confuse my program into misreading the data. That will likely take some big time cleaning on my part. 

In the food inspection data, however, things are rather clean. It may be a matter of pairing down all the violation listings that I want to include, but I may just print it all as parents find it interesting and it's not overwhelming if you are looking one school, one year at a time.

### How will the data be stored?
As I mentioned, the data is currently stored on an online database. I think I will clean the data myself, streamline it, etc after downloading it off the interwebs. Then I want to save a new CSV or series of CSVs and have my program upload and read it as a CSV file and translate into JSON. I did a little bit of practice with this for another project, and we touched on it in the flask app, so I think that's all okay.

### Who else has done it and how is your attempt better?

As I mentioned, the Tribune did a really clean data tool on daycare data. I don't want to reinvent the wheel here, because they were definitely smart about what they did and did not include. But, I want to work on CPS schools, which I believe is a more interesting topic due to budget issues. And more importantly, I want to reformat their table idea into an actual "timeline" visualization between the years of 2010 and 2015. I want to do this both to: 1) give the user a visual sense of the data, so they can understand and compare immediately and intuitively without having to read text (which I think is always a good goal for a viz), and also to 2) give a wider sense of time and history by doing a range of dates, which the table from the Trib does not have. 

### Pre-mortem

Alright, as per usual, this might be biting off more than I can chew. If I were to forecast this premordem, the cleaning of the data was too hard in the first place when trying to cross-reference the CPS total schools with the schools we know were inspected... and maybe I had to drop the cross-referencing all together and just run with the schools we know were inspected. (This idea to find the schools "falling through the cracks" came from the Tribune's work. But now I am thinking, well, it might not be the end of the world if I just run with the inspected schools and do a dope viz, now that I think about it. It would still be giving the schools a tool they don't have, while daycare does.) 

Also, the factor that could kill me is the design aspect of my proposed "timelime." I also need to make sure that isn't too heavy a programming lift for me, given the short timeframe. I might consider the same formatting as the China blocked websites viz, which could work well for me and also streamline the process a bit. Ideally, as I mentioned, each point would then have a clickable option in which the violations would expand for that year folks could read it.... but if I need to get down to the nitty-gritty, maybe the beautiful viz timeline, with the capacity to compare between schools at the same time, could be enough. 
Dan -- let me know what you would suggest, for the most useful ways and pair it down. I will think on it too.