# Slido-Bot
A bot for the audience interaction tool sli.do.
Since Slido blocks malicious access via the API very effectively, this bot was created as a new solution for voting up questions automatically. It works via Firefox or Chrome browser.
## Instalation
```
git clone https://github.com/4rts/slido-bot.git
python -m pip install -r requirements.txt
```
## Syntax
To use the bot, copy 
```
python slidobot.py -h "hash" -x "xpath" -d "driver" - v "amount of votes"
```
and paste it into your terminal. Next, replace
1. "hash" with the text between event/ and /live in the slido-link.
For example, the hash in ```"https://app.sli.do/event/1a2b3c4d5e/live/questions"```
would be ```"1a2b3c4d5e"```.
2. "xpath" with the xpath to the upvote-button of the post. To find out what the xpath looks like, you can use a tool like ChroPath for Firefox or the Chrome developer tools.
3. "driver" with the path to the [chromedriver](https://chromedriver.chromium.org/) or [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) I r.ecommend to use Chrome, because the bot is more performant with it.
4. "amount of votes" with the amount of votes you'd like to add to the question.

Have fun.
