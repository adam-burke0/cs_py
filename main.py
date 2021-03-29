import requests
import json

with open("skins.txt", "r") as f_read, open("prices.txt", "w") as f_write:
  for line in f_read:
    skin_name = line.strip()
    skin_info = requests.get("http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=" + skin_name)
    skin_json = json.loads(skin_info.text)
    median = skin_json["median_price"]
    f_write.write("\n" + skin_name + ": " + median.replace('€', '') )
    print(skin_name + ": " + skin_json["median_price"])
