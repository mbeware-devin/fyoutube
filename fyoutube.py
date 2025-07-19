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
# Todo : Create a RSS feed of magnets to share with others with torrent clients
# Todo : Embed a torrent client.
# Todo : Download from the torrent client before downloading from YouTube
# Todo : Offer to the creator to upload the video directly to the torrent rss feed
