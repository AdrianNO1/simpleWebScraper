import os, json, datetime, time, random
try:
    from simpleWebScraper import scrape
except ModuleNotFoundError:
    print("To enable global use of the package, install the package using 'pip install -e .' in the same directory as the setup.py file.")
    exit(1)

dir_path = os.path.dirname(os.path.realpath(__file__))

url = "https://socialblade.com/youtube/channel/UCVun3IyFIh6AsEMV11zlVHg"

target_elem = '<span id="youtube-stats-header-subs" style="display: none;">911K</span>'

def main():
    data = scrape(url, target_elem, use_selenium=True, element_properties=["id"], return_html=True)

    if data[1]:
        print(f"Error: {data[1]}")
        if data[2]:
            with open(os.path.join(dir_path, "webpage.html"), "w", encoding="utf-8") as f:
                f.write(data[2])
    else:
        print(data[0])

        with open(os.path.join(dir_path, "data.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"datetime": str(datetime.datetime.now()), "subs": data[0]}) + "\n")

        if data[2]:
            with open(os.path.join(dir_path, "webpage.html"), "w", encoding="utf-8") as f: # for debugging
                f.write(data[2])

while True:
    main()
    time.sleep(90)
    now = datetime.datetime.now()
    next_hour = now + datetime.timedelta(hours=1)
    next_hour = next_hour.replace(minute=0, second=0, microsecond=0)
    time.sleep((next_hour - now).seconds + random.randint(-15, 15))