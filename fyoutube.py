#!/usr/bin/env python3
"""
YouTube Playlist Downloader using yt-dlp
Downloads all videos from a playlist with subtitles, chapters, and custom naming.
"""

import sys
import subprocess
import argparse
from pathlib import Path

def download_playlist(playlist_url, output_dir="."):
    """
    Download all videos from a YouTube playlist using yt-dlp.
    
    Args:
        playlist_url (str): URL of the YouTube playlist
        output_dir (str): Directory to save downloaded videos
    """
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # yt-dlp command with all specified options
    cmd = [
        'yt-dlp',
        
        # Download entire playlist
        '--yes-playlist',
        
        # Output format and filename template
        '--output', f'{output_dir}/%(upload_date)s-%(uploader)s-%(title)s.%(ext)s',
        
        # Video format selection (best quality)
        '--format', 'best[ext=mp4]/best',
        
        # Remux to MKV container
        '--remux-video', 'mkv',
        
        # Download subtitles
        '--write-subs',
        '--write-auto-subs',
        '--sub-langs', 'en,en-US,en-GB',
        '--embed-subs',
        
        # Enable chapters (remove --remove-chapters to keep them)
        '--remove-chapters',
        
        # Use 4 threads for downloading
        '--concurrent-fragments', '4',
        
        # Additional options for better quality and reliability
        '--ignore-errors',
        '--no-warnings',
#        '--extract-flat', 
        'never',
        
        # The playlist URL
        playlist_url
    ]
    
    try:
        print(f"Starting download of playlist: {playlist_url}")
        print(f"Output directory: {output_dir}")
        print("Options:")
        print("  - Format: MKV container")
        print("  - Quality: Best available")
        print("  - Subtitles: Enabled (embedded)")
        print("  - Chapters: Removed")
        print("  - Threads: 4")
        print("  - Filename: <upload_date>-<uploader>-<title>.mkv")
        print("-" * 50)
        
        # Execute the command
        result = subprocess.run(cmd, check=True, capture_output=False)
        
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
    parser = argparse.ArgumentParser(
        description="Download YouTube playlist with yt-dlp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py "https://www.youtube.com/playlist?list=PLxxxxxxx"
  python script.py "https://www.youtube.com/playlist?list=PLxxxxxxx" -o downloads/
        """
    )
    
    parser.add_argument(
        'playlist_url',
        help='YouTube playlist URL'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Validate URL
    if not args.playlist_url.startswith(('http://', 'https://')):
        print("Error: Please provide a valid YouTube playlist URL")
        sys.exit(1)
    
    download_playlist(args.playlist_url, args.output)

if __name__ == "__main__":
    main()