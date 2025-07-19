import sys
import subprocess
import Config

def InfoFromPlaylist(url:str):    
    cname:str = url.split('@')[1]
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


def download_playlist(url:str):    
    cname = url.split('@')[1]
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
            '--match-filters', "live_status!='is_upcoming'" ,
            '--match-filters', "live_status!='not_live'" ,
            '--no-abort-on-error',
            '--check-formats',
#            '--verbose',
            '-q',
            url,

    ]
    
    try:

        subprocess.run(cmd, check=True, capture_output=False)

       
    except subprocess.CalledProcessError:
        print(f"Error occurred during download for [{cname}] but the show must go on!")

    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)

def get_videos():
    print("get_videos main")