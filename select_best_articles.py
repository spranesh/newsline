import random
import newsitem

def select_relevant_articles(articles, ranked_keywords):
    # Sort each of the set of articles by date
    for x in articles:
        x.sort(reverse=True)

    relevances = [b for (a, b) in ranked_keywords]
    probabilites = [x/sum(relevances) for x in relevances] + [0.2] * 10

    final_articles = set()

    for i in range(len(articles)):
        for y in articles[i]:
            final_articles.add(y)
            if random.uniform(0, 1) > probabilites[i]:
                break

    return list(final_articles)

def select_all_articles(articles, ranked_keywords):
    s = set()
    for group in articles:
        for a in group:
          s.add(a)
    return list(s)