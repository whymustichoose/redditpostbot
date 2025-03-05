# Reddit Post Manager

A Python script that helps you manage and automate posting content to multiple subreddits. The script reads content from text files and posts them to specified subreddits using the Reddit API.

## Features

- Post content to multiple subreddits from text files
- Support for markdown formatting in posts
- Configurable Reddit API credentials
- Detailed logging of posting activities
- Easy to add new content through text files

## Prerequisites

- Python 3.x
- Reddit API credentials (client ID and client secret)
- Reddit account with appropriate permissions

## Installation

1. Clone this repository:
```bash
git clone https://github.com/whymustichoose/rdprj2.git
cd rdprj2
```

2. Install required packages:
```bash
pip install praw
```

3. Create your configuration file:
   - Copy `config.example.txt` to `config.txt`
   - Fill in your Reddit credentials in `config.txt`

## Configuration

### Reddit API Setup

1. Go to https://www.reddit.com/prefs/apps
2. Click "create another app..."
3. Select "script"
4. Fill in the required information
5. Once created, you'll get:
   - Client ID (under the app name)
   - Client Secret

### Config File

Create a `config.txt` file with the following format:
```
username=your_reddit_username
password=your_reddit_password
client-id=your_reddit_client_id
client-secret=your_reddit_client_secret
```

## Content Files

Create your content files in the `content` directory. Each file should follow this format:

1. First line: Target subreddit name
2. Second line: Post title
3. Remaining lines: Post body content

Example:
```
subreddit_name
Post Title

Post content goes here...
You can use **markdown** formatting
- Lists
- Tables
- Links
```

See `content/content.example.txt` for a detailed template.

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Read all `.txt` files from the `content` directory
2. Post each file's content to its specified subreddit
3. Log all activities to `reddit.log`

## Logging

All posting activities and errors are logged to `reddit.log` in the following format:
```
MM/DD/YYYY HH:MM:SS AM/PM LEVEL : Message
```

## File Structure

```
rdprj2/
├── main.py              # Main script
├── config.txt          # Your Reddit credentials (not in repo)
├── config.example.txt  # Example configuration
├── reddit.log         # Log file (not in repo)
└── content/
    ├── content.txt    # Your content files (not in repo)
    └── content.example.txt  # Example content template
```

## Notes

- The script will skip any files that don't follow the required format
- Each content file can target a different subreddit
- Make sure your Reddit account has appropriate permissions for the subreddits you're posting to
- The script uses the Reddit API's rate limits, so it may take some time to process multiple files

## License

This project is open source and available under the MIT License.
