# Magazine Domain

Python classes for managing authors, magazines, and articles.

## Files

- `lib/author.py` - Author class
- `lib/magazine.py` - Magazine class  
- `lib/article.py` - Article class
- `lib/debug.py` - Testing script
- `test_implementation.py` - Tests

## Setup

```bash
pipenv install
pipenv shell
```

## Usage

``` python
from lib. author import Author
from lib. magazine import Magazine
from lib. article import Article

author = Author("John Doe")
magazine = Magazine("Tech Today", "Technology")
article = Article(author, magazine, "The Future of Technology")

print(author.articles())
print(magazine.contributors())
```

## Testing

```bash
python test_implementation.py
cd lib && python debug.py
```

## Classes

### Author
- `Author(name)` - create author
- `articles()` - get articles
- `magazines()` - get magazines
- `add_article(magazine, title)` - add article
- `topic_areas()` - get categories

### Magazine  
- `Magazine(name, category)` - create magazine
- `articles()` - get articles
- `contributors()` - get authors
- `article_titles()` - get titles
- `contributing_authors()` - authors with >2 articles
- `top_publisher()` - magazine with the most articles

### Article
- `Article(author, magazine, title)` - create article
- `author`, `magazine`, `title` properties

## AUTHOR
IVVY
