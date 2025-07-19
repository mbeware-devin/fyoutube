import os
import sys
import subprocess
import time
import Config




def InfoFromPlaylist(url:str):    
    cname = url.split('@')[1]
    ### Info ###
    
    Config.paths.info_value={'home':f'{Config.VIDEO_DIR}','temp':'tmp'}
    Config.download_archive.info_value=f'{Config.ARCHIVE_DIR}/archive_{cname}.md'


    print(f"New channel: {cname}" )
    cmd = [
            'yt-dlp',
            '--concurrent-fragments','4', # This might still be useful for processing multiple playlists/channels
            '--force-write-archive',
            '--skip-download', 
            '-P','/mnt/AllVideo/0082-youtube',
            '-P','temp:tmp',
            '--download-archive',f'{Config.ARCHIVE_DIR}/archive_{cname}.md',
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

def moreinfo(url:str):
    cname = url.split('@')[1]
    print(f"Getting more info: {cname}" )
    moreinfofile = f'{Config.ARCHIVE_DIR}/archive_{cname}_debug.txt'
          
    cmd2 = [
    'yt-dlp',
    '--skip-download', 
    '-P','/mnt/AllVideo/0082-youtube',
    '-P','temp:tmp',
    '--yes-playlist',
    '-O','%(id)s', # Output only the video ID
    '--flat-playlist', 
    '--progress',
    '--ignore-errors',
    '--print-to-file', '***********\n%(id)s-%(title)s\n%(description)s\nrelease date : %(release_date)s\nlive_status:%(live_status)s - is_live:%(is_live)s - was_live:%(was_live)s\nurl:%(webpage_url)s-%(original_url)s', moreinfofile,        
    url,
    ]       
    subprocess.run(cmd2, check=True, capture_output=False) # Keep capture_output=False if you want to see yt-dlp's progress


def download_playlist(url:str):    
    cname = url.split('@')[1]
    ### Download ###
    
    Config.paths.info_value={'home':f'{Config.VIDEO_DIR}','temp':'tmp','subtitle':'subs'}
    Config.download_archive.info_value=f'{Config.ARCHIVE_DIR}/archive_{cname}.md'
    


    print(f"Processing channel: {cname}" )
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
             '--download-archive',f'{Config.ARCHIVE_DIR}/archive_{cname}.md',
            '-f','bestvideo+bestaudio/best',
            '--sub-langs','all,-live_chat',
            '--embed-subs',
            '--yes-playlist',
            '--remux-video', 'mkv',            
            '--progress',
            '--xattrs',
            '--match-filters', '!is_live',
            '--no-abort-on-error',
            '--check-formats',
            '-q',
            
            url,
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=False)

    except subprocess.CalledProcessError:
        print(f"Error occurred during download for [{cname}] ")
        moreinfo(url)
  

    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)


def get_videos():
    while True:
        urls = []
        with open(Config.SUBSCRIPTIONS_FILE, 'r') as f:
            urls = f.readlines()    

        for url in urls:  
            url = url.strip()
            if url: # Check if the line is not empty
                cname = url.split('@')[1]             
                archive_file = f'{Config.ARCHIVE_DIR}/archive_{cname}.md'
                if not os.path.exists(archive_file): #Don't download old videos
                    InfoFromPlaylist(url)
                else:
                    download_playlist(url)
        time.sleep(600)  # Sleep for a while before checking again