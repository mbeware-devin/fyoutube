import time
import Config
from Config import log_channel

from fyoutube_yt_dlp import download_all_video_from_channel
from Config import messagelog

def is_next_channel(url:str,last_url:str)-> bool:
    cname = url.split('@')[1]             
    lasturlcname = last_url.split('@')[1]             
    if last_url == url:
        messagelog.info(f'found {cname}! - downloading will start with next channel')
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
        messagelog.info("Here we go for an other round...")
        for url in urls:  
            url = url.strip()
            cname = url.split('@')[1] 
            log_channel(cname)
            if url and is_next_channel(url,last_url) if last_url else True: 
                if last_url:
                    last_url=None 
                else:                
                    if download_all_video_from_channel(url,Config.VIDEO_DIR,f'{Config.ARCHIVE_DIR}/archive_{cname}.list') == 0:
                        save_lastchannel(url)
                
        messagelog.info("Waiting for a bit...")
        time.sleep(600)  # Sleep for a while before checking again



    