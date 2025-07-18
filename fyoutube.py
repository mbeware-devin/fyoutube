#!/usr/bin/env python3

import os
import sys
import subprocess
import time

SLEEP_SUBTITLES = '1'
SLEEP_INTERVAL = '10'
SLEEP_REQUESTS = '1'
MAX_SLEEP_INTERVAL = '20'
VIDEO_DIR = '/mnt/AllVideo/0082-youtube'
ARCHIVE_DIR = '/mnt/AllVideo/0082-youtube/archive'
SUBSCRIPTIONS_FILE = '/home/mbeware/Documents/dev/fyoutube/subscriptions.md'



def InfoFromPlaylist(url):    
    cname = url.split('@')[1]
    print(f"New channel: {cname}" )
    cmd = [
            'yt-dlp',
            '--concurrent-fragments','4', # This might still be useful for processing multiple playlists/channels
            '--force-write-archive',
            '--skip-download', 
            '-P','/mnt/AllVideo/0082-youtube',
            '-P','temp:tmp',
            '--download-archive',f'{ARCHIVE_DIR}/archive_{cname}.md',
            '--yes-playlist',
            '-O','%(id)s', # Output only the video ID
            '--flat-playlist', 
            '--progress',
            '-q',
            url,
    ]       
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False) # Keep capture_output=False if you want to see yt-dlp's progress
        if result.returncode == 0:
            print("Info retrieval completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during Info: {e}")
        print("Make sure yt-dlp is installed and the playlist URL is valid.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)


def download_playlist(url):    
    cname = url.split('@')[1]
    print(f"Processing channel: {cname}" )

    cmd = [
            'yt-dlp',
            '--sleep-subtitles',SLEEP_SUBTITLES,
            '--sleep-interval',SLEEP_INTERVAL,
            '--sleep-requests',SLEEP_REQUESTS,
            '--max-sleep-interval',MAX_SLEEP_INTERVAL,
#            '--concurrent-fragments','4',
            '--force-write-archive',
#            '--skip-download',  # Skip downloading videos
            '-P',VIDEO_DIR,
            '-P','temp:tmp',
            '-P','subtitle:subs',
            '-o','[%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s',
             '--download-archive',f'{ARCHIVE_DIR}/archive_{cname}.md',
            '-f','bestvideo+bestaudio/best',
            '--sub-langs','all,-live_chat',
            '--embed-subs',
            '--yes-playlist',
            '--remux-video', 'mkv',            
            '--progress',
            '--xattrs',
            '--match-filters', '!is_live',
            '--match-filters', "live_status!='is_upcoming'" ,
            '--match-filters', "live_status!='not_live'" ,
            '--no-abort-on-error',
            '--check-formats',
#            '--verbose',
            '-q',
            url,

    ]
    
    try:

        r=subprocess.run(cmd, check=True, capture_output=False)

       
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during download for [{cname}] but the show must go on!")

    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)

def main():
    while True:
        urls = []
        with open(SUBSCRIPTIONS_FILE, 'r') as f:
            urls = f.readlines()    

        for url in urls:  
            url = url.strip()
            if url: # Check if the line is not empty
                cname = url.split('@')[1]             
                archive_file = f'{ARCHIVE_DIR}/archive_{cname}.md'
                if not os.path.exists(archive_file): #Don't download old videos
                    InfoFromPlaylist(url)
                else:
                    download_playlist(url)
        time.sleep(3600)  # Sleep for a while before checking again

if __name__ == "__main__":
    main()



####
# Todo : Split the code in two processe. One will build the list of videos to download and the other will download them.
# Todo : Use yt-dlp python API instead of subprocess
# Todo : Configuration files in OS appropriate locations
# Todo : Metadata files in OS appropriate locations
# Todo : Use a proper logging library instead of print statements
# Todo : Self register in cron / windows task scheduler
# Todo : Language support
# Todo : Set configuration from command line arguments
# Todo : Use a proper package manager for Python
# Todo : Use a proper package manager for Python dependencies     
# Todo : GUI to manage subscriptions and configurations
# Todo : Include Extract channel to get all the subscriptions
# Todo : Hook to run after download is complete
# Todo : Option to use RSS feeds to get new videos
# Todo : Add date last downloaded for each channel and start from the least recent
# Todo : Add messaging to remind the user that the creators are not getting paid for their work
# Todo : Add a way to donate to the creators
# Todo : Create a RSS feed of magnets to share with others with torrent clients
# Todo : Embed a torrent client.
# Todo : Download from the torrent client before downloading from YouTube
# Todo : Offer to the creator to upload the video directly to the torrent rss feed
# Todo : Opt-in telemetrics to see how many people are using the tool and how many videos are downloaded
# Todo : Update the tool through the tool itself/Torrent
