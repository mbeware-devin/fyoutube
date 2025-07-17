#!/usr/bin/env python3
"""
YouTube Playlist Downloader using yt-dlp
Downloads all videos from a playlist with subtitles, chapters, and custom naming.
"""

# https://www.youtube.com/feeds/videos.xml?channel_id=UCxkM67T_Iele-mRVUiBkRqg -o /mnt/AllVideo/0082-youtube

import sys
import datetime
import subprocess
import argparse
from pathlib import Path

#def download_playlist(playlist_url, output_dir="."):
def download_playlist():    
    """
    Download all videos from a YouTube playlist using yt-dlp.
    
    Args:
        playlist_url (str): URL of the YouTube playlist
        output_dir (str): Directory to save downloaded videos
    """
    
    # Create output directory if it doesn't exist
    #Path(output_dir).mkdir(parents=True, exist_ok=True)
    # yt-dlp command with all specified options
    cmd = [
            'yt-dlp',
            '--sleep-subtitles','10',
            '--sleep-interval','20',
            '--sleep-requests','2',
            '--max-sleep-interval','60',
#             '-t','sleep',
            '--concurrent-fragments','4',
            '--force-write-archive',
            '--skip-download',  # Skip downloading videos
            '-P','/mnt/AllVideo/0082-youtube',
            '-P','"temp:tmp"',
#            '-P','"subtitle:subs"',
#            '-o','%(upload_date)s-%(uploader)s-%(title)s_[%(id)s].%(ext)s',
            '--download-archive','/mnt/AllVideo/0082-youtube/archive.md',
#            '-f',"'bestvideo+bestaudio/best'",
#            '--sub-langs','all,-live_chat',
#            '--embed-subs',
            '--yes-playlist',
#            '--format', 'best[ext=mp4]/best',
#            '--remux-video', 'mkv',            
            '--batch-file','/home/mbeware/Documents/dev/fyoutube/subscriptions.md',
#            '--sponsorblock-remove','all',
            '--progress',
#            '--xattrs',
#            '-q',

    ]
    
    try:
        print("Starting download")
        print("-" * 50)
        fullcmdstr = ' '.join(cmd)
        print(f"Executing command: {fullcmdstr}")
        # Execute the command
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"result : {result.stdout.decode() if result.stdout else ''}")
        print("-" * 50)
        print("Download completed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during download: {e}")
        print("Make sure yt-dlp is installed and the playlist URL is valid.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it first:")
        print("pip install yt-dlp")
        sys.exit(1)

def main():
#    parser = argparse.ArgumentParser(
#        description="Download YouTube playlist with yt-dlp",
#        formatter_class=argparse.RawDescriptionHelpFormatter,
#        epilog="""
#Examples:
#  python script.py "https://www.youtube.com/playlist?list=PLxxxxxxx"
#        """
#)
    
 #   parser.add_argument(
 #       'playlist_url',
 #       help='YouTube playlist URL'
#    )
    
 #   args = parser.parse_args()
    
 #   # Validate URL
 #   if not args.playlist_url.startswith(('http://', 'https://')):
 #       print("Error: Please provide a valid YouTube playlist URL")
 #       sys.exit(1)
 #   op = "/mnt/AllVideo/0082-youtube"
    download_playlist()

if __name__ == "__main__":
    main()