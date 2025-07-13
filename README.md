# Simple YouTube Downloader

A simple Python script to download YouTube videos using a graphical interface for URL input and folder selection.

## Features
- Download YouTube videos in the highest available MP4 quality
- Simple GUI input for video URL (no need to use the command line)
- Choose the download folder using a folder picker dialog
- Error handling for invalid URLs or download issues

## Requirements
- Python 3.x
- pytube
- tkinter (usually included with Python)

## Installation
1. Install Python 3 if you don't have it: https://www.python.org/downloads/
2. Install pytube:
   ```sh
   pip install pytube
   ```

## Usage
1. Run the script:
   ```sh
   python youtube.py
   ```
2. Enter the YouTube video URL in the popup window.
3. Select the folder where you want to save the video.
4. Wait for the download to complete. The script will notify you when done.

## Troubleshooting
- **HTTP Error 400: Bad Request**: Make sure the URL is correct, public, and not restricted. Try updating pytube if the error persists:
  ```sh
  pip install --upgrade pytube
  ```
- **No URL entered**: The script will exit if you don't provide a URL.
- **No folder selected**: The script will exit if you don't select a folder.

## Example
```
Enter the YouTube video URL: [GUI input box]
Selected folder: C:/Users/YourName/Downloads
Starting download...
Downloaded: Example Video Title
Download completed!
```

## License
This project is for educational purposes only. Please respect YouTube's Terms of Service.
