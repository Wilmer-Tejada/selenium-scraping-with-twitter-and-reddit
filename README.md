# Using Selenium for Scraping Reddit and Posting on Twitter
This project is built in two seperate pieces. The first is to download images from a subreddit and the next is to post those images on twitter.

The first portion, downloading images from reddit is done using the `reddit_scraper.py` file. This scraper runs on a schedule and downloads images as long as the script is kept running. 

The second portion is done using the `twitter_scraper.py` file. This takes the images that were downloaded from the previous script and uploads them to Twitter.
