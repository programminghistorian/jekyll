#!/usr/bin/python

'''
Prepare original HTML files for Pandoc conversion to Markdown.
Making meta HTML tags for author, title, etc. enables Pandoc
to insert this info automatically in the YAML header of the md file.
'''

import os
import re
import time
from bs4 import BeautifulSoup

files = os.listdir('.')

for file in files:
    if file.endswith('.html'):
        print "Trying: " + str(file)
    
        # open the file, make soup
        f = open(file, 'r')
        html = f.read()
        soup = BeautifulSoup(html)
        f.close()
        
        # find relevant metadata
        original_head = soup.head
        author = soup.find(class_='byline')
        date = soup.find(class_='kicker')
        title = soup.article.header
        technical_reviewers = soup.find(class_='technical-reviewer')
        literary_reviewers = soup.find(class_='literary-reviewer')
        
        # create new author tag
        author_tag = soup.new_tag('meta')
        author_tag.attrs['name'] = 'author'
        if author:
            author_tag.attrs['content'] = author.string.lstrip('By ')
        
        # create new title tag
        title_tag = soup.new_tag('meta')
        title_tag.attrs['name'] = 'title'
        if title:
            title_tag.attrs['content'] = title.h1.a.string
        
        # create new reviewers tag
        reviewers = []
        if technical_reviewers:
           reviewers.append(technical_reviewers.string.split(': ')[1])
        if literary_reviewers:
           reviewers.append(literary_reviewers.string.split(': ')[1])
        reviewers_tag = soup.new_tag('meta', content=', '.join(reviewers))
        reviewers_tag.attrs['name'] = 'reviewers'
        
        # create new date tag
        date_tag = soup.new_tag('meta')
        date_tag.attrs['name'] = 'date'
        if date:
            date_str = time.strptime(date.string, '%B %d, %Y')
            date_tag.attrs['content'] = time.strftime('%m-%d-%Y', date_str)
        
        # append new tags into head, discarding old
        new_tags = [author_tag, title_tag, date_tag, reviewers_tag]
        for tag in new_tags:
            original_head.append(tag)
        
		# change attributes of `pre` blocks so pandoc will recognize them
        codeblocks = soup.find_all('pre')
        for block in codeblocks:
            brush = block.attrs['class'][1]
            block.attrs['class'] = brush
		    
        # try to decompose divs that won't be needed in markdown version
        headers = soup.find_all('header')
        footers = soup.find_all('footer')
        comments = soup.find_all(class_=re.compile('comment.*'))
        comments.append(soup.find('div', {'id': 'respond'}))
        comments.append(soup.find('h3', {'id': 'comments'}))
        old_tags = [author, date, title, technical_reviewers, literary_reviewers] + headers + footers + comments
        for tag in old_tags:
            try: 
                tag.decompose()
            except:
                continue
        
        # write new HTML to file
        f = open(file, 'w')
        f.write(str(soup))
        print "Successful: " + str(file)
        f.close
    
