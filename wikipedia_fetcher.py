import wikipediaapi
import datetime

def fetch_wikipedia_summary(topic):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='project-3-study-app (andromachintoupi@gmail.com)'
    )
    page = wiki.page(topic)

    if not page.exists():
        return None

    return page.summary

def clean_text(text, max_words=500):
    words = text.split()
    cleaned = " ".join(words[:max_words])
    return cleaned

def get_clean_wikipedia_text(topic):
    raw_text = fetch_wikipedia_summary(topic)
    if raw_text is None:
        return None
    return clean_text(raw_text)

def save_output(topic, summary):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"example_outputs/{topic.replace(' ', '_')}_{now}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"📚 Study Topic: {topic}\n\n")
        f.write("📘 Cleaned Summary:\n")
        f.write(summary)
    print(f"\n✅ Summary saved to: {filename}")

def log_search(topic):
    with open("search_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} - Searched: {topic}\n")

if __name__ == "__main__":
    topic = input("🔎 Enter a study topic: ").strip()

    log_search(topic)
    summary = get_clean_wikipedia_text(topic)

    if summary:
        print("\n📘 Cleaned Summary:\n")
        print(summary)
        save_output(topic, summary)
    else:
        print("⚠️ Topic not found. Please try another.")
