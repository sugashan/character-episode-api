import os
import requests

BASE_URL = os.getenv('API_BASE_URL', 'https://rickandmortyapi.com')

def fetch_characters(page):
    response = requests.get(f"{BASE_URL}/api/character?page={page}")
    response.raise_for_status()
    data = response.json()
    return [
        {
            "id": char['id'],
            "name": char['name'],
            "image": char['image'],
            "species": char['species'],
            "gender": char['gender'],
            "origin": char['origin']['name'],
            "status": char['status'],
            "episodes": char['episode'][-3:]
        } for char in data['results']
    ]


def fetch_characters_using_grapghQL(page):
    query = """
    query($page: Int!) {
        characters(page: $page) {
            info {
                count
                pages
            }
            results {
                id
                name
                image
                species
                gender
                origin {
                    name
                }
                status
                episode {
                    name
                }
            }
        }
    }
    """
    variables = {"page": page}
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()
    return [
        {
            "id": char["id"],
            "name": char["name"],
            "image": char["image"],
            "species": char["species"],
            "gender": char["gender"],
            "origin": char["origin"]["name"],
            "status": char["status"],
            "episodes": [ep["name"] for ep in char["episode"][-3:]],
        }
        for char in data["data"]["characters"]["results"]
    ]