#!/bin/bash

# Define the cron job command
CRON_JOB="*/5 * * * * /usr/bin/python3 /home/thinkpad/Documents/Medium/1-api/news_api_project/fetch_news.py >> /home/thinkpad/Documents/Medium/1-api/news_api_project/execution_logs/cron_log.txt 2>&1"

# Check if the cron job already exists to avoid duplication
(crontab -l | grep -v -F "$CRON_JOB"; echo "$CRON_JOB") | crontab -

echo "✅ Scheduled cron job to run every 5 minutes."

# Schedule a one-time cron job to remove it at midnight
(crontab -l; echo "59 23 * * * crontab -r") | crontab -

echo "✅ Scheduled removal of cron job at midnight."
