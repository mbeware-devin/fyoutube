# fyoutube - YouTube Content Archiving System

## Overview

fyoutube is an automated YouTube content downloading and archiving system designed for long-term content preservation. The system continuously monitors a list of subscribed YouTube channels and automatically downloads new videos as they become available, preventing content loss due to deletions, account suspensions, or platform changes.

## Features

- **Automated Channel Monitoring**: Continuously monitors YouTube channels from a subscription list
- **Resume Capability**: Resumes downloads from the last processed channel after interruptions
- **Duplicate Prevention**: Maintains archive files to prevent re-downloading existing content
- **Multiple Download Engines**: Four different implementations for various use cases
- **Configurable Parameters**: Extensive configuration system with context-aware options
- **Comprehensive Logging**: Detailed logging for monitoring and debugging

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install yt-dlp
   ```

2. **Configure Channels**:
   Edit `subscriptions.list` with YouTube channel URLs (one per line):
   ```
   https://www.youtube.com/@example-channel
   https://www.youtube.com/playlist?list=PLexample
   ```

3. **Run fyoutube**:
   ```bash
   python fyoutube.py --IAmAPirateAndIWillStarveTheCreators go
   ```

## Architecture

fyoutube consists of several key components:

- **Main Entry Point** (`fyoutube.py`): CLI interface and command dispatch
- **Download Engines**: Multiple implementations for different use cases
  - `fyoutube_V09.py`: Primary engine with subprocess-based yt-dlp calls
  - `fyoutube_main.py`: Alternative using direct yt-dlp library interface
  - `fyoutube_select.py`: Specialized content archiving with filtering
  - `fyoutube_yt_dlp.py`: Direct Python library interface
- **Configuration System** (`Config.py`): Centralized configuration management
- **State Management**: Resume capability and archive tracking

## Documentation

- **[Architecture](ARCHITECTURE.md)**: System flow diagrams and component overview
- **[Functions](FUNCTIONS.md)**: Detailed function documentation with file/folder dependencies
- **[yt-dlp Parameters](YT_DLP_PARAMETERS.md)**: Complete catalog of yt-dlp parameters used

## Configuration

The system uses a sophisticated configuration system with:

- **OptionDescriptor Pattern**: Context-aware parameter definitions
- **TOML Configuration**: User-configurable settings
- **Environment-specific Paths**: Automatic path resolution for different platforms

Key configuration files:
- `subscriptions.list`: Channel URLs to monitor
- `lastdownloadedchannel.info`: Resume state
- `baseconfig.toml`: User configuration (auto-generated)

## Usage Examples

### Basic Download
```bash
python fyoutube.py --IAmAPirateAndIWillStarveTheCreators go
```

### Version Selection
```bash
python fyoutube.py --compatibilitymode V0.9 go
```

### Configuration Management
```bash
python fyoutube.py guiconfig  # GUI configuration
python fyoutube.py status     # Check status
python fyoutube.py install    # Install scheduler
```

## File Structure

```
fyoutube/
├── fyoutube.py              # Main entry point
├── Config.py                # Configuration system
├── manage_arguments.py      # CLI argument handling
├── fyoutube_V09.py         # Primary download engine
├── fyoutube_main.py        # Alternative engine
├── fyoutube_select.py      # Content archiving engine
├── fyoutube_yt_dlp.py      # Direct library interface
├── subscriptions.list      # Channel URLs
├── lastdownloadedchannel.info  # Resume state
├── ARCHITECTURE.md         # System documentation
├── FUNCTIONS.md           # Function documentation
└── YT_DLP_PARAMETERS.md   # Parameter documentation
```

## Important Notes

⚠️ **Ethical Usage**: This tool downloads content from YouTube. Please consider supporting content creators directly through official channels, subscriptions, or donations.

⚠️ **Legal Compliance**: Ensure your usage complies with YouTube's Terms of Service and applicable copyright laws in your jurisdiction.

⚠️ **Rate Limiting**: The system includes built-in rate limiting to be respectful of YouTube's servers.

## Contributing

When contributing to fyoutube:

1. Read the architecture documentation to understand the system design
2. Follow the existing code patterns and configuration system
3. Update documentation when adding new features
4. Test with the restricted channel list during development

## License

This project is for educational and personal archival purposes. Users are responsible for ensuring their usage complies with applicable laws and terms of service.
