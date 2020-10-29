import twitch, twitter, sys
import auth

client = twitch.TwitchClient(auth.twitch_client_id)
channel = client.channels.get_by_id(auth.channel_id)
status = channel.status

""" channel members:
mature
status
broadcaster_language
broadcaster_software
display_name
game
language
id
name
created_at
updated_at
partner
logo
video_banner
profile_banner
profile_banner_background_color
url
views
followers
broadcaster_type
description
private_video
privacy_options_enabled
"""

api = twitter.Api(consumer_key=auth.twitter_api_key, consumer_secret=auth.twitter_secret_key,
                  access_token_key=auth.twitter_access_token, access_token_secret=auth.twitter_access_secret)

prefix = 'Streaming: '
postfix = '\nhttps://twitch.tv/onelivesleft'

overshoot = len(prefix) + len(postfix) + len(status) - 140
if overshoot > 0:
    status = status[:-(overshoot + 3)] + '...'

try:
    api.PostUpdate(prefix + status + postfix)
except Exception as e:
    print(e)
    sys.exit(1)
