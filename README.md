Welcome to my Spotify Playlist Creator program!

Before running this program a few things will need to be completed.

1. First you will need to sign into this website "https://developer.spotify.com/" and then create an app.
2. 
   All you need to fill out are the App Name, App Description, and Redirect URL fields.
   
   Nothing specific needed here, just fill out whatever you want to call the app, for the redirect you can makup a url such as "https://example.com/".
   
   Once completed it will take you back to your dashboard and you should see your new app, click on it and at the top under basic information is the keys you will need.

4. In your terminal you will need to set 3 environmental variables
   
   $Env:OATH_CLIENT_ID = "In your spotify app copy the Client ID info here"
   
   $Env:OATH_CLIENT_KEY = "In your spotify app copy the Client Secret info here"
   
   $Env:OATH_REDIRECT_URL = "Copy whatever you entered for your redirect URL here"

Now you can run the main.py, it will prompt for a date in a YYYY-MM-DD format

Once entered it will print out each song from that day and add it to the playlist if the song is on Spotify

Enjoy!
