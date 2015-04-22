## Pitch
In the face of a shortage of police, the number of burglary incidents has been rising in San Jose -- along
with the community's concern. Every time someone tweets at my Twitter bot, called @B&EWatchSJ, with the hashtag #showme, they will receive a string of tweets to their timeline detailing the time and location of each B&E incident in San Jose over the 7 days. 

(Potential adds: if someone would like to change the date range of the incidents to two weeks or a month from the current day, they need only include the phrase 'two weeks' or 'one month' in the tweet to make this change. Additionally, if they'd like to download the incident information in an excel spreadsheet format to their computer, they can include the hashtag #download)
 
## Steps
1. Bot checks Twitter API endpoint of statuses/mentions_timeline
2. For each Tweet, the bot will see if the #showme hashtag was used, and read for the user's screen name and the ID of the tag.
3. 
