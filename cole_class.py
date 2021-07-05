#Main Class file
#2021 - Angelo Poggi

import praw
from common/config.py username,password,secret,agent,client,subreddit
import random
import re
import time

class Cole:
    '''Reddit Comment Bot'''
    def __init__(self,instance,speak,subreddit,file,match,quote):
        self.start = instance
        self.speak = speak
        self.subreddit = subreddit
        self.file = file
        self.match = match
        self.quote = quote


    def bot_login(self):
        '''Login method'''
        try:
            self.start = praw.Reddit(username = username,
                                     password = password,
                                     client_id = client,
                                     client_secret = secret,
                                     user_agent = agent)
        except Exception:
            raise('could not log in!')
        return self.start

    def quote_generator(self):
        '''Random Quote generator'''
        quotes = []
        with open(self.file, 'r') as quoteFile:
            for line in quoteFile:
                quotes.append(line)
            random_quote = random.choice(quotes)
            self.quote = random_quote
            return self.quote

    def post(self):
        '''Post method'''
        with open('comments_replied_to.txt', 'a+') as comment_file:
            comment_file.seek(0)
            comment_list = comment_file.read()
            comment_list = comment_list.split('\n')
        reddit_instance = self.start
        space = reddit_instance.subreddit(self.subreddit)
        comments = space.stream.comments()
        for comment in comments:
            if re.search(self.match, comment.body, re.IGNORECASE) and comment.id not in commment_list:
                comment.reply(f'{self.message}')
                comment_list.append(comment.id)
                comment_file.write(f'{comment.id}\n')
                time.sleep(300)








