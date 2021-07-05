#Reddit Bot Commenter - Main Project File
#2021 - Angelo Poggi

from cole_class import Cole

if __name__ == '__main__':
    #Specify your quote file
    Cole.file = 'quotes.txt'
    #Specity what text you want to match
    Cole.match('gordon cole')
    #Start the bot
    redditbot = Cole.start()
    #make the bot talk!
    redditbot.

