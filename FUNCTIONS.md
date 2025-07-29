# fyoutube Function Documentation

## fyoutube_V09.py - Primary Download Engine

### InfoFromPlaylist(url: str, downloaded_video_archive_file: str)
**Purpose**: Populate archive file with existing video IDs without downloading content (for new channels)

**Files/Folders Used**:
- `/mnt/AllVideo/0082-youtube` - Hard-coded video directory
- `tmp/` - Temporary files directory
- `downloaded_video_archive_file` - Channel-specific archive file

**Config Variables Used**:
- `Config.get_channel_name()` - Extract channel name from URL
- `Config.messagelog` - Logging instance

**Behavior**: Creates archive entries for all videos in a channel/playlist without downloading, preventing bulk historical downloads when adding new channels.

### moreinfo(url: str)
**Purpose**: Extract detailed metadata about channel videos for debugging

**Files/Folders Used**:
- `Config.LOGS_DIR` - Log directory for output files
- `/mnt/AllVideo/0082-youtube` - Hard-coded video directory
- `tmp/` - Temporary files directory

**Config Variables Used**:
- `Config.get_channel_name()` - Extract channel name from URL
- `Config.LOGS_DIR` - Log file directory
- `Config.messagelog` - Logging instance

**Behavior**: Generates detailed video metadata files for debugging and analysis purposes.

### download_playlist(url: str)
**Purpose**: Main download function for processing YouTube channels

**Files/Folders Used**:
- `Config.ARCHIVE_DIR/archive_global.list` - Global archive file
- `Config.GLOBAL_CONFIGDIR/{channel}.config` - Channel configuration files
- `Config.VIDEO_DIR` - Video download directory
- `Config.LOGS_DIR` - Log files directory
- `tmp/` - Temporary files
- `subs/` - Subtitle files

**Config Variables Used**:
- `Config.SLEEP_SUBTITLES` - Sleep interval for subtitle downloads
- `Config.SLEEP_INTERVAL` - General sleep interval between requests
- `Config.SLEEP_REQUESTS` - Sleep between individual requests
- `Config.MAX_SLEEP_INTERVAL` - Maximum sleep interval
- `Config.VIDEO_DIR` - Video output directory
- `Config.ARCHIVE_DIR` - Archive directory
- `Config.LOGS_DIR` - Log directory
- `Config.GLOBAL_CONFIGDIR` - Global configuration directory
- `Config.get_channel_name()` - Channel name extraction
- `Config.messagelog` - Logging instance

**Behavior**: Downloads videos from a channel with comprehensive yt-dlp parameters, handles new channel detection, and manages error logging.

### get_videos()
**Purpose**: Main infinite loop for continuous channel monitoring

**Files/Folders Used**:
- `Config.SUBSCRIPTIONS_FILE` - Channel subscription list
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - Resume state file

**Config Variables Used**:
- `Config.SUBSCRIPTIONS_FILE` - Subscription list file path
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - Last channel state file
- `Config.i_PIRATEMESSAGE` - Ethical warning message
- `Config.messagelog` - Logging instance
- `manage_arguments.g_args.IAmAPirateAndIWillStarveTheCreators` - Piracy acknowledgment flag

**Behavior**: Continuously processes subscription list, handles resume functionality, manages download state, and implements sleep intervals between cycles.

### is_next_channel(url: str, last_url: str) -> bool
**Purpose**: Determine if processing should resume from a specific channel

**Config Variables Used**:
- `Config.get_channel_name()` - Channel name extraction
- `Config.messagelog` - Logging instance

**Behavior**: Compares channel names to implement resume functionality after interruptions.

### save_lastchannel(url: str) / get_lastchannel() -> str
**Purpose**: Persist and retrieve resume state

**Files/Folders Used**:
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - State persistence file

**Config Variables Used**:
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - State file path

**Behavior**: Simple file-based state persistence for resume capability.

## fyoutube_main.py - Alternative Engine

### get_videos()
**Purpose**: Alternative main loop using direct yt-dlp library interface

**Files/Folders Used**:
- `Config.SUBSCRIPTIONS_FILE` - Channel subscription list
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - Resume state file
- `Config.VIDEO_DIR` - Video download directory
- `Config.ARCHIVE_DIR/archive_global.list` - Global archive file

**Config Variables Used**:
- `Config.SUBSCRIPTIONS_FILE` - Subscription list file path
- `Config.LASTDOWNLOADEDCHANNEL_FILE` - Last channel state file
- `Config.VIDEO_DIR` - Video output directory
- `Config.ARCHIVE_DIR` - Archive directory
- `Config.get_channel_name()` - Channel name extraction
- `Config.messagelog` - Logging instance

**Behavior**: Similar to V09 but uses `fyoutube_yt_dlp.download_all_video_from_channel()` instead of subprocess calls.

## fyoutube_select.py - Content Archiving Engine

### InfoFromPlaylist(url: str, cname: str, MFD_video_archive_file: str, verboselog: str|None, stdoutlog: str|None, quick: bool)
**Purpose**: Advanced info extraction with filtering and multiple output formats

**Files/Folders Used**:
- `/tmp/fyoutube/MFD_videoUrls_temp_{cname}.list` - Temporary URL list
- `/tmp/fyoutube/DEBUG_videoUrls_temp_{cname}.list` - Debug output
- `/tmp/fyoutube/tmp` - Temporary working directory
- `MFD_video_archive_file` - Archive file parameter
- `verboselog` - Verbose log file (optional)
- `stdoutlog` - Standard output log file (optional)

**Config Variables Used**:
- `Config.buildtemplate()` - Template building function

**Behavior**: Extracts video information with advanced filtering (3-day window, live status filtering), supports both quick and detailed modes, generates multiple output formats for analysis.

## fyoutube_yt_dlp.py - Direct Library Interface

### download_all_video_from_channel(channel_url: str, video_destination: str, downloaded_video_archive_file: str)
**Purpose**: Download videos using yt-dlp Python library directly

**Files/Folders Used**:
- `video_destination` - Video output directory parameter
- `downloaded_video_archive_file` - Archive file parameter
- `Config.LOGS_DIR` - Log directory

**Config Variables Used**:
- `Config.get_channel_name()` - Channel name extraction
- `Config.build_options()` - Configuration builder
- `Config.Request_type.DOWNLOAD_ALL_CHANNEL` - Request type enum
- `Config.messagelog` - Logging instance

**Behavior**: Uses yt-dlp Python library instead of subprocess, leverages Config.build_options() for parameter generation, provides more programmatic control over download process.

### InfoFromPlaylist(url: str, downloaded_video_archive_file: str)
**Purpose**: Library-based info extraction (similar to V09 version)

**Files/Folders Used**:
- `/mnt/AllVideo/0082-youtube` - Hard-coded video directory
- `tmp/` - Temporary files directory
- `downloaded_video_archive_file` - Archive file parameter

**Config Variables Used**:
- `Config.get_channel_name()` - Channel name extraction
- `Config.messagelog` - Logging instance

**Behavior**: Subprocess-based implementation similar to V09 version.

## fyoutube_download.py - Specialized Download Function

### download_video(url: str, cname: str, downloaded_video_archive_file: str, downloaded_video_folder: str, verboselog: str, stdoutlog: str)
**Purpose**: Specialized video download with advanced features

**Files/Folders Used**:
- `downloaded_video_folder` - Video output directory parameter
- `downloaded_video_archive_file` - Archive file parameter
- `/tmp/fyoutube/subs` - Subtitle directory
- `/tmp/fyoutube/tmp` - Temporary directory
- `verboselog` - Verbose log file parameter
- `stdoutlog` - Standard output log file parameter

**Config Variables Used**:
- `Config.buildtemplate()` - Template building function
- `Config.SLEEP_SUBTITLES` - Subtitle download sleep interval
- `Config.SLEEP_INTERVAL` - General sleep interval
- `Config.SLEEP_REQUESTS` - Request sleep interval
- `Config.MAX_SLEEP_INTERVAL` - Maximum sleep interval

**Behavior**: Advanced download with sponsorblock integration, subtitle embedding, progress templates, cookie support, and comprehensive filtering options.

## Common Patterns

### File/Folder Dependencies
- **Video Storage**: `Config.VIDEO_DIR` or hard-coded `/mnt/AllVideo/0082-youtube`
- **Archive Management**: `Config.ARCHIVE_DIR/archive_global.list` and channel-specific archives
- **Logging**: `Config.LOGS_DIR` for various log files
- **Temporary Files**: `/tmp/fyoutube/tmp` and `/tmp/fyoutube/subs`
- **State Management**: `Config.SUBSCRIPTIONS_FILE` and `Config.LASTDOWNLOADEDCHANNEL_FILE`

### Config Variable Usage
- **Sleep Configuration**: `SLEEP_SUBTITLES`, `SLEEP_INTERVAL`, `SLEEP_REQUESTS`, `MAX_SLEEP_INTERVAL`
- **Path Configuration**: `VIDEO_DIR`, `ARCHIVE_DIR`, `LOGS_DIR`, `SUBSCRIPTIONS_FILE`, `LASTDOWNLOADEDCHANNEL_FILE`
- **Utility Functions**: `get_channel_name()`, `buildtemplate()`, `build_options()`
- **Logging**: `messagelog` for consistent logging across all functions
