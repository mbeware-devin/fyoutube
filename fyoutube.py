#!/usr/bin/env python3
import Config

from manage_arguments import parse_arguments, load_fyoutube_version


def main():

    args = parse_arguments()
    if not args.IAmAPirateAndIWillStarveTheCreators:
        print(Config.i_PIRATEMESSAGE)

    if args.version:
        print(f"Version = {args.compatibilitymode}")
    elif args.command == "guiconfig":
        Config.run_config()
    elif args.command == "install":
        Config.run_install()
    elif args.command == "status":
        Config.run_status()
    elif args.command == "set":
        print("Set mode activated:")
        print(args)
    elif args.command == "go":
        main_module = load_fyoutube_version(args.compatibilitymode)
        main_module.get_videos()
    else:
        print("No command specified. Use -h for help.")
        return


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
