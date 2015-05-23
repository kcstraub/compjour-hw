from random import random

def find_first_nearme_mention(mentions):
    """
    Given the list of tweets from the mentions-API-endpoint, find the earliest tweet that has the 
    @B&ETrendsWatchSF mention with the #nearme

    Arguments:
        mentions (list): a list of the Twitter tweet objects that are dictionaries

    Returns:
        if any such tweet is found, then return that tweet (dict)
        else, return None

    """
    bmentions = []
    for m in mentions:
        hastags = m['entities']['hastags']
        for tag in hashtags:
            if tag['text'] == "nearme":
                bmentions.append(m)


    if len(bmentions) > 0:
        return bmentions[0]
    else:
        return None

def latest_nearme_reply(tweets):
    """
    Given a list of tweets (ostensibly from user_timeline API endpoint),
    find the earliest one that has the #nearme
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    for tweet in tweets:
        tags = [tag for tag in tweet['entities']['hashtags'] if tag['text'].upper() == 'nearme']
        if len(tags) > 0:
            return tweet

def near_me_pull():
    """
    Pull up the last burglary incident in the tweeters area, assuming that we have the 
    actual geotag lat/lng data from which to pull. I need to take the geotagged lat/lng and 
    compare that to the lat/lng list in the dataSF database, for only the crimes that were burglaries.

    Arguments (list): 
        burglary_location (list): a list of dataSF burglaries lat/lng location data, which are shown in X and Y
        columns

    Returns:
        if the crime is a burglary,
            then return all information that row (list)
                if an X (lat) number value has the first 6 matching decimal points with the geotag we found in the tweet, then 
                return the information the data SFrow for that Address, Date and Description of the burglary incident (list of dict)
                elseif a Y (lng) number value has the first 5 matching decimal points with the geotag we found in the tweet, then
                return the information in the dataSF row that Address, Date, and Description (list of dict)
                else return None

    """

    def most_recent_near_me():
        """
        Take any list of dictionaries that may have arisen from the near_me_pull function, and take the one with 
        the most recent date. 

        Arguments (list):
            the near_me_pull lists

        Returns: 
        The first dict when sorted for date, meaning the most recently dated burglary that matched the geotag we described.

        """ 


    def make_update_text():
        """
        Create a custom message for the tweeter with the particular location.
        Arguments:
            The dict that were returned from the most_recent_near_me function. 

        Return:
            With that text string with that information expressed in the form of a sentence. 
        """


