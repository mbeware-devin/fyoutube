#!/usr/bin/env python3

import os
import sys
import subprocess
import time
import argparse
import textwrap

from fyoutube_V09 import V09




SLEEP_SUBTITLES = '1'
SLEEP_INTERVAL = '10'
SLEEP_REQUESTS = '1'
MAX_SLEEP_INTERVAL = '20'
VIDEO_DIR = '/mnt/AllVideo/0082-youtube'
ARCHIVE_DIR = '/mnt/AllVideo/0082-youtube/archive'
SUBSCRIPTIONS_FILE = '/home/mbeware/Documents/dev/fyoutube/subscriptions.md'



def VCurrent():
    pass


VERSION = {'V0.9': V09,
           "Current": VCurrent,  # Default version
          }



def run_config():
    print("Executing Config function...")

def run_install():
    print("Executing Install function...")

def run_status():
    print("Executing Status function...")


config = {
    'SLEEP_SUBTITLES': SLEEP_SUBTITLES,
    'SLEEP_INTERVAL': SLEEP_INTERVAL,
    'SLEEP_REQUESTS': SLEEP_REQUESTS,
    'MAX_SLEEP_INTERVAL': MAX_SLEEP_INTERVAL,
    'VIDEO_DIR': VIDEO_DIR,
    'ARCHIVE_DIR': ARCHIVE_DIR,
    'SUBSCRIPTIONS_FILE': SUBSCRIPTIONS_FILE
}



def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="local youtube library",
                                     epilog=
'''
This is a tool using yt-dlp to download videos from YouTube and store them locally to watch them offline, without ads, and without relying on YouTube's servers.\n
''' + PIRATEMESSAGE)

    # Hidden optional arguments
    parser.add_argument(
        "--compatibilitymode",
        choices=list(VERSION.keys()),
        default="Current",
        help=argparse.SUPPRESS
    )
    parser.add_argument("--IAmAPirateAndIWillStarveTheCreators",
        action='store_true',
        default=False,
        help=argparse.SUPPRESS
    )
    parser.add_argument("-V",
        "--version",
        action='store_true',
        default=False
        
    )
    helpconfig = "Set configuration options for fyoutube:\n"
    for key in config.keys():
        helpconfig += f"--{key} (default: {config[key]})\n"
    subparsers = parser.add_subparsers(dest="command", title="Available commands")
    sparser = subparsers.add_parser("set",formatter_class=argparse.RawTextHelpFormatter, add_help=False, help=helpconfig)
    allConfigParams=[]
    for configoption in config.keys():
        allConfigParams.append(sparser.add_argument(f"--{configoption}", type=str, default=config[configoption], help=f"Set {configoption}"))

    sparser = subparsers.add_parser("guiconfig", help="Show GUI configuration dialog")
    sparser = subparsers.add_parser("install",  help="Install fyoutube in the system's scheduler")
    sparser = subparsers.add_parser("status",  help="Display it fyoutube is currently running, and if it is installed in the system's scheduler")

    return parser.parse_args()

    
PIRATEMESSAGE = "\033[1m\033[93m\033[41mUsing this tool means that the video creators are not getting paid for their work, so please consider supporting them directly.\033[0m"
def main():
    args = parse_arguments()
    if not args.IAmAPirateAndIWillStarveTheCreators:
        print(PIRATEMESSAGE)

    if args.version:
        print(f"Version = {args.compatibilitymode}")
    elif args.command == "guiconfig":
        run_config()
    elif args.command == "install":
        run_install()
    elif args.command == "status":
        run_status()
    elif args.command == "set":
        print("Set mode activated:")
        print(args)
    else:
        print(f"No action taken.  {args.compatibilitymode=}")



if __name__ == "__main__":
    main()



####
# Todo : Split the code in two processe. One will build the list of videos to download and the other will download them.
# Todo : Configuration files in OS appropriate locations
# Todo : Metadata files in OS appropriate locations
# Todo : Use yt-dlp python API instead of subprocess
# Todo : Use a proper logging library instead of print statements
# Todo : Self register in cron / windows task scheduler
# Todo : Language support
# Todo : Set configuration from command line arguments
# Todo : Use a proper package manager for Python
# Todo : Use a proper package manager for Python dependencies     
# Todo : GUI to manage subscriptions and configurations
# Todo : Include Extract channel to get all the subscriptions
# Todo : Hook to run after download is complete
# Todo : Option to use RSS feeds to get new videos
# Todo : Add date last downloaded for each channel and start from the least recent
# Todo : Add messaging to remind the user that the creators are not getting paid for their work
# Todo : Add a way to donate to the creators
# Todo : Create a RSS feed of magnets to share with others with torrent clients
# Todo : Embed a torrent client.
# Todo : Download from the torrent client before downloading from YouTube
# Todo : Offer to the creator to upload the video directly to the torrent rss feed
# Todo : Opt-in telemetrics to see how many people are using the tool and how many videos are downloaded
# Todo : Update the tool through the tool itself/Torrent
