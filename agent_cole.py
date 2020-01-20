##################
#Agent Cole Reddit Bot
#
#
#By: Angelo Poggi
#angelo@poggi.work
##################

import praw
import config
import quote_generator
import time
import re




################
#Login to reddit as authorized
#
#
################
def bot_login():
    bot_login = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'Gordon Cole Bot v.01'
                )
    print('Logged in!')
    return bot_login


def bot_action(instance):
    #I Am opening the file that contains all of the Comment ID's the bot has seen/interescted with.
    #comment_tuple = []
    with open('comments_replied_to', 'a+') as comments_file:
        #For some reason, it was positioning the cursor at the END of file
        comments_file.seek(0)
        comment_list = comments_file.read()
        comment_list = comment_list.split('\n')
        #comment_tuple.append(comment_list)
        print(comment_list)


        #Tapping into the subreddit
        space = instance.subreddit('test')
        #checking the stream in the subreddit
        comments = space.stream.comments()
        #bring in the empty tuple and write all the comment ID to it.


        #check comment stream and reply with a gordon quote
        #for the comments in the subreddit stream, read the comment body and save it to text
        #Also checking the author and saving it to a variable if we want to use it later
        for comment in comments:
            message = quote_generator.cole_quote()


            #within the iteration of the comment stream, if the comment contains the kewords, AND the comment ID is not
            #in the tuple, Reply with a random quote
            if re.search('gordon cole', comment.body, re.IGNORECASE) and comment.id not in comment_list:
                print('Found Comment, Replying!')
                print(comment.body)

                comment.reply(f'{message}\n\n\n\n\n\n\nBeep Boop, I am a bot.')
                # #I need to add the comment in the tuple again, as thats what im checking in the stream
                # #I am only reading the file in the begining
                comment_list.append(comment.id)
                comments_file.write(comment.id)
                comments_file.write('\n')
                #I also save that comment ID in the file, for future refernce
                #wait a bit before next iteration.
                time.sleep(540)

#Create Instance of bot
reddit_instance = bot_login()

#Run this always; Bot checks comment stream
#Stream handles the loop
bot_action(reddit_instance)








