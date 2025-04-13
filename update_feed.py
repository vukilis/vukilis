import feedparser
import re

README = "README.md"
START = "<!-- FEED-START -->"
END = "<!-- FEED-END -->"
MAX_ITEMS = 5

def fetch_feed():
    feed = feedparser.parse("https://vukilis.com/index.xml")
    items = feed.entries[:MAX_ITEMS]
    lines = ["## 🔗 Recent Blog Posts\n"]
    for item in items:
        lines.append(f"- [{item.title}]({item.link})")
    return "\n".join(lines)

def update_readme():
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    new_feed = fetch_feed()
    pattern = f"{START}.*?{END}"
    replacement = f"{START}\n{new_feed}\n{END}"
    updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    update_readme()
