import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["my_little_pony_name", "type", "color", "favorite_food"]

def generate_row():

    return {
        "my_little_pony_name": random.choice([
        "Twilight Sparkle", "Rainbow Dash", "Pinkie Pie", "Rarity",
        "Applejack", "Fluttershy", "Starlight Glimmer", "Sunset Shimmer",
        "Princess Celestia", "Princess Luna", "Princess Cadance",
        "Sweetie Belle", "Apple Bloom", "Scootaloo", "Lyra Heartstrings",
        "Bon Bon", "Vinyl Scratch", "Octavia Melody", "Derpy Hooves",
        "Spitfire", "Soarin", "Berry Punch", "Cherry Spices",
        "Silver Spoon", "Diamond Tiara", "Crystal Breeze",
        "Moonbeam Dancer", "Velvet Dream", "Ember Glow", "Stardust Trail"
    ]),

    "type": random.choice([
        "unicorn", "pegasus", "earth pony", "alicorn"
    ]),

    "color": random.choice([
        "purple", "blue", "pink", "white", "orange", "yellow", "red",
        "green", "gray", "lavender", "mint", "gold", "silver", "crystal", "rainbow"
    ]),

    "favorite_food": random.choice([
        "cupcakes", "apple pie", "muffins", "cookies", "candy", "tea",
        "cake", "fruits", "pastries", "sweets", "chocolate", "berries", "sandwiches", "juice", "desserts"
    ])
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)