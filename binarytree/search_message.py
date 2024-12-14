"""
Kafka Log Search Script (Python 2.7)

This script reads Kafka log files and searches for specific messages based on user inputs. 
It verifies whether the publish time of messages falls within a specified topic retention period. 
The script reads multiple Kafka log files from multiple directories, searches for a unique string in messages, 
and ensures the message is within the retention period.

Author: [Your Name]
Version: 1.1
"""
import os
import re
from datetime import datetime, timedelta

def get_log_dirs(base_path='/u0/kafka-log'):
    """
    Gets the directories where Kafka stores its log files based on the specified base path.
    
    :param base_path: Base path for Kafka log files (default: /u0/kafka-log)
    :return: List of log directories
    """
    log_dirs = []
    try:
        # You may modify this section if you have specific topic names or dynamic path fetching
        log_dirs = [os.path.join(base_path, topic) for topic in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, topic))]
        print("Log directories found: ", log_dirs)
    except Exception as e:
        print("Error reading log directories:", e)
    return log_dirs

def search_messages(log_dirs, topic_name, unique_string, retention_period):
    """
    Searches for messages in the Kafka log files based on the topic name and unique string.
    It also checks if the message's publish time is within the retention period.
    
    :param log_dirs: List of log directories
    :param topic_name: The Kafka topic name to search for
    :param unique_string: The unique string to search in messages
    :param retention_period: The topic retention period (in hours)
    """
    current_time = datetime.now()
    retention_delta = timedelta(hours=retention_period)

    for dir_path in log_dirs:
        print("\nChecking directory:", dir_path)
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                if topic_name in file_name:
                    log_file = os.path.join(root, file_name)
                    print("Searching in file:", log_file)
                    with open(log_file, 'r') as f:
                        for line in f:
                            if unique_string in line:
                                publish_time = extract_publish_time(line)
                                if publish_time:
                                    time_diff = current_time - publish_time
                                    if time_diff <= retention_delta:
                                        print("Message is within retention period:", line)
                                    else:
                                        print("Message expired:", line)
                                else:
                                    print("No publish time found for message:", line)

def extract_publish_time(log_line):
    """
    Extracts the publish time from a Kafka log message.
    Assumes that the timestamp is in the format YYYY-MM-DD HH:MM:SS.
    
    :param log_line: A single line from the Kafka log file
    :return: Publish time as a datetime object, or None if no valid timestamp is found
    """
    match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_line)
    if match:
        return datetime.strptime(match.group(0), '%Y-%m-%d %H:%M:%S')
    return None

def is_within_retention(publish_time, retention_period):
    """
    Checks whether the publish time is within the retention period.
    
    :param publish_time: The publish time of the message
    :param retention_period: The topic retention period (in hours)
    :return: True if within retention period, False otherwise
    """
    current_time = datetime.now()
    retention_delta = timedelta(hours=retention_period)
    return (current_time - publish_time) <= retention_delta

if __name__ == "__main__":
    """
    Main function to run the Kafka log search script.
    It reads the inputs from the user, then searches the Kafka log files for messages.
    """
    # Predefined path for Kafka log files
    base_log_path = '/u0/kafka-log'

    # Input from the user
    topic_name = raw_input("Enter the Kafka topic name: ")
    unique_string = raw_input("Enter the unique string to search in messages: ")
    retention_period = int(raw_input("Enter the topic retention period (in hours): "))

    # Step 1: Read log directories from the base log path
    log_dirs = get_log_dirs(base_log_path)

    # Step 2: Search for messages in the log files
    search_messages(log_dirs, topic_name, unique_string, retention_period)