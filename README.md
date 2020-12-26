# twitter-webhook-discord
A simple daemon script that forwards Tweets from one or multiple users to one or multiple Discord Webhooks.

## Setup



### What you'll need

- Python Installation, version >= 3.6

- Repository requirements. Install via cmd/terminal: `python -m pip install -r requirements.txt`

- Twitter Developer Account [Here](https://developer.twitter.com/en).

- Twitter API Credentials. Make a set of API keys if you haven't already.

- User/s to follow.

### Config File (config.json)

- Update the config file with your Twitter Auth Credentials. (consumer, consumer_s, token, token_s)

- Depending on whether or not you want only the intended author/s Tweets or all Tweets including intended author/s you can set. (bool_only_author)

- Add the screen name/s of the author/s that you want to follow to the array. (usernames_to_watch)

- Add the url/s of your Discord Webhook/s to the last array. (webhook_urls) 

#### Editing The Config.json (Example):

```json

{
    // Your Twitter API Credentials
    "consumer": "TWITTER_CONSUMER_KEY",
    "consumer_s":"TWITTER_CONSUMER_KEY_SECRET",
    "token": "TWITTER_TOKEN",
    "token_s": "TWITTER_TOKEN_SECRET",
    
    // true = only push Tweets that are by the intended author.
    // false = push ALL replies, retweets etc that include the intended author.
    "bool_only_author": true,
    
    // Array of our screen names to push to the webhook.
    "usernames_to_watch": [
        "joerogan",
        "neiltyson"
        ],
    
    // Array of Webhooks to push Tweets to.
    "webhook_urls": [
        "https://discord.com/api/webhooks/792164415010263085/Y0NKBZjh2wFZFoAS0VWhsoK0hMUfn_GM7Z8hPiIOYAyhldbCKM24mZbmd1D44Y4egJYf",
        "https://discord.com/api/webhooks/792164415010263085/Y0NKBZjh2wFZFoAS0VWhsoK0hMUfn_GM7Z8hPiIOYAyhldbCKM26mZbmf1D44Y4egJYa"
    ]
}
```

## Run 

- Simply double-click or run the file __webhook.py__.

- Correct Output:
    ```
    [joerogan] -> Successfully added joerogan to feed!
    [neiltyson] -> Successfully added neiltyson to feed!
    ```

- Tweets will be pushed to the Webhook as they are seen by the listenser.

- Enjoy!



