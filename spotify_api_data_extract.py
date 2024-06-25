#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    client_id=os.environ.get('client_id')
    client_secret=os.environ.get('client_secret')
    client_credentials_manager = SpotifyClientCredentials(client_id="f9ece6168dc34bf8a855b6d9cbd9fe50", client_secret="517fb92932f548878076b0fb4fcb2e43")
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    playlist_URI = playlist_link.split("/")[-1].split('?')[0]
    spotify_data=sp.playlist_tracks(playlist_URI)
    
    client=boto3.client('s3')
    
    filename="spotify_raw_"+datetime.now().strftime("%Y%m%d%H%M%S%f")+".json"
    
    client.put_object(
        Bucket="spotify-etl-project-poojitha",
        Key="raw_data/to_be_processed/"+filename,
        Body=json.dumps(spotify_data)
        )