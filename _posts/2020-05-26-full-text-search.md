---
title: |
  Full-Text Search for Lessons
authors:
- Zoe LeBlanc
layout: post
categories: posts
---

In an effort to make finding lessons more user-friendly, we've officially launched full-text searching for all our lessons. Previously you could use filter buttons to select lessons based on topic or activity, and sort them by date and difficulty. However, you weren't able to find lessons based on their content.

As of today now you can you dig even deeper, finding the exact lesson to match your interests in all of our supported languages! This feature has been a long time coming (our initial issue ticket was opened on September 20, 2018) and we hope this new addition will make Programming Historian even more accessible.

## How to search?

To use the search feature, go to the lessons page and click on the `Start Searching` button.

<figure>
  <img src="/images/full-text-search/start_search.png" alt="Initial lesson home page, showing the start search button." title="Initial lesson home page, showing the start search button."/>
  <figcaption>Initial lesson home page. Click start searching to enter search queries.</figcaption>
</figure>

<br/>

You'll now see a search bar and button. You can enter your search terms and get a list of the relevant  lessons, with the search terms highlighted.

<figure>
  <img src="/images/full-text-search/search_results.png" alt="Search results displaying highlighted search terms." title="Search results displaying highlighted search terms."/>
  <figcaption>Search results for <em>Twitter</em> and <em>Network</em></figcaption>
</figure>

<br/>

The results are ranked by relevance and you can also filter them using our existing buttons.

<figure>
  <img src="/images/full-text-search/search_filter.png" alt="Search results displaying highlighted search terms with selected filters." title="Search results displaying highlighted search terms with selected filters."/>
  <figcaption>Search results for <em>Twitter</em> and <em>Network</em> with topic <em>Python</em></figcaption>
</figure>

<br/>
If you want more information about searching, you can click the information button to get more details about how to use this feature.

<img src="/images/full-text-search/search_info.png" alt="Search info section, displaying additional details on how to search." title="Search info section, displaying additional details on how to search."/>

## How does the search work?

Behind the scenes, this search feature uses [LunrJS](https://lunrjs.com), a software package for enabling full-text search on static sites.
<div style="display: flex;">
  <figure>
    <img src="/images/full-text-search/inverted_index.jpeg" alt="Search info section, displaying additional details on how to search." title="Search info section, displaying additional details on how to search."/>
    <figcaption>Inverted index diagram</figcaption>
  </figure>
  <figure>
    <img src="/images/full-text-search/book_index.jpg" alt="Search info section, displaying additional details on how to search." title="Search info section, displaying additional details on how to search."/>
    <figcaption>Book index (<a href="https://commons.wikimedia.org/wiki/File:Book_of_Knowledge_1919_Vol_20,_General_Index_Start.jpg">from Wikipedia entry on <em>Book of Knowledge</em></a>)</figcaption>
  </figure>
</div>

Lunr builds an *inverted index* of all our lessons, which is essentially the same as an index at the back of a book. So each time you enter a search term, Lunr looks for term, finds all the lessons that is in, and then returns the lessons based on relevance of the term (which is calculated using an information retrieval algorithm called [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)).

For optimal results, we recommend using multiple search terms, as well as the `+` and `-` symbols to get exact searches or limit searches, respectively. You can also read more about how to search with Lunr on their [searching documentation](https://lunrjs.com/guides/searching.html).

## How did we implement search?

In adding full-text search, we have endeavored to optimize speed, as well as accuracy of results. Most search engines utilized inverted indices (like Solr or ElasticSearch) but they still expect you to have some sort of database to dynamically return results to your queries. Since we use a static site architecture, we don't have any live databases, which means that our entire search index needs to be built prior to the site being loaded (otherwise users won't be able to get search results).

Lunr remains one of the most common solutions for adding search to static site, but there's a few drawbacks. One is that it takes a lot of time to build the search index and it can end up creating fairly large files to be loaded into the browser. We also had the additional complication of wanting to separate search results by language.

In the end, we implemented a fairly novel approach (as far as I know) to generate the search corpora using Jekyll, and then built a separate NodeJS app to make the search indices - in essence creating a microservice. You can view the code for this search index building in the [search-index repository](https://github.com/programminghistorian/search-index), and we used TravisCI to automatically rebuild the indices every night. In separating out the search index building, we were able to limit the JavaScript dependencies in our main repository and minimize the time needed to build the site locally. Having the indices built separately also allowed us to use Github's built-in CDN functionality for serving the indices, as well as enabling us to limit the JavaScript payload for slower connections.

For more information about the technical features behind our full-text search, feel free to visit our [technical documentation on search](https://github.com/programminghistorian/jekyll/wiki/Technical-Tutorial-on-Search).

We hope that search allows users to more easily access lessons, as well as discover lessons in new ways. As Programming Historian continues to produce new lessons and support for additional languages, we hope features like full-text search help us maintain a user-friendly and sustainable web infrastructure.