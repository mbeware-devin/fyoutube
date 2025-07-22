import os
import sys
import subprocess
import time
import Config
from datetime import datetime
from pathlib import Path


def InfoFromPlaylist(url:str, downloaded_video_archive_file:str):    
    cname = Config.get_channel_name(url)
    print(f"New channel: {cname}" )
    cmd = [
            'yt-dlp',
            '--concurrent-fragments','4', # This might still be useful for processing multiple playlists/channels
            '--force-write-archive',
            '--skip-download', 
            '-P','/mnt/AllVideo/0082-youtube',
            '-P','temp:tmp',
            '--download-archive',downloaded_video_archive_file,
            '--yes-playlist',
#            '-O','%(id)s', # Output only the video ID
            '--flat-playlist', 
            '--progress',
            '-q',
            url,
    ]       
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False) # Keep capture_output=False if you want to see yt-dlp's progress
        if result.returncode == 0:
            print("Info retrieval completed successfully.")
        Path(downloaded_video_archive_file).touch() # just in case there were no video on that channel
        return result.returncode
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during Info: {e}")
        print("Make sure yt-dlp is installed and the playlist URL is valid.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)

def moreinfo(url:str):
    cname = Config.get_channel_name(url)
    print(f"Getting more info: {cname}" )
    moreinfofile = f'{Config.LOGS_DIR}/archive_{cname}_moreinfo_debug.txt'
          
    cmd2 = [
    'yt-dlp',
    '--skip-download', 
    '-P','/mnt/AllVideo/0082-youtube',
    '-P','temp:tmp',
    '--yes-playlist',
    #'-O','%(id)s', # Output only the video ID
    '--flat-playlist', 
    '--progress',
    '--ignore-errors',
    '--print-to-file', '[%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s]', moreinfofile,        
    url,
    ]       
    subprocess.run(cmd2, check=True, capture_output=False) # Keep capture_output=False if you want to see yt-dlp's progress


def download_playlist(url:str):    
    cname = Config.get_channel_name(url)
    downloaded_video_archive_file = f'{Config.ARCHIVE_DIR}/archive_{cname}.list'
    if not os.path.exists(downloaded_video_archive_file): #New channel - Don't download all old videos
        return InfoFromPlaylist(url,downloaded_video_archive_file)
        

    print(f"{datetime.now().strftime('%H:%M:%S')} - Processing channel: {cname}" )
    moreinfofile = f'{Config.LOGS_DIR}/archive_{cname}_debug.log'
    cmd:list[str] = [
            'yt-dlp',
            '--sleep-subtitles',Config.SLEEP_SUBTITLES,
            '--sleep-interval',Config.SLEEP_INTERVAL,
            '--sleep-requests',Config.SLEEP_REQUESTS,
            '--max-sleep-interval',Config.MAX_SLEEP_INTERVAL,
#            '--concurrent-fragments','4',
            '--force-write-archive',
#            '--skip-download',  # Skip downloading videos
            '-P',Config.VIDEO_DIR,
            '-P','temp:tmp',
            '-P','subtitle:subs',
            '-o','[%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s',            
             '--download-archive',downloaded_video_archive_file,
            '-f','bestvideo+bestaudio/best',
            '--sub-langs','all,-live_chat',
            '--embed-subs',
            '--yes-playlist',
            '--remux-video', 'mkv',            
            '--progress',
            '--xattrs',    
            '--match-filters', "live_status!~=?'post_live|is_live|is_upcoming'",     
            '--no-abort-on-error',
            '--check-formats',
            '--no-abort-on-error',
            '--restrict-filenames', 
            '--print-to-file', '['+datetime.now().strftime('%Y-%m-%d% %H:%M:%S')+']-[%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s]', moreinfofile,        
            '-q',
            '--verbose',
            url,
    ]
    
    try:
        with open(f"{Config.LOGS_DIR}/archive_{cname}_stderr.log", 'w') as error_file:
            r=subprocess.run(cmd, check=True, stdout=None, text=True, stderr=error_file )
            return r.returncode



    except subprocess.CalledProcessError:
        print(f"Error occurred during download for [{cname}] ")
#        moreinfo(url)
        return 22
  

    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)
    
    

def is_next_channel(url:str,last_url:str)-> bool:
    cname = Config.get_channel_name(url)         
    lasturlcname = Config.get_channel_name(last_url)             
    if last_url == url:
        print(f'found {cname}! - downloading will start with next channel')
        return True
    
    print(f'Looking for {lasturlcname} - skipping {cname} for now')
    return False

def save_lastchannel(url:str):
    with open(Config.LASTDOWNLOADEDCHANNEL_FILE, 'w') as lastdownloadedchannel:
        lastdownloadedchannel.write(url)

def get_lastchannel()->str:
    with open(Config.LASTDOWNLOADEDCHANNEL_FILE, 'r+') as lastdownloadedchannel:
        return lastdownloadedchannel.readline()    

def get_videos():
    last_url = get_lastchannel()
    while True:
        urls = []
        with open(Config.SUBSCRIPTIONS_FILE, 'r') as f:
            urls = f.readlines()    
        print(f"{datetime.now().strftime('%H:%M:%S')} - Here we go for an other round...")
        for url in urls:  
            url = url.strip()
            if url and is_next_channel(url,last_url) if last_url else True: 
                if last_url:
                    last_url=None 
                else:                
                    if download_playlist(url) == 0:
                        save_lastchannel(url)
                
        print("Waiting for a bit...")
        time.sleep(600)  # Sleep for a while before checking again