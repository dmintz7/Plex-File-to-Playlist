import os, csv, config
from plexapi.server import PlexServer
from datetime import datetime

files_to_add = []
with open(config.file) as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		if len(row) > 0: files_to_add.append(row[0])

plex = PlexServer(config.plex_host, config.plex_api)
all = []
for section in plex.library.sections():
	if section.TYPE in ('movie'):
		all = all + section.search()
	if section.TYPE in ('show'):
		all = all + section.searchEpisodes()
keep =[]
for item in all:
		for media in item.media:
			for part in media.parts:
				if part.file in files_to_add:
					keep.append((part.file, item))

if len(keep) > 0:
	play_lst = []
	for x in files_to_add:
		for file, item in keep:
			if item.lastViewedAt is None:
				lastViewed = datetime.strptime("1900-01-01", '%Y-%m-%d')
			else:
				lastViewed = item.lastViewedAt
			
			try:
				if lastViewed < datetime.strptime(config.start_date, '%Y-%m-%d'):
					if file == x:
						play_lst.append(item)
			except ValueError:
				play_lst.append(item)
			except:
				pass
				
	for playlist in plex.playlists():
		if playlist.title == config.playlist_name:
			try:
				playlist.delete()
			except:
				pass
				
	plex.createPlaylist(config.playlist_name, play_lst)
else:
	print("No Videos Found, Playlist Not Created")
