import os
from app.db.mongo_manager import get_db
from datetime import datetime, timedelta

CACHE_EXPIRY_HOURS = int(os.getenv('CACHE_EXPIRY_HOURS', 24))
CACHE_EXPIRY = timedelta(hours=CACHE_EXPIRY_HOURS)

def get_cached_data(key, page):
    db = get_db()
    cache = db.cache.find_one({"key": key, "page": page})
    if cache and cache['expiry'] > datetime.utcnow():
        return cache['data']
    return None

def set_cached_data(key, data, page):
    db = get_db()
    db.cache.update_one(
        {"key": key, "page": page},
        {"$set": {"data": data, "expiry": datetime.utcnow() + CACHE_EXPIRY}},
        upsert=True
    )
