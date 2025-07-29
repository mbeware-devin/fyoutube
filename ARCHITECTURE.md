# fyoutube System Architecture

## Overview

fyoutube is an automated YouTube content downloading and archiving system built around yt-dlp with Python orchestration for subscription management, state persistence, and automated scheduling.

## System Flow Diagram

```mermaid
graph TD
    A[fyoutube.py - Main Entry Point] --> B[manage_arguments.py - Parse CLI Args]
    B --> C{Command Type}
    
    C -->|go| D[load_fyoutube_version()]
    C -->|guiconfig| E[Config.run_config()]
    C -->|install| F[Config.run_install()]
    C -->|status| G[Config.run_status()]
    C -->|set| H[Configuration Setting]
    
    D --> I{Version Selection}
    I -->|V0.9/Current| J[fyoutube_V09.py - Primary Engine]
    I -->|dev| K[fyoutube_main.py - Alternative Engine]
    
    J --> L[get_videos() - Main Loop]
    K --> M[get_videos() - Alternative Loop]
    
    L --> N[Read subscriptions.list]
    M --> N
    
    N --> O[For each channel URL]
    O --> P{New Channel?}
    
    P -->|Yes| Q[InfoFromPlaylist() - Populate Archive]
    P -->|No| R[download_playlist() - Download Videos]
    
    Q --> S[Create channel config file]
    R --> T[Execute yt-dlp with parameters]
    
    S --> U[save_lastchannel()]
    T --> U
    
    U --> V[Sleep 600 seconds]
    V --> L
    
    subgraph "Configuration System"
        W[Config.py - Central Configuration]
        X[OptionDescriptor - Parameter Definitions]
        Y[build_options() - Context-aware Config]
        Z[UserConfig - TOML Configuration]
    end
    
    subgraph "File Dependencies"
        AA[subscriptions.list - Channel URLs]
        BB[lastdownloadedchannel.info - Resume State]
        CC[archive_global.list - Downloaded Videos]
        DD[VIDEO_DIR - Downloaded Content]
        EE[LOGS_DIR - Log Files]
        FF[ARCHIVE_DIR - Archive Files]
    end
    
    subgraph "Alternative Engines"
        GG[fyoutube_select.py - Content Archiving]
        HH[fyoutube_yt_dlp.py - Direct Library Interface]
        II[fyoutube_download.py - Specialized Download]
    end
    
    J -.-> W
    K -.-> W
    GG -.-> W
    HH -.-> W
    II -.-> W
    
    L -.-> AA
    L -.-> BB
    L -.-> CC
    T -.-> DD
    T -.-> EE
    T -.-> FF
```

## Core Components

### 1. Entry Point Layer
- **fyoutube.py**: Main CLI entry point with command dispatch
- **manage_arguments.py**: Argument parsing and version management

### 2. Download Engines
- **fyoutube_V09.py**: Primary download engine with continuous monitoring
- **fyoutube_main.py**: Alternative implementation using direct yt-dlp library
- **fyoutube_select.py**: Specialized content archiving with filtering
- **fyoutube_yt_dlp.py**: Direct yt-dlp Python library interface
- **fyoutube_download.py**: Specialized download function

### 3. Configuration System
- **Config.py**: Central configuration with OptionDescriptor pattern
- **OptionDescriptor**: Structured parameter definitions with context flags
- **UserConfig**: TOML-based user configuration management

### 4. State Management
- **subscriptions.list**: Plain text file with YouTube channel URLs
- **lastdownloadedchannel.info**: Resume state for interrupted downloads
- **archive_global.list**: Master archive preventing re-downloads

## Data Flow

1. **Initialization**: CLI arguments parsed, version selected, configuration loaded
2. **Channel Processing**: Read subscription list, resume from last processed channel
3. **New Channel Detection**: Use InfoFromPlaylist() to populate archive without downloading
4. **Download Execution**: Use download_playlist() with full yt-dlp parameter set
5. **State Persistence**: Save last processed channel, update archives
6. **Loop Continuation**: Sleep and repeat the cycle

## Key Design Patterns

- **Version Compatibility**: Dynamic module loading for different implementations
- **Context-Aware Configuration**: OptionDescriptor with info/download/debug contexts
- **Resume Capability**: State persistence across interruptions
- **Archive Management**: Prevent duplicate downloads across channels
- **Error Handling**: Graceful degradation with comprehensive logging
