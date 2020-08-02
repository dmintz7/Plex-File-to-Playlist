# Plex-File-to-Playlist

Convert text file to Plex playlist 

To Use:
* Create Text file with the full path of each episode/movie.
	* The file path needs to be the same path that is visiable to the Plex instance.
* Copy config.py.sample to config.py and populate plex_api, plex_host, playlist_name and file. start_date is optional.
	* start_date will dictate if an episode/movie should no longer be added if watched after start_date. This allows the script to be cron and run daily to remove and watched episodes/movies
