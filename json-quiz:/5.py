import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)
print('A.', data['created_at'])
print('B', data['user']['created_at'])
print('C.', data['text'])
print('D.', data['user']['screen_name'])
print('E.', data['id'])
print('F.', data['entities']['user_mentions'])
print('G.', data['entities']['hashtags'][0]['text'],',',data['entities']['hashtags'][1]['text'])
hashtag_objs = data['entities']['hashtags']
hashtag_texts = []
for h in hashtag_objs:
	hashtag_texts.append(h['text'])
print('G.', ','.join(hashtag_texts))
display_objs = data['entities']['urls']
display_texts = []
for d in display_objs:
	display_texts.append(d['display_url'])
print('H.', ','.join(display_texts))
