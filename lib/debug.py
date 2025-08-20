#!/usr/bin/env python3
import pdb

from author import Author
from magazine import Magazine
from article import Article

if __name__ == '__main__':
    # Create sample data for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Science Weekly", "Science")
    
    article1 = Article(author1, magazine1, "The Future of Technology")
    article2 = Article(author1, magazine2, "Climate Change Solutions")
    article3 = Article(author2, magazine1, "Programming Best Practices")
    
    # Start debugging session
    pdb.set_trace()