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

in_path = './original_html'
out_path = './modified_html'
files = os.listdir(in_path)

for file in files:
    if file.endswith('.html'):
        print "Converting: " + str(file)
    
        # open the file, make soup
        f = open(in_path + '/' + file, 'r')
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
        reviewers = [i.rstrip() for i in set(reviewers)]
        reviewers_tag = soup.new_tag('meta', content=', '.join(reviewers))
        reviewers_tag.attrs['name'] = 'reviewers'
        
        # create new date tag
        date_tag = soup.new_tag('meta')
        date_tag.attrs['name'] = 'date'
        if date:
            date_str = time.strptime(date.string, '%B %d, %Y')
            date_tag.attrs['content'] = time.strftime('%Y-%m-%d', date_str)
        
        # create new layout tag
        layout_tag = soup.new_tag('meta')
        layout_tag.attrs['name'] = 'layout'
        layout_tag.attrs['content'] = 'default'

        # append new tags into head
        new_tags = [author_tag, title_tag, date_tag, reviewers_tag, layout_tag]
        for tag in new_tags:
            original_head.append(tag)
        
        # change attributes of `pre` blocks so pandoc will recognize them
        codeblocks = soup.find_all('pre')
        for block in codeblocks:
            if block.attrs:
               brush = block.attrs['class'][1]
               if brush != 'plain;': block.attrs = {'class': brush.rstrip(';')}

        # change monospace inline spans to code tags
        spans = soup.find_all('span', class_=re.compile('filename|userinput'))
        for span in spans:
            span.name = 'code'
            span.attrs = {}

        # change figures and figcaptions
        figs = soup.find_all(re.compile('figure|figcaption'))
        for fig in figs:
            if fig.br: fig.br.decompose()
            fig.name = 'p'
        for image in soup.find_all('img'):
            parent = image.parent
            if parent.name == 'a':
               image.attrs['src'] = parent.attrs['href']
               parent.unwrap()

        # try to decompose divs that won't be needed in markdown version
        nav_pager = soup.find('ul', class_='navigation')
        headers = soup.find_all('header')
        footers = soup.find_all('footer')
        comments = soup.find_all(class_=re.compile('comment.*'))
        comments.append(soup.find('div', {'id': 'respond'}))
        comments.append(soup.find('h3', {'id': 'comments'}))
        old_tags = [author, date, title, technical_reviewers, literary_reviewers, nav_pager] + headers + footers + comments
        for tag in old_tags:
            try: 
                tag.decompose()
            except:
                continue
        
        # write new HTML to file
        f = open(out_path + '/' + file, 'w')
        f.write(str(soup))
        f.close
    
