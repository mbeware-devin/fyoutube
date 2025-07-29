# yt-dlp Parameter Documentation

This document catalogs all yt-dlp parameters used across the fyoutube codebase. Parameters are listed with their values, where multiple values on the same line indicate the parameter name followed by its values.

## fyoutube_V09.py

### InfoFromPlaylist() Function
```
yt-dlp
--concurrent-fragments: 4
--force-write-archive
--skip-download
-P: /mnt/AllVideo/0082-youtube
-P: temp:tmp
--download-archive: downloaded_video_archive_file
--yes-playlist
--flat-playlist
--progress
-q
url
```

### moreinfo() Function
```
yt-dlp
--skip-download
-P: /mnt/AllVideo/0082-youtube
-P: temp:tmp
--yes-playlist
--flat-playlist
--progress
--ignore-errors
--print-to-file: [%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s], moreinfofile
url
```

### download_playlist() Function (Commented Implementation)
```
yt-dlp
--use-extractors: all
--sleep-subtitles: Config.SLEEP_SUBTITLES
--sleep-interval: Config.SLEEP_INTERVAL
--sleep-requests: Config.SLEEP_REQUESTS
--max-sleep-interval: Config.MAX_SLEEP_INTERVAL
--force-write-archive
-P: Config.VIDEO_DIR
-P: temp:tmp
-P: subtitle:subs
-o: [%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s
--download-archive: downloaded_video_archive_file
-f: bestvideo+bestaudio/best
--yes-playlist
--remux-video: mkv
--progress
--xattrs
--match-filters: live_status!~=?'post_live|is_live|is_upcoming'
--no-abort-on-error
--check-formats
--restrict-filenames
--print-to-file: [timestamp]-[%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s], moreinfofile
--force-keyframes-at-cuts
--sponsorblock-remove: sponsor,selfpromo
-q
--verbose
url
```

## fyoutube_yt_dlp.py

### InfoFromPlaylist() Function
```
yt-dlp
--concurrent-fragments: 4
--force-write-archive
--skip-download
-P: /mnt/AllVideo/0082-youtube
-P: temp:tmp
--download-archive: downloaded_video_archive_file
--yes-playlist
--flat-playlist
--progress
-q
url
```

### moreinfo() Function
```
yt-dlp
--skip-download
-P: /mnt/AllVideo/0082-youtube
-P: temp:tmp
--yes-playlist
--flat-playlist
--progress
--ignore-errors
--print-to-file: [%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s], moreinfofile
url
```

### download_all_video_from_channel() Function (yt-dlp Library Call)
Uses `Config.build_options(Request_type.DOWNLOAD_ALL_CHANNEL)` to generate parameters dynamically from OptionDescriptor instances.

**Key OptionDescriptor Values Used**:
- sleep_interval_subtitles.download_value: 1
- sleep_interval.download_value: 10
- sleep_interval_requests.download_value: 1
- max_sleep_interval.download_value: 20
- force_write_download_archive.download_value: True
- skip_download.download_value: False
- subtitleslangs.download_value: all,-live_chat
- embedsubtitles.download_value: True
- noplaylist.download_value: False
- remuxvideo.download_value: mkv
- noprogress.download_value: False
- xattrs.download_value: True
- match_filter.download_value: live_status!~=?'post_live|is_live|is_upcoming'&availability~=?'unlisted|public'
- ignoreerrors.download_value: only_download
- check_formats.download_value: selected
- quiet.download_value: True
- paths.download_value: {home: VIDEO_DIR, temp: tmp, subtitle: subs, pl_video: VIDEO_DIR}
- outtmpl.download_value: {default: [%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s}
- download_archive.download_value: ************************

## fyoutube_select.py

### InfoFromPlaylist() Function (Full Mode)
```
yt-dlp
--concurrent-fragments: 4
--use-extractors: all
--yes-playlist
--skip-download
--match-filters: live_status!~=?'post_live|is_live|is_upcoming'&availability~=?'unlisted|public'
--dateafter: now-3day
--force-write-archive
--download-archive: MFD_video_archive_file
-P: temp:/tmp/fyoutube/tmp
--quiet
--verbose
--print-to-file: MFD_videoUrlsTemplate, MFD_videoUrls_temp
--print-to-file: DEBUG_videoUrlslistTemplate, DEBUG_videoUrls_temp
url
```

### InfoFromPlaylist() Function (Quick Mode)
```
yt-dlp
--concurrent-fragments: 4
--use-extractors: all
--yes-playlist
--flat-playlist
--skip-download
--force-write-archive
--download-archive: MFD_video_archive_file
-P: temp:/tmp/fyoutube/tmp
--quiet
url
```

## fyoutube_download.py

### download_video() Function
```
yt-dlp
--concurrent-fragments: 4
-P: downloaded_video_folder
-o: %(upload_date)s-%(title)s_[%(id)s].%(ext)s
--format: bestvideo*+bestaudio/best
--remux-video: mkv
--xattrs
--no-check-formats
--no-abort-on-error
--restrict-filenames
--use-extractors: all
--match-filters: live_status!~=?'post_live|is_live|is_upcoming'
--match-filters: availability~=?'unlisted|public'
--dateafter: now-3day
-P: subtitle:/tmp/fyoutube/subs
--sub-langs: all,-live_chat
--embed-subs
--force-keyframes-at-cuts
--sponsorblock-remove: sponsor,selfpromo
--sleep-subtitles: Config.SLEEP_SUBTITLES
--sleep-interval: Config.SLEEP_INTERVAL
--sleep-requests: Config.SLEEP_REQUESTS
--max-sleep-interval: Config.MAX_SLEEP_INTERVAL
--force-write-archive
--download-archive: downloaded_video_archive_file
-P: temp:/tmp/fyoutube/tmp
--progress
--progress-template: download:progresstemplate
--progress-template: postprocess:progresstemplate
--print: stdouttemplate
--no-simulate
--print-to-file: debugtemplate, verboselog
--quiet
--verbose
--cookies-from-browser: brave
url
```

## GetVidInfo.py

### InfoFromPlaylist() Function
```
yt-dlp
--concurrent-fragments: 4
--force-write-archive
--skip-download
-P: /mnt/AllVideo/0082-youtube
-P: temp:tmp
--download-archive: /mnt/AllVideo/0082-youtube/archive_{cname}.md
--yes-playlist
--flat-playlist
--progress
-q
url
```

## Parameter Categories

### Core Download Parameters
- `yt-dlp`: Base command
- `url`: Target URL (always last parameter)

### Performance Parameters
- `--concurrent-fragments`: 4 (consistent across all implementations)
- `--use-extractors`: all (used in most implementations)

### Archive Management
- `--force-write-archive`: Ensure archive file is updated
- `--download-archive`: Path to archive file (prevents re-downloads)

### Output Control
- `-P`: Path specifications (home, temp, subtitle directories)
- `-o`: Output filename template
- `--remux-video`: mkv (container format)

### Download Behavior
- `--skip-download`: Info extraction only
- `--yes-playlist`: Process entire playlists/channels
- `--flat-playlist`: Extract IDs without metadata (faster)
- `--no-simulate`: Actually download (when not skipping)

### Filtering Parameters
- `--match-filters`: Live status and availability filtering
- `--dateafter`: Time-based filtering (e.g., now-3day)

### Sleep/Rate Limiting
- `--sleep-subtitles`: Delay between subtitle downloads
- `--sleep-interval`: General delay between downloads
- `--sleep-requests`: Delay between requests
- `--max-sleep-interval`: Maximum delay

### Subtitle Handling
- `--sub-langs`: all,-live_chat (all languages except live chat)
- `--embed-subs`: Embed subtitles in video files

### Quality/Format
- `--format` / `-f`: Video quality selection
- `--check-formats` / `--no-check-formats`: Format validation

### Post-Processing
- `--sponsorblock-remove`: sponsor,selfpromo (remove sponsor segments)
- `--force-keyframes-at-cuts`: Ensure clean cuts
- `--xattrs`: Extended file attributes

### Output/Logging
- `--progress`: Show download progress
- `--progress-template`: Custom progress display
- `--print`: Output specific information
- `--print-to-file`: Write information to files
- `--quiet` / `-q`: Suppress output
- `--verbose`: Detailed output

### Error Handling
- `--ignore-errors`: Continue on errors
- `--no-abort-on-error`: Don't stop on errors
- `--restrict-filenames`: Safe filename characters

### Authentication/Network
- `--cookies-from-browser`: brave (use browser cookies)

## Template Formats Used

### Filename Templates
- `[%(upload_date)s]-[%(uploader)s]_[%(title)s].%(ext)s`
- `%(upload_date)s-%(title)s_[%(id)s].%(ext)s`

### Info Templates
- `[%(id)s]-[%(title)s]-[release date : %(release_date)s]-[live_status:%(live_status)s]-[is_live:%(is_live)s]-[was_live:%(was_live)s]-[url:%(webpage_url)s]-[%(original_url)s]`

### Progress Templates
- Built using `Config.buildtemplate()` with fields like `info.title`, `progress.elapsed`, `progress.eta`, `progress.speed`
