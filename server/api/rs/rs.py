from endpoints.watson import watson
from endpoints.twitter import twitter
import pandas as pd
import math


# RS.py

def random_rs(feature_data, num_songs):
    # Lets create a user playlist of random songs 
    playlist_tracks = []
    
    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability', 'energy', 'valence'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
    
    count1 = 0
    while count1 < num_songs:
        temp_song = all_tracks.at[0, 'id']
        if temp_song not in playlist_tracks:
            playlist_tracks.append(temp_song)
            all_tracks.drop(0)
            all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
            count1 += 1
        else: 
            all_tracks = all_tracks.sample(frac=1).reset_index(drop=True) 
    
    return playlist_tracks

def joy_rs(feature_data, num_songs):
    # Mini Playlist
    # Lets create a user playlist of joyful songs
    playlist_tracks = []

    # Lets keep the playlist size range between 25-50 
    tot_songs = num_songs
    if tot_songs > 50:
        tot_songs = 50

    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability', 'energy', 'valence'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)

    # joy_tracks
    joy_tracks = df.copy()
    joy_tracks = joy_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    joy_tracks = joy_tracks[joy_tracks['energy'] > 0.5]
    joy_tracks = joy_tracks[joy_tracks['valence'] > 0.5]
    joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True)

    count1 = 0
    while count1 < tot_songs:
        if joy_tracks.size > 0:
            temp_song = joy_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                joy_tracks.drop(0)
                joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else: 
                joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True)
        else:
            # Pull random tracks from all_tracks
            temp_song = all_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                all_tracks.drop(0)
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else:
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
    
    return playlist_tracks

def anger_rs(feature_data, num_songs):
    # Mini Playlist
    # Lets create a user playlist of angry songs
    playlist_tracks = []

    # Lets keep the playlist size range between 25-50 
    tot_songs = num_songs
    if tot_songs > 50:
        tot_songs = 50

    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability', 'energy', 'valence'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)

    # ang_tracks
    ang_tracks = df.copy()
    ang_tracks = ang_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    ang_tracks = ang_tracks[ang_tracks['energy'] > 0.5]
    ang_tracks = ang_tracks[ang_tracks['valence'] < 0.5]
    ang_tracks = ang_tracks.sample(frac=1).reset_index(drop=True)

    count1 = 0
    while count1 < tot_songs:
        if ang_tracks.size > 0:
            temp_song = ang_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                ang_tracks.drop(0)
                ang_tracks = ang_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else: 
                ang_tracks = ang_tracks.sample(frac=1).reset_index(drop=True)
        else:
            # Pull random tracks from all_tracks
            temp_song = all_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                all_tracks.drop(0)
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else:
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
    
    return playlist_tracks

def sad_rs(feature_data, num_songs):
    # Mini Playlist
    # Lets create a user playlist of sad songs
    playlist_tracks = []

    # Lets keep the playlist size range between 25-50 
    tot_songs = num_songs
    if tot_songs > 50:
        tot_songs = 50

    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability', 'energy', 'valence'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)

    # sad_tracks
    sad_tracks = df.copy()
    sad_tracks = sad_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    sad_tracks = sad_tracks[sad_tracks['energy'] < 0.5]
    sad_tracks = sad_tracks[sad_tracks['valence'] < 0.5]
    sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)

    count1 = 0
    while count1 < tot_songs:
        if sad_tracks.size > 0:
            temp_song = sad_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                sad_tracks.drop(0)
                sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else: 
                sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)
        else:
            # Pull random tracks from all_tracks
            temp_song = all_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                all_tracks.drop(0)
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else:
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
    
    return playlist_tracks

def calm_rs(feature_data, num_songs):
    # Mini Playlist
    # Lets create a user playlist of calm songs
    playlist_tracks = []

    # Lets keep the playlist size range between 25-50 
    tot_songs = num_songs
    if tot_songs > 50:
        tot_songs = 50

    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability', 'energy', 'valence'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)

    # calm_tracks
    calm_tracks = df.copy()
    calm_tracks = calm_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    calm_tracks = calm_tracks[calm_tracks['energy'] < 0.5]
    calm_tracks = calm_tracks[calm_tracks['valence'] > 0.5]
    calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)

    count1 = 0
    while count1 < tot_songs:
        if calm_tracks.size > 0:
            temp_song = calm_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                calm_tracks.drop(0)
                calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else: 
                calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)
        else:
            # Pull random tracks from all_tracks
            temp_song = all_tracks.at[0, 'id']
            if temp_song not in playlist_tracks:
                playlist_tracks.append(temp_song)
                all_tracks.drop(0)
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
                count1 += 1
            else:
                all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
    
    return playlist_tracks

def playlist_rs(feature_data, tones, per_song, num_songs):
    # list of track ids to be added to a playlist at the end of the algorithm
    playlist_tracks = []  

    # using pandas dataframe to manipulate songs
    df = pd.DataFrame.from_dict(feature_data)

    # all_tracks
    all_tracks = df.copy() 
    all_tracks = all_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)       

    # joy_tracks
    joy_tracks = df.copy()
    joy_tracks = joy_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    joy_tracks = joy_tracks[joy_tracks['energy'] > 0.5]
    joy_tracks = joy_tracks[joy_tracks['valence'] > 0.5]
    # shuffle joy_tracks
    joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True)

    # anger_tracks
    anger_tracks = df.copy()
    anger_tracks = anger_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    anger_tracks = anger_tracks[anger_tracks['energy'] > 0.5]
    anger_tracks = anger_tracks[anger_tracks['valence'] < 0.5]
    # shuffle anger_tracks
    anger_tracks = anger_tracks.sample(frac=1).reset_index(drop=True)

    # sad_tracks
    sad_tracks = df.copy()
    sad_tracks = sad_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    sad_tracks = sad_tracks[sad_tracks['energy'] < 0.5]
    sad_tracks = sad_tracks[sad_tracks['valence'] < 0.5]
    # shuffle sad_tracks
    sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)
    
    # calm_tracks
    calm_tracks = df.copy()
    calm_tracks = calm_tracks.drop(['speechiness','instrumentalness','liveness','acousticness','name','artist','loudness','tempo','danceability'], axis=1)
    calm_tracks = calm_tracks[calm_tracks['energy'] < 0.5]
    calm_tracks = calm_tracks[calm_tracks['valence'] > 0.5]
    # shuffle calm_tracks
    calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)

    # check what tones have been calculated
    tone_scores = [0, 0, 0, 0]
    songs_per_tone = [0, 0, 0, 0]
                # joy[0],anger[1],sadness[2],calm[3]

    # fill tone_scores
    if 'joy' in tones.keys():
        tone_scores[0] = tones['joy']
    if 'anger' in tones.keys():
        tone_scores[1] = tones['anger']
    if 'sadness' in tones.keys():
        tone_scores[2] = tones['sadness']
    if 'calm' in tones.keys():
        tone_scores[3] = tones['calm']

    # fill tone_songs
    if 'joy' in per_song.keys():
        songs_per_tone[0] = per_song['joy']
    if 'anger' in per_song.keys():
        songs_per_tone[1] = per_song['anger']
    if 'sadness' in per_song.keys():
        songs_per_tone[2] = per_song['sadness']
    if 'calm' in per_song.keys():
        songs_per_tone[3] = per_song['calm']

    # loop, only decrementing the counter when a song is added to playlist__tracks list of ids
    count1 = 0
    while(count1 < num_songs):
        for i in range(len(tone_scores)):               # repeatedly loop through each song type
            if songs_per_tone[i] == 0:                  # no songs to add of this emotion
                i += 1                                  # skip to next song type in list
            # Joy
            elif songs_per_tone[i] > 0 and i == 0:      # songs_per_tone[0] = 25    aka: there are 25 joy songs left to be added to the final playlist      
                temp_song = joy_tracks.at[0, 'id']      # joy song to be added to playlist
                if temp_song not in playlist_tracks:    # Prevent duplicate tracks
                    playlist_tracks.append(temp_song)
                    songs_per_tone[i] -= 1              # Decrement the song_per_tone value since we added a song to the playlist
                    joy_tracks.drop(0)                  # Remove this track from the dataframe since we have added it
                    joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True) # Shuffle the dataframe
                    count1 += 1
                else: 
                    joy_tracks = joy_tracks.sample(frac=1).reset_index(drop=True) # Well the track was already in the playlist, so lets shuffle the joy_track list
            # Anger
            elif songs_per_tone[i] > 0 and i == 1:
                temp_song = anger_tracks.at[0, 'id']
                if temp_song not in playlist_tracks:
                    playlist_tracks.append(temp_song)
                    songs_per_tone[i] -= 1
                    anger_tracks.drop(0)
                    anger_tracks = anger_tracks.sample(frac=1).reset_index(drop=True)
                    count1 += 1
                else:
                    anger_tracks = anger_tracks.sample(frac=1).reset_index(drop=True)
            # Sad
            elif songs_per_tone[i] > 0 and i == 2:
                temp_song = sad_tracks.at[0, 'id']
                if temp_song not in playlist_tracks:
                    playlist_tracks.append(temp_song)
                    songs_per_tone[i] -= 1
                    sad_tracks.drop(0)
                    sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)
                    count1 += 1
                else:
                    sad_tracks = sad_tracks.sample(frac=1).reset_index(drop=True)
            # Calm 
            elif songs_per_tone[i] > 0 and i == 3:
                temp_song = calm_tracks.at[0, 'id']
                if temp_song not in playlist_tracks:
                    playlist_tracks.append(temp_song)
                    songs_per_tone[i] -= 1
                    calm_tracks.drop(0)
                    calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)
                    count1 += 1
                else:
                    calm_tracks = calm_tracks.sample(frac=1).reset_index(drop=True)
            # Empty List
            elif (songs_per_tone[0] == 0) and (songs_per_tone[1] == 0) and (songs_per_tone[2] == 0) and (songs_per_tone[3] == 0):
                temp_song = all_tracks.at[0, 'id']
                if temp_song not in playlist_tracks:
                    playlist_tracks.append(temp_song)
                    # songs_per_tone[i] -= 1
                    all_tracks.drop(0)
                    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)
                    count1 += 1
                else:
                    all_tracks = all_tracks.sample(frac=1).reset_index(drop=True)

    return playlist_tracks

    
    
def get_tones(username: str) -> dict:
    """generate list of sentiments corresponding to user's tweets"""
    tweet_data = twitter.get_all_tweets(username) # returns a list of users most recent 200 tweets, includes retweets
    empty_dict = {}
    if len(tweet_data) == 0:    # an empty list of tweets was gathered, the twitter account doesnt have any tweets.
        return empty_dict
    sentiment_data = watson.get_sentiment(tweet_data) # returns a dictionary of sentiment analysis objects from watson
    print("LENGTH")
    print(len(sentiment_data))
    sentiment_data = watson.format_sentiment(sentiment_data) # returns a dictionary of ONLY the document tones, COULD BE EMPTY
    if len(sentiment_data) == 0:    # If the dictionary is empty lets just return an empty dictionary
        return empty_dict
    sentiment_data = watson.sort_tones(sentiment_data)
    return sentiment_data


def adjust_songs(tone_in: dict, nums: int) -> dict:
    # Returns a new dictionary containing the amount of songs of each tone to produce in the playlist
    temp_calm = 0
    temp_joy = 0
    temp_anger = 0
    temp_sad = 0
    length = len(tone_in)
    song_num = nums

    # Check if tone_in is an empty dictionary
    if length == 0:
        empty_dict = {}
        return empty_dict
        # return an empty dictionary in case length of tone_in is 0

    # Otherwise continue to check which tones are in the dictionary 
    count = 0 
    div = 0 
    if 'joy' in tone_in.keys():   # count each tone found
        temp_joy = tone_in['joy'] # set = to temporary values to manipulate tone scores
        count = count + 1         # increment count because we found a tone
    if 'anger' in tone_in.keys():
        temp_anger = tone_in['anger']
        count = count + 1
    if 'sadness' in tone_in.keys():
        temp_sad = tone_in['sadness']
        count = count + 1
    if 'calm' in tone_in.keys():
        temp_calm = tone_in['calm']
        count = count + 1

    if count > 0:           
        div = 1 / count # if there are multiple tones we need the ratio of div = (1/# of tones)
    else: 
        div = 1 # otherwise div = 1
    
    sum1 = 0
    list_vals = [0, 0, 0, 0]
    # joy, anger, sad, calm,  order matters!
    
    # getsum1
    if temp_joy > 0:                    # if the temp value has been set
        temp_joy *= song_num            # multiply the score by the number of total songs in end playlist
        temp_joy *= div                 # multiply by div ratio
        temp_joy = math.floor(temp_joy) # get floor of this float
        list_vals[0] = temp_joy         # set the joy value in list to the new temp_joy value calculated
        sum1 += temp_joy                # keep track of the sum1 variable, tracking if we have met the total number of songs in final playlist
    if temp_anger > 0:
        temp_anger *= song_num
        temp_anger *= div
        temp_anger = math.floor(temp_anger)
        list_vals[1] = temp_anger
        sum1 += temp_anger
    if temp_sad > 0:
        temp_sad *= song_num
        temp_sad *= div
        temp_sad = math.floor(temp_sad)
        list_vals[2] = temp_sad
        sum1 += temp_sad
    if temp_calm > 0:
        temp_calm *= song_num
        temp_calm *= div
        temp_calm = math.floor(temp_calm)
        list_vals[3] = temp_calm
        sum1 += temp_calm
        
    # (MOST LIKELY COMPARISON SCENARIO) 
    # sum1 < song_num
    if sum1 < song_num:                     # if the sum1 calculated above is less than the desired song_num 
        while sum1 < song_num:              # loop to increment only calculated (tones > 0)
            for i in range(len(list_vals)):
                if list_vals[i] == 0:       # if the value in the list is 0 then we don't want to add an extra song of this type to the final playlist
                    i += 1                  # increment our loop
                else:
                    list_vals[i] = list_vals[i] + 1     # if the value in list_vals[i] isn't 0 then we should increment
                    sum1 += 1
    # This else if scenario is unlikely to execute, but it is here in case of this scenario.
    elif sum1 > song_num: 
        if list_vals[0] == 0 and list_vals[1] == 0 and list_vals[2] == 0 and list_vals[3] == 0:
            # if every value in this list is somehow 0, then lets just return an empty dictionary
            empty_dict = {}
            return empty_dict
        else:
            # sum1 > song_num
            while sum1 > song_num:
                for i in range(len(list_vals)):
                    if list_vals[i] == 0:
                        i += 1
                    elif list_vals[i] > 1:
                        list_vals[i] = list_vals[i] - 1 # decrement the values
                        sum1 -= 1
                        # while loop stops execution once sum1 = song_num
     
    # list_val = [number_of_joy_songs, number_of_anger_songs, number_of_sad_songs, number_of_calm_songs]
    ret_dic = tone_in.copy()
    
    # update the output dictionary with new values
    if 'joy' in ret_dic.keys():
        ret_dic['joy'] = list_vals[0]
    if 'anger' in ret_dic.keys():
        ret_dic['anger'] = list_vals[1]
    if 'sadness' in ret_dic.keys():
        ret_dic['sadness'] = list_vals[2]
    if 'calm' in ret_dic.keys():
        ret_dic['calm'] = list_vals[3]
        
    return ret_dic


# function for testing
def show_vals(sad, joy, anger, calm):
    print("Sad: %d" %sad)
    print("Joy: %d" %joy)
    print("Anger: %d" %anger)
    print("Calm: %d" %calm)

