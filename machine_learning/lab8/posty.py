# import snscrape.modules.reddit as snreddit
# import json

# # Funkcja do pobierania postów z Reddita
# def scrape_reddit(subreddit, query, limit):
#     scraped_posts = []
#     scraper = snreddit.RedditSearchScraper(f'subreddit:{subreddit} {query}')

#     for i, post in enumerate(scraper.get_items()):
#         if i >= limit:
#             break
#         scraped_posts.append({
#             "title": post.title,
#             "content": post.selftext,
#             "author": post.author,
#             "date": post.date.strftime("%Y-%m-%d %H:%M:%S"),
#             "url": post.url
#         })

#     return scraped_posts

# # Konfiguracja
# subreddit = "technology"  # Możesz zmienić na dowolny subreddit
# query = "AI"  # Temat do wyszukiwania
# limit = 100  # Liczba postów do pobrania

# # Pobieranie postów
# try:
#     posts = scrape_reddit(subreddit, query, limit)

#     # Zapisanie do pliku JSON
#     output_file = "reddit_posts.json"
#     with open(output_file, "w", encoding="utf-8") as f:
#         json.dump(posts, f, ensure_ascii=False, indent=4)

#     print(f"Pobrano {len(posts)} postów i zapisano w pliku {output_file}.")

# except Exception as e:
#     print(f"Wystąpił błąd podczas pobierania postów: {e}")

import praw
import json

# Konfiguracja PRAW
reddit = praw.Reddit(
    client_id="X1Gjy0VUG3TADfCJqhgP4Q",
    client_secret="mgHgxzDB_urB-zmeCj85wDqA8uxCmQ",
    user_agent="smt_v0.01"
)

# Funkcja do pobierania postów z Reddita
def scrape_reddit(subreddit, query, limit):
    subreddit = reddit.subreddit(subreddit)
    posts = []
    for submission in subreddit.search(query, limit=limit):
        posts.append({
            "title": submission.title,
            "content": submission.selftext,
            "author": submission.author.name if submission.author else "unknown",
            "date": submission.created_utc,
            "url": submission.url
        })
    return posts

# Konfiguracja
subreddit = "technology"
query = "AI"
limit = 100

# Pobieranie postów
posts = scrape_reddit(subreddit, query, limit)

# Zapisanie do pliku
with open("reddit_posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)

print(f"Pobrano {len(posts)} postów.")
