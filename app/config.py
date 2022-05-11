"""
On this file contains configuration variables
"""

import os

from dotenv import load_dotenv

load_dotenv()


LOCALE = os.environ.get("LOCALE", "ru")
COUNTRY = os.environ.get("COUNTRY", "UA")
URL = f"""
https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale={LOCALE}&country={COUNTRY}&allowCountries={COUNTRY}
"""
BASE_URL = f"https://store.epicgames.com/{LOCALE}/p"
