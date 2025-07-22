
from typing import Any
import logging 

from enum import Enum

#@dataclass
class OptionDescriptor:
    name:str|None = None
    description:str|None = None
    active:bool = False
    info:bool = False
    download:bool = False
    debug:bool = False
    info_required:bool = False
    download_required:bool = False
    debug_required:bool = False
    allowed_values:list[str] = []
    download_value:Any|None = None
    info_value:Any|None = None
    debug_value:Any|None = None
    def __init__(self,  
                name:str|None=None,
                description:str|None = None,
                active:bool = False,
                info:bool = False,
                download:bool = False,
                debug:bool = False,
                info_required:bool = False,
                download_required:bool = False,
                debug_required:bool = False,
                allowed_values:list[str] = [],
                download_value:Any|None = None,
                info_value:Any|None = None,
                debug_value:Any|None = None,
                ) -> None:
        self.name:str|None = name
        self.description:str|None = description
        self.active:bool = active
        self.info:bool = info
        self.download:bool = download
        self.debug:bool = debug
        self.info_required:bool = info_required
        self.download_required:bool = download_required
        self.debug_required:bool = debug_required
        self.allowed_values:list[str] = allowed_values
        self.download_value:Any|None = download_value
        self.info_value:Any|None = info_value
        self.debug_value:Any|None = debug_value


                
username=OptionDescriptor()
password=OptionDescriptor()          
videopassword=OptionDescriptor()     
usenetrc=OptionDescriptor()          
netrc_location=OptionDescriptor()    
netrc_cmd=OptionDescriptor()         
verbose=OptionDescriptor(active=True,debug=True)           
quiet=OptionDescriptor(active=True,info=True,download=True)             
no_warnings=OptionDescriptor(active=True)       
forceprint=OptionDescriptor(active=True,info=True)
print_to_file=OptionDescriptor(active=True,info=True,debug=True)     
forcejson=OptionDescriptor(active=True)         
dump_single_json=OptionDescriptor(active=True)  
force_write_download_archive=OptionDescriptor(active=True,info=True,download=True)
simulate=OptionDescriptor(active=True)          
format=OptionDescriptor(active=True,download_required=True)            
allow_unplayable_formats=OptionDescriptor()
ignore_no_formats_error=OptionDescriptor()
format_sort=OptionDescriptor()
format_sort_force=OptionDescriptor()
prefer_free_formats=OptionDescriptor()
allow_multiple_video_streams=OptionDescriptor() 
allow_multiple_audio_streams=OptionDescriptor()
check_formats =OptionDescriptor(active=True,download=True)    
paths=OptionDescriptor(active=True,info=True,download=True,allowed_values=['home','temp','chapter','subtitle','thumbnail','description','annotation','infojson','link','pl_video','pl_thumbnail','pl_description','pl_infojson' ])
outtmpl=OptionDescriptor(active=True,download=True,allowed_values=['default','chapter','subtitle','thumbnail','description','annotation','infojson','link','pl_video','pl_thumbnail','pl_description','pl_infojson' ])           
outtmpl_na_placeholder=OptionDescriptor()
restrictfilenames=OptionDescriptor(active=True,info=True,debug=True,download=True) 
trim_file_name=OptionDescriptor()    
windowsfilenames=OptionDescriptor()  
ignoreerrors=OptionDescriptor(active=True,download_required=True)                             
skip_playlist_after_errors=OptionDescriptor(active=True) 
allowed_extractors=OptionDescriptor()
overwrites=OptionDescriptor(active=True)        
playlist_items=OptionDescriptor(active=True)    
playlistrandom=OptionDescriptor(active=True)    
lazy_playlist=OptionDescriptor(active=True)     
matchtitle=OptionDescriptor(active=True)        
rejecttitle=OptionDescriptor(active=True)       
logger=OptionDescriptor(active=True)            
logtostderr=OptionDescriptor(active=True)       
consoletitle=OptionDescriptor(active=True)      
writedescription=OptionDescriptor(active=True)  
writeinfojson=OptionDescriptor(active=True)     
clean_infojson=OptionDescriptor(active=True)    
getcomments=OptionDescriptor()       
writeannotations=OptionDescriptor()  
writethumbnail=OptionDescriptor()    
allow_playlist_files=OptionDescriptor(active=True) 
write_all_thumbnails=OptionDescriptor() 
writelink=OptionDescriptor(active=True)         
writeurllink=OptionDescriptor(active=True)      
writewebloclink=OptionDescriptor(active=True)   
writedesktoplink=OptionDescriptor(active=True)  
writesubtitles=OptionDescriptor(active=True)    
writeautomaticsub=OptionDescriptor(active=True) 
listsubtitles=OptionDescriptor(active=True)     
subtitlesformat=OptionDescriptor()   
subtitleslangs=OptionDescriptor(active=True,download=True)    
keepvideo=OptionDescriptor(active=True)         
daterange=OptionDescriptor(active=True)         
skip_download=OptionDescriptor(active=True,info_required=True,download_required=True)     
cachedir=OptionDescriptor(active=True)          
noplaylist=OptionDescriptor(active=True,download=True,info=True)        
age_limit=OptionDescriptor(active=True)         
min_views=OptionDescriptor(active=True)         
max_views=OptionDescriptor(active=True)         
download_archive=OptionDescriptor(active=True,download_required=True)  
break_on_existing=OptionDescriptor(active=True,info=True,debug=True,download=True) 
break_per_url=OptionDescriptor(active=True,info=True,debug=True,download=True)     
cookiefile=OptionDescriptor(active=True)        
cookiesfrombrowser=OptionDescriptor(active=True)
legacyserverconnect=OptionDescriptor(active=True)
nocheckcertificate=OptionDescriptor(active=True)         
client_certificate=OptionDescriptor(active=True)         
client_certificate_key=OptionDescriptor(active=True)         
client_certificate_password=OptionDescriptor(active=True)         
prefer_insecure=OptionDescriptor(active=True)         
enable_file_urls=OptionDescriptor(active=True)         
http_headers=OptionDescriptor(active=True)         
proxy=OptionDescriptor(active=True)         
geo_verification_proxy=OptionDescriptor(active=True)         
socket_timeout=OptionDescriptor(active=True)         
bidi_workaround=OptionDescriptor()         
debug_printtraffic=OptionDescriptor()         
default_search=OptionDescriptor(active=True)         
encoding=OptionDescriptor(active=True)         
extract_flat=OptionDescriptor(active=True,info_required=True)         
wait_for_video=OptionDescriptor(active=True)    
postprocessors=OptionDescriptor(active=True)    
progress_hooks=OptionDescriptor(active=True)    
postprocessor_hooks=OptionDescriptor()
merge_output_format=OptionDescriptor(active=True)
final_ext=OptionDescriptor(active=True)        
fixup=OptionDescriptor(active=True,allowed_values=['never','warn','detect_or_warn'])            
source_address=OptionDescriptor(active=True)   
impersonate=OptionDescriptor(active=True)      
sleep_interval_requests=OptionDescriptor(active=True,download_required=True)
sleep_interval=OptionDescriptor(active=True,download_required=True)    
max_sleep_interval=OptionDescriptor(active=True,download_required=True)
sleep_interval_subtitles=OptionDescriptor(active=True,download_required=True) 
match_filter=OptionDescriptor(active=True,download=True)      
color=OptionDescriptor()             
progress_template=OptionDescriptor(active=True,allowed_values=['download', 'postprocess','download-title','postprocess-title']) 
force_keyframes_at_cuts=OptionDescriptor(active=True,info=True,debug=True,download=True) 
noprogress=OptionDescriptor(active=True,info=True,download=True)        
ffmpeg_location=OptionDescriptor(active=True,info=True,debug=True,download=True)   
concurrent_fragment_downloads=OptionDescriptor(active=True,info=True)
embedsubtitles=OptionDescriptor(active=True,download=True)
remuxvideo=OptionDescriptor(active=True,download_required=True)
xattrs=OptionDescriptor(active=True,download=True)    

all_options:dict[str,OptionDescriptor] = {
    name: obj for name, obj in globals().items()
    if isinstance(obj, OptionDescriptor)
}

for option_name, option_instance in all_options.items():
    option_instance.name = option_name if None else option_instance.name



SLEEP_SUBTITLES:str ='1'
SLEEP_INTERVAL: str = '10'
SLEEP_REQUESTS: str = '1'
MAX_SLEEP_INTERVAL: str = '20'
VIDEO_DIR: str = '/mnt/AllVideo/0082-youtube'
ARCHIVE_DIR: str = f'{VIDEO_DIR}/archive'
LOGS_DIR: str = f'{ARCHIVE_DIR}/logs'
BASE_DOWNLOAD_LIST : str = '/home/mbeware/Documents/dev/fyoutube'
SUBSCRIPTIONS_FILE: str = f'{BASE_DOWNLOAD_LIST}/subscriptions.list'
LASTDOWNLOADEDCHANNEL_FILE:str = f'{BASE_DOWNLOAD_LIST}/lastdownloadedchannel.info'




### How to read a value : 
## aaa = sleep_interval.info_value if (sleep_interval.info_value is not None and sleep_interval.active and (sleep_interval.info_required or sleep_interval.info)) else None
### Info
concurrent_fragment_downloads.info_value = 4
force_write_download_archive.info_value = True
skip_download.info_value = True
noplaylist.info_value=False
forceprint.info_value='%(id)s'
extract_flat.info_value='in_playlist'
noprogress.info_value=False
quiet.info_value=True
### Download 
sleep_interval_subtitles.download_value = 1
sleep_interval.download_value = 10
sleep_interval_requests.download_value = 1
max_sleep_interval.download_value = 20
force_write_download_archive.download_value = True
skip_download.download_value = False
subtitleslangs.download_value= 'all,-live_chat'
embedsubtitles.download_value=True
noplaylist.download_value=False
remuxvideo.download_value='mkv'
noprogress.download_value=False
xattrs.download_value=True
match_filter.download_value= "live_status!~=?'post_live|is_live|is_upcoming'&availability~=?'unlisted|public'"
ignoreerrors.download_value='only_download'
check_formats.download_value= 'selected'
quiet.download_value=True
paths.download_value={'home':VIDEO_DIR,
                      'temp':'tmp',
                      'subtitle':'subs',
                      'pl_video':VIDEO_DIR,
                      }
outtmpl.download_value={'default':'[%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s'}
download_archive.download_value="************************"





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

global messagelog
global channel_info_log_handler
global channel_debug_log_handler
global messagelog_formatter 

channel_info_log_handler:logging.Handler|None=None
channel_debug_log_handler:logging.Handler|None=None

messagelog_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

messagelog = logging.getLogger("fyoutube")
messagelog.setLevel(logging.DEBUG)

general_handler = logging.FileHandler(f"{LOGS_DIR}/fyoutube.info.log")
general_handler.setLevel(logging.INFO)
general_handler.setFormatter(messagelog_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(messagelog_formatter)

messagelog.addHandler(general_handler)
messagelog.addHandler(console_handler)


def log_channel(channel_name:str):
    global messagelog
    global channel_info_log_handler
    global channel_debug_log_handler
    if channel_info_log_handler:
        messagelog.removeHandler(channel_info_log_handler)
        channel_info_log_handler=None
    if channel_debug_log_handler:
        messagelog.removeHandler(channel_debug_log_handler)
        channel_debug_log_handler=None
    
    channel_info_log_handler = logging.FileHandler(f"{LOGS_DIR}/{channel_name}_info.log")
    channel_debug_log_handler = logging.FileHandler(f"{LOGS_DIR}/{channel_name}_debug.log")
    channel_info_log_handler.setLevel(logging.INFO)
    channel_info_log_handler.setFormatter(messagelog_formatter)
    channel_debug_log_handler.setLevel(logging.DEBUG)
    channel_debug_log_handler.setFormatter(messagelog_formatter)
    messagelog.addHandler(channel_info_log_handler)
    messagelog.addHandler(channel_debug_log_handler)

class Request_type(Enum):
    DOWNLOAD_ALL_CHANNEL = 'DOWNLOAD_CHANNEL'
    DOWNLOAD_ALL_LIST = 'DOWNLOAD_LIST'
    LIST_VIDEO_CHANNEL = 'LIST_VIDEO_CHANNEL'
    LIST_VIDEO_PLAYLIST ='LIST_VIDEO_PLAYLIST'
    LIST_VIDEO_RSS ='LIST_VIDEO_RSS'
    LIST_RSS_CHANNEL ='LIST_RSS_CHANNEL'
    LIST_RSS_PLAYLIST ='LIST_RSS_PLAYLIST'
    


def build_options(request_type:Request_type|None)->dict[str,Any]:
    selected_options:dict[str,Any]={}

    for option_name,option in all_options.items():
        if (option.download_value is not None and option.active and (option.download_required or option.download)):
            selected_options[option_name]=option.download_value
            messagelog.debug(f'{option_name=}-{option.download_value=}-{type(option.download_value)=}')
    return selected_options
    

def get_channel_name(channel_url:str)->str:
    sep=None
    if '@' in channel_url:
        sep = '@'
    elif '?' in channel_url:
        sep = '?'
    cname = channel_url.split(sep)[1] if sep else channel_url
    return cname


