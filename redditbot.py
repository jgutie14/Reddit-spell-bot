import praw
import time

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

targetWord = "columbia"

botReply = "*Bleep-Bloop-Bleep* I am the Colombia_Spell_Bot. Are you refering to the country in South America? If so, here's a friendly reminder that it is spelled 'Colombia' :)"

#reddit.subreddit("all of these subreddits will be serarched")
for comment in reddit.subreddit("asklatinamerica+colombia+languagelearning").stream.comments(skip_existing=True):

    getUserComment = comment.body.lower()  # Converts comments to lower case
    # Retrieves the name of the commentor(i.e. username)
    author = comment.author.name
    subredditOfComment = comment.subreddit

    if (getUserComment.find(targetWord) != -1):
        comment.reply(botReply)
        print('Username: u/' + author +
              " Subreddit: r/" + str(subredditOfComment))
