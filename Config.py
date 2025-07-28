
from typing import Any
import logging 
from enum import Enum


import tomli
import tomli_w
from platformdirs import user_config_path
import platformdirs


class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for thekey, thevalue in self.items():
            if isinstance(thevalue, dict):
                self[thekey] = DotDict(thevalue)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(key) from e

    def __setattr__(self, key, value):
        self[key] = value

    def to_dict(self):
        result = {}
        for thekey, thevalue in self.items():
            if isinstance(thevalue, DotDict):
                result[thekey] = thevalue.to_dict()
            else:
                result[thekey] = thevalue
        return result


class UserConfig:
    def __init__(
        self,
        app_name="fyoutube",
        org_name="mbeware",
        filename="baseconfig.toml",
        default_config=None,
    ):
        self.config_path = user_config_path(app_name, org_name) / filename
        self.default_config = default_config or {"Config": {"Empty":"True"},}
        self._ensure_config_file()
        self.data = self._load()

    def _ensure_config_file(self):
        if not self.config_path.exists():
            print(f"Creating default config at: {self.config_path}")
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with self.config_path.open("wb") as f:
                tomli_w.dump(self.default_config, f)

    def _load(self):
        with self.config_path.open("rb") as f:
            return DotDict(tomli.load(f))

    def save(self):
        """Write current config back to the file."""
        with self.config_path.open("wb") as f:
            tomli_w.dump(self.data.to_dict(), f)

    def reload(self):
        """Reload the config from file."""
        self.data = self._load()

    def __getattr__(self, name):
        return getattr(self.data, name)

    def _resolve(self,value):
        t={}
        lv = value
        while "%-" in lv:
            tplv1=lv.partition("%-")
            tplv2=tplv1[2].partition("-%")
            p1=tplv1[0]
            kw=tplv2[0]
            p2=tplv2[2]
            print(p1,kw,p2)
            lv2=f'{p1}{t[kw]}{p2}'
            print(lv2)
            lv=lv2
        return lv

Config_app_name="fyoutube"
Config_org_name="mbeware"
Config_filename="baseconfig.toml"

#     SelectedFeatures={'KeepDownloadedVideoList':True,'DownloadVideo':True,'AddSubtitles':True,'FilterSponsor':True,'ShowProgress':True, 'stdouttofile':False, "stderrortofile":True, 'verboseToFile': True}

# from dataclasses import dataclass
# @dataclass
# class ParameterConfig:
#     Optional:bool=False
#     DefaultValue:Any|None=None
#     Configurable:bool=True
# @dataclass
# class ParameterValue:
#     current:Any
#     previous:Any
#     changed:bool
#     valid:bool

# @dataclass
# class FeatureParameter:
#     parameter:str
#     config:ParameterConfig
#     value:ParameterValue


# @dataclass
# class FeatureParameterList:
#     feature:str
#     parameters:list[FeatureParameter]
    
#     ParametersValues={}
#     FeatureParameterValues={}
#     AllFeatureParameterValues={}
# 'KeepDownloadedVideoList':{'ParamName':{Optional:False,DefaultValue:3,Configurable:True}','DownloadVideo':True,'AddSubtitles':True,'FilterSponsor':True,'ShowProgress':True, 'stdouttofile':False, "stderrortofile":True, 'verboseToFile': True}


BaseConfig={        
            "Paths": {
                "VIDEO_DIR": f"{platformdirs.user_downloads_path()}", #/mnt/AllVideo/0082-youtube",
                "ARCHIVE_DIR": '%Paths.VIDEO_DIR%/archive',
                "LOGS_DIR": '%Paths.ARCHIVE_DIR%/logs',
                "BASE_DOWNLOAD_LIST" : f'{platformdirs.user_data_path(Config_app_name,Config_org_name)}', #/home/mbeware/Documents/dev/fyoutube',
                "SUBSCRIPTIONS_FILE": '%BASE_DOWNLOAD_LIST%/subscriptions.list',
                "LASTDOWNLOADEDCHANNEL_FILE" : '%BASE_DOWNLOAD_LIST%/lastdownloadedchannel.info',
                
            },
            "Sleep": {
                "SUBTITLES":"1",
                "INTERVAL":"2",
                "REQUESTS":"1",
                "MAX_INTERVAL":"20",
            }
        }
 


USER = UserConfig(app_name="fyoutube",org_name="mbeware",filename="baseconfig.toml",default_config=BaseConfig)




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
GLOBAL_CONFIGDIR:str = str(platformdirs.user_data_path(Config_app_name,Config_org_name) )




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


def buildtemplate(nuggetlist:list, bannednuggetlist:list=[], separator:str|None=None,prefix:str|None=None,postfix:str|None=None):
    template = ""
    for nugget in nuggetlist:
        if nugget not in bannednuggetlist:
            if prefix:
                template += prefix
            template += f'%({nugget})s'    
            if postfix:
                template += postfix
            if separator:
                template += separator
    return template


available_elements = [
'id',
'title',
'fulltitle',
'ext',
'alt_title',
'description',
'display_id',
'uploader',
'uploader_id',
'uploader_url',
'license',
'creators',
'creator',
'timestamp',
'upload_date',
'release_timestamp',
'release_date',
'release_year',
'modified_timestamp',
'modified_date',
'channel',
'channel_id',
'channel_url',
'channel_follower_count',
'channel_is_verified',
'location',
'duration',
'duration_string',
'view_count',
'concurrent_view_count',
'like_count',
'dislike_count',
'repost_count',
'average_rating',
'comment_count',
'age_limit',
'live_status',
'is_live',
'was_live',
'playable_in_embed',
'availability',
'media_type',
'start_time',
'end_time',
'extractor',
'extractor_key',
'epoch',
'autonumber',
'video_autonumber',
'n_entries',
'playlist_id',
'playlist_title',
'playlist',
'playlist_count',
'playlist_index',
'playlist_autonumber',
'playlist_uploader',
'playlist_uploader_id',
'playlist_channel',
'playlist_channel_id',
'playlist_webpage_url',
'webpage_url',
'webpage_url_basename',
'webpage_url_domain',
'original_url',
'categories',
'tags',
'cast',
'urls',
'filename',
'formats_table',
'thumbnails_table',
'subtitles_table',
'automatic_captions_table',
]