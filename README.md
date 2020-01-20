# Twin Peaks Reddit Bot

----

This is a simple bot that reads the comment stream in /r/twinpeaks and replies with a random quote

uses PRAW to read the stream

# How it works
----
* logins to reddit using the bot_login function and return this value
* uses the returned value to read the comment stream of /r/twin peaks
* if a comment contains the words "gordon cole" it replies using a random quote form quotes.txt passed through quote_generator

# notes
---
Login credentials are stored in config.py and passed into the main script "agent_cole.py".
This was excluded for privacy reasons, but you can simply create your own using the example below.

`username = ''
password = '''
client_id = '''
client_secret = '`