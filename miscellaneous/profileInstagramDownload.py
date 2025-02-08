import instaloader
import os
import re
from datetime import datetime
from itertools import dropwhile, takewhile

L = instaloader.Instaloader()

L.login("biiiped", "O8TK2tYX8649Ng")        # (login)

savePath = r"C:\Users\Biiiped\Desktop\hello"
profil="hardimages.v2"

posts = instaloader.Profile.from_username(L.context, profil).get_posts()
for post in posts:
    try:
        L.download_post(post, savePath)
    except Exception as e:
        print(e)
        continue



"""
def sanitize_filename(filename):

    return re.sub(r'[\\/*?:"<>|]', "", filename)

def download_profile_post(post_url, download_directory):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Extract the shortcode from the post URL
    shortcode = post_url.split("/")[-2]

    try:
        # Get post from shortcode
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        # Define the download path
        target_directory = os.path.join(download_directory, f"{post.owner_username}_{shortcode}")

        # Download the post
        loader.download_post(post, target=target_directory)

        # Sanitize filenames and rename files
        for filename in os.listdir(target_directory):
            file_path = os.path.join(target_directory, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                new_filename = sanitize_filename(f"{post.owner_username}_{post.shortcode}_{post.date_utc.strftime('%Y%m%d')}{file_extension}")
                new_file_path = os.path.join(download_directory, new_filename)
                os.rename(file_path, new_file_path)
        print(f"Downloaded post from {post_url} to {download_directory}")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the Instagram post URL

    # Define the desktop path
    

    # Call the function to download the post
    download_profile_post(instagram_post_url, desktop_path)
"""