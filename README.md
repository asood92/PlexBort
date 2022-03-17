# Plexbot
A discord bot to monitor and query your Plex server.

#### Installation
[Docker Link](https://hub.docker.com/repository/docker/rem3dy/plexbot)  
Pull the image.
Create your environment variables file as follows.
```
BASE_URL=YourPlexWebURL // ex. https://app.plex.tv/desktop/#!/ or https://yourdomain.com/plex
PLEX_API_TOKEN=YourPlexWebToken // Find this by navigating to any individual file on your Plex Web, 3 dot menu -> Get Info -> View XML -> It will be in the address bar as the value afte rthe = in ?X-Plex-Token=
DISCORD_API_TOKEN=YourDiscordBotToken // Find this on the Discord Developer Portal for your created bot
```

`docker run --env-file ./.env rem3dy/plexbot .`
#### Features
-   Query for new releases

#### Planned
-   Continuously monitor for new releases and send a message for new uploads.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
