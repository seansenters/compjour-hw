Pitch:  From people’s tweets, we can create a map of where in the world it is currently raining; especially where people are displeased by the rain.

Steps:

1.	Bot checks Twitter API endpoint of statuses/mentions_timeline
2.	For each Tweet, the bot checks to see if the hashtag #rainraingoaway was used.
3.	In each Tweet, we also want to get the location (hopefully through geolocation).  If there is no geolocation, we could potentially use if people say where they are in the Tweet or picture of the weather forecast from their phone (more common than one might think).
4.	Use Google Maps geocoding API to get lat/lng coordinates.
5.	Export this data into a list.
6.	Using a map template, plot these data points onto a world map.
