import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="Colombia_Spelling_Bot: v1.1.0 (by u/SadLas)",
    username="colombia_spell_bot",
    password="",
)

# Dictionary that contains the key-value pairs as follows: <targetWord,replyToUser>
targetWordAndReplyDict = {
    "columbia": "*Bleep-Bloop-Bleep* I am the Colombia_Spell_Bot. Are you refering to the country in South America? If so, here's a friendly reminder that it is spelled 'Colombia' :)"
}

# reddit.subreddit("all of these subreddits will be searched")
def reply_if_targetword_in_comment(dict, key):
    for comment in reddit.subreddit(
        "asklatinamerica+colombia+languagelearning"
    ).stream.comments(skip_existing=True):
        # Converts comments to lower case
        getUserComment = comment.body.lower()
        # Retrieves the name of the commentor(i.e. username)
        author = comment.author.name
        subredditOfComment = comment.subreddit

        if getUserComment.find(key) != -1:
            comment.reply(dict[key])
            # Print the username and the subreddit they posted the comment in
            print("Username: u/" + author + " Subreddit: r/" + str(subredditOfComment))


# Calling the function
reply_if_targetword_in_comment(targetWordAndReplyDict, "columbia")
