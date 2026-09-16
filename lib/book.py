#!/usr/bin/env python3

class Book:
    def __init__(self, title="Untitled", page_count=100):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        # Increment page count when turning a page
        self.page_count += 1
    
        