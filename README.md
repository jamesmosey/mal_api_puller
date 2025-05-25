
# MyAnimeList API Puller

A short Python script that populates a pandas dataframe with anime data pulled from the MyAnimeList API. This documentation provides a walkthrough on the setup and usage of the script.


## Initial Setup

### Adding a ClientID

Before the script can be used, a ClientID must first be obtained. This can be done by creating an account on the MyAnimeList website, heading to the API section of the account settings and selecting 'Create ID'.

![](https://cdn.discordapp.com/attachments/1334642856534605824/1376168062880845914/image.png?ex=683457e2&is=68330662&hm=78b86e6e04d209a390323b0c3d0d6e79a4c5f8cd2ea9bf4f0596f804a06738e9&)

After the client setup is complete, open the script and navigate to:
```py
headers = {
    'X-MAL-CLIENT-ID': '<YOUR_CLIENT_ID>'
}
```
Replace `'<YOUR_CLIENT_ID>'` with the ClientID you just obtained. Setup is now complete and the script can be ran with the default fields. It will populate a dataframe with 2000 rows of Anime data ready to be cleaned and analysed.
### Changing Fields

As per the [MAL API documentation](https://myanimelist.net/apiconfig/references/api/v2), the fields that can be pulled from the ranking endpoint (api.myanimelist.net/v2/anime/ranking) are:
```http
  GET /anime/ranking
```

| Query Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | ID of an Anime on MyAnimeList |
| `title` | `string` |  |
| `main_picture` | `object or null` |  |
| `alternative_titles` | `object or null` | "synonyms or ISO 639-1" |
| `start_date` | `string or null` |  |
| `end_date` | `string or null` |  |
| `synopsis` | `string or null` | Synopsis |
| `mean` | `float or null` | Mean score. When the `mean` can not be calculated, the result does not include this field. |
| `rank` | `integer or null` | When the `rank` cannot be calculated, the result does not include this field. |
| `popularity` | `integer or null` | MyAnimeList's popularity metric |
| `num_list_users` | `integer` | Number of users who have this work in their list. |
| `num_scoring_users` | `integer` |  |
| `nsfw` | `string or null` | white: Safe for work, gray: May not be safe for work, black: Not safe for work |
| `genres` | `Array of 'Genre' objects` |  |
| `created_at` | `string <date-time>` |  |
| `updated_at` | `string <date-time>` |  |
| `media_type` | `string` | unknown, tv, ova, movie, special, ona, music |
| `status` | `string` | finished_airing, currently_airing, not_yet_aired. |
| `num_episodes` | `integer` | Total number of episodes in the series. If unknown, it is 0. |
| `start_season` | `object or null` | start_season.year, start_season.season |
| `broadcast` | `object or null` | Broadcast date. |
| `rating` | `string or null` |  |
| `id` | `Array of 'AnimeStudio' objects` |  |

Feel free to change the endpoint and fields in the script to pull different data, as per the API documentation.
## Usage/Examples

This script was used to pull the dataset necessary to perform an exploratory data analysis on the 2000 highest-rated Anime. The notebook for this project can be found on Kaggle using the following link: <coming-soon> 


## Author

- [@jamesmosey](https://www.github.com/jamesmosey)


