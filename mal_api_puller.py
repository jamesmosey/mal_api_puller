import time
import requests
import pandas as pd

anime_data = []
# URL can be changed as per API documentation.
url = 'https://api.myanimelist.net/v2/anime/ranking'
headers = {
    'X-MAL-CLIENT-ID': '<YOUR_CLIENT_ID>' # Your ClientID goes here.
}

# Set fields you wish to pull, can be found on MAL API Documentation.
fields = 'id,rank,title,mean,genres,studios,popularity,media_type,rating,num_episodes,start_season,start_date,status'
limit = 100  # Max limit per request.
total = 2000  # Total anime to fetch, can be increased or lowered.

for offset in range(0, total, limit):
    params = {
        'ranking_type': 'all',
        'limit': limit,
        'offset': offset,
        'fields': fields
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Request failed at offset {offset}: {response.status_code}")
        break

    batch = response.json().get('data', [])
    anime_data.extend(item['node'] for item in batch)

    time.sleep(1.1)  # Delay requests to avoid hitting rate limits.
    
# Final dataframe containing Anime data from the API request, may need cleaning.
anime_df = pd.json_normalize(anime_data)