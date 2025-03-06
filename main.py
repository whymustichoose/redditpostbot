import praw
import logging
import os
from pathlib import Path

logging.basicConfig(filename='reddit.log', level=logging.INFO,
                   format='%(asctime)s %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def read_config():
	"""Read and validate the configuration file."""
	try:
		with open('config.txt', 'r') as config_file:
			config_settings = config_file.readlines()
	except FileNotFoundError:
		raise Exception('config.txt file not found!')

	# Validate configuration
	for config in config_settings:
		if config[-2:] == '=\n' and config[:10] != 'submission':
			raise Exception('Configuration field left blank!')

	# Parse configuration
	config = {
		'username': config_settings[0][9:].rstrip(),
		'password': config_settings[1][9:].rstrip(),
		'client_id': config_settings[2][10:].rstrip(),
		'client_secret': config_settings[3][14:].rstrip()
	}
	return config

def process_content_file(file_path):
	"""Process a single content file and return subreddit, title and body."""
	try:
		with open(file_path, 'r') as content_file:
			content = content_file.readlines()
	except FileNotFoundError:
		raise Exception(f'Content file not found: {file_path}')

	if not content:
		raise Exception(f'Content file is empty: {file_path}')

	if len(content) < 2:
		raise Exception(f'Content file must have at least 2 lines (subreddit and title): {file_path}')

	subreddit = content[0].rstrip()
	submission_title = content[1].rstrip()
	submission_body = ''.join(line.rstrip() + '\n' for line in content[2:])
	
	return subreddit, submission_title, submission_body

def post_to_reddit(reddit, subreddit, title, body):
	"""Submit a post to Reddit."""
	try:
		target_subreddit = reddit.subreddit(subreddit)
		target_subreddit.submit(
			title=title,
			selftext=body,
			url=None,
			resubmit=True,
			send_replies=True
		)
		logging.info(f'Successful post to /r/{subreddit}: {title}')
	except Exception as err:
		logging.error(f'Failed to post to /r/{subreddit}: {str(err)}')
		raise

def main():
	# Read configuration
	try:
		config = read_config()
	except Exception as err:
		logging.error(f'Configuration error: {str(err)}')
		return

	# Initialize Reddit client
	try:
		reddit = praw.Reddit(
			client_id=config['client_id'],
			client_secret=config['client_secret'],
			password=config['password'],
			username=config['username'],
			user_agent="User"
		)
	except Exception as err:
		logging.error(f'Failed to initialize Reddit client: {str(err)}')
		return

	# Process all content files in the content directory
	content_dir = Path('content')
	if not content_dir.exists():
		content_dir.mkdir()
		logging.info('Created content directory')
		return

	for content_file in content_dir.glob('*.txt'):
		if 'example' in content_file.name.lower():
			logging.info(f'Skipping example file: {content_file}')
			continue
		try:
			subreddit, title, body = process_content_file(content_file)
			post_to_reddit(reddit, subreddit, title, body)
		except Exception as err:
			logging.error(f'Failed to process {content_file}: {str(err)}')
			continue

if __name__ == '__main__':
	main()