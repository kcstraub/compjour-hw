# Pitch A
Every time someone tweets at my Twitter bot, called @B&EWatchSF, with the hashtag #nearme and their location, they will receive a tweet stating if there was a break and enter incident within 5 miles of their location in the last week. If there was a break and enter incident within that radius, the tweet will also state the location and caluculate exactly how many miles away from the tweeted location it occured. If there were also break and enter incidents outside that radius, the bot will include a number count of how many occured elsewhere and a link to the police crime report page. If no incident was within that radius, the bot will state that and instead include, as stated before, the information a number count of how many occured elsewhere and a link to the police crime report page.

# Steps

1. Bot checks Twitter API endpoint of statuses/mentions_timeline
2. For each Tweet, the bot will see if the #update hashtag was used, and read for the user's screen name and the ID of the tag.
3. Getting the location of the "tweeter": The location to look up is going to be the other text in that tweet, besides the @bot. Or, if the tweet has geolocation enabled, we use those coordinates.
4. If the location is an address string, use the Google Maps geocoding API to get lat/lng coordinates.
5. Getting the location and the date/time of the last break and enter in San Jose: The location to look up is going to be in the table listed automatically on SFPD open data site. The bot much navigate to that page, to the table view, search for 'Break and Enter' under the Crime Type column, and extract the 'Location' and 'Date/Time' cells in those particular rows.
6. The locations will be address strings, so the bot will use Google maps geocoding to get lat/lan coordinates.
7. The bot will compute the difference in mileage (using some formula I create) between the tweeted location and each geocoded result of the 'Break and Enter' extraction. 
8. If the mileage computed from this formula is 5 miles or less, the bot will tweet: "Be aware: this week on (insert Date/Time of incident, as extracted), a break and enter incident occured at (insert Location of incident, in string form) -- (insert number of miles, as computed by bot) miles from your location. (Insert number of other total locations detected) also occured farther from you. (Insert SFPD URL)"
9. If more than one location satisfies the >5 miles requirement, the bot will send a separate tweets with each location and its information.
10. If the milage computed does not yield any locations within 5 miles or less, the bot will tweet: "No break and enter incidents occured within 5 miles of your location this week. (Insert number of other total locations detected), however, occured farther from you this week. (Insert SFPD URL)"
11. For the above step, if there are no break and enter incidents at all, the bot will tweet: "No break and enter incidents have been detected by the SFPD this week. Tweet for updates later."

ANOTHER IDEA, depending on what works best:

# Pitch B
Every time someone tweets at my Twitter bot, called @B&ETrendsWatchSF, they will receive a tweet comparing the last week's break and enter incidents with the last week's number of incidents, as a basic monitoring system on the week-to-week trends of this occuing problem. 

#Steps
1. Bot checks Twitter API endpoint of statuses/mentions_timeline
2. Bot navigates to the SFPD data site.  
3. Bot searches for the number of 'Break and Enter' incidents under the 'Crime Type' column of the data table and extracts the number of these incidents. 
4. The bot will calculate the difference between the number of break and enter incidents in the 14 day period (call it X) and the number of break and enter incidents in the last 7 day period (call it Y). Essentially, X - Y = Z, and Z - Y = A, or the change in number of incidents from one week to the next. (That was complicated, but I think it works.)
5. If A is a positive number, the bot will then tweet a response that says the following: "There were (insert number, without the positive sign) more break and enter incidents this week than there were last week. Report all suspicious activity to the SFPD (insert SFPD website URL)."
6. If A is a negative number, the bot will tweet a response that says the following: "There were (insert number, without the negative sign) fewer break and enter incidents this week than there were last week. Report all suspicious activity to the SFPD (insert SFPD website URL)." 

