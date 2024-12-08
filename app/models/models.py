from app.db.mongo_manager import get_db

class User:
    @staticmethod
    def get_or_create(username):
        db = get_db()
        user = db.users.find_one({"username": username})
        if not user:
            db.users.insert_one({"username": username, "favorites": []})
            user = db.users.find_one({"username": username})
        return User(user)

    def __init__(self, data):
        self.username = data['username']
        self.favorites = data.get('favorites', [])

    def to_dict(self):
        return {"username": self.username, "favorites": self.favorites}

class Favorite:
    @staticmethod
    def toggle(username, character_id):
        db = get_db()
        user = db.users.find_one({"username": username})
        favorites = user.get('favorites', [])

        if character_id in favorites:
            favorites.remove(character_id)
        else:
            favorites.append(character_id)

        db.users.update_one({"username": username}, {"$set": {"favorites": favorites}})
        return {"username": username, "favorites": favorites}
