import praw
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

bot = praw.Reddit(user_agent=config['Config']['user_agent'],
                client_id=config['Config']['client_id'],
                client_secret=config['Config']['client_secret'],
                username=config['Config']['username'],
                password=config['Config']['password'])

subreddit = bot.subreddit('greentext')

comments = subreddit.stream.comments()

for comment in comments:
    body = comment.body # Fetch body
    # print(body)
    if re.match(r'Real: (?P<RealText>.*)\n\nStraight: (?P<StraightText>.*)', body):
        bodyregex = re.match(r'Real: (?P<RealText>.*)\n\nStraight: (?P<StraightText>.*)', body)
        reply = ">be me\n\n"+">fucking this one dude’s wife\n\n"+">lots of slapping and moaning\n\n"+">hear door open\n\n"+">smell distinct mixture of regret, Doritos, and a lack of hygiene\n\n"+">must be the virgin again\n\n"+">he knows we want our privacy, so he goes on the computer in his room\n\n"+">i get bored of looking at the wife’s face while I fuck her, so I open my phone while I continue to pound away\n\n"+">log onto reddit and open r/greentext\n\n"+">read a funny greentext from the 4chan and chuckle as the wife begs for genes that the husband can’t give her\n\n"+">think of a simple way I can relate straightness and truthfulness to the events of the greentext\n\n"+">make the dude’s wife cum again as I begin to type my masterpiece in the comment section\n\n"+">Real: "+bodyregex.group("RealText")+"\n\n"+">Straight: "+bodyregex.group("StraightText")+"\n\n"+">chuckle as I make her orgasm once more and bust inside her, making her moan with ecstasy\n\n"+">it’s been a good day\n\n"+">i wonder what the virgin’s been up to. If he makes a comment that’s funny enough, I might let him eat my cum out of his wife’s pussy"
        print(comment.reply(reply))
        # print("Replied to comment: "+body)