import os
from dotenv import load_dotenv
from Instafollower import InstaFollower

load_dotenv()
username_ig = os.getenv('email')
password_ig = os.getenv('password')
ig_account = os.getenv('insta')
link = "https://www.instagram.com/"
xx_path = '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'

InstaBot = InstaFollower()
InstaBot.login(username_ig, password_ig, link)
InstaBot.find_followers(ig_account)
InstaBot.follow()




