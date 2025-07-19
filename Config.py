
SLEEP_SUBTITLES: str = '1'
SLEEP_INTERVAL: str = '10'
SLEEP_REQUESTS: str = '1'
MAX_SLEEP_INTERVAL: str = '20'
VIDEO_DIR: str = '/mnt/AllVideo/0082-youtube'
ARCHIVE_DIR: str = '/mnt/AllVideo/0082-youtube/archive'
SUBSCRIPTIONS_FILE: str = '/home/mbeware/Documents/dev/fyoutube/subscriptions.md'

i_PIRATEMESSAGE = "\033[1m\033[93m\033[41mUsing this tool means that the video creators are not getting paid for their work, so please consider supporting them directly.\033[0m"
i_EPILOG:str ="This is a tool using yt-dlp to download videos from YouTube and store them locally to watch them offline, without ads, and without relying on YouTube's servers."
i_EPILOG += "\n" + i_PIRATEMESSAGE



i_BASENAME = 'fyoutube'
i_VERSIONS: dict[str, str] = {
 # Version   :   ModuleName without the .py extension
    'dev'   :  f'{i_BASENAME}_main',
    'V0.9'    :   f'{i_BASENAME}_V09',
    'Current':   f'{i_BASENAME}_V09',     
        }

def run_config():
    print("Running GUI configuration dialog...")

def run_install():
    print("Running installation process...")

def run_status():
    print("Checking installation status...")