# main packagess 
from RedDownloader import RedDownloader
#from instagrapi import instagrapi

# sub packages
import time
#import os
#import random

def GetMeme():
    post = RedDownloader.DownloadBySubreddit('dankmemes' , 1 , quality = 720 , SortBy='new')
    author = post.GetPostAuthors()[0]
    print(f'\nSubreddit: r/dankmemes')
    print(f'Author: {author}\n')
    return author 

while True:
    GetMeme()
    time.sleep(100000)
