import requests



url='https://api.cognitive.microsoft.com/bing/v5.0/search'
key1 = 'f7b590dbfa26499da9044a51c5192da0'
key2 = '47a9419d389843379bb02fd1bdaa2870'

subscription_id = '6976e396-9e3c-45e4-87a5-2fdd4754273b'

endpoint = 'https://api.cognitive.microsoft.com/bing/v5.0'

term = ["reverse osmosis", "waste water"]

heade = dict()
heade['Ocp-Apim-Subscription-Key'] = key1

queryURL = url+"?q="+term

print heade
r = requests.get(queryURL, headers=heade)

print r.text