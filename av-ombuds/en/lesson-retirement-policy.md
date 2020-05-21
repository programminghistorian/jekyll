---
title: Lesson Retirement Policy
layout: blank
redirect_from: /lesson-retirement-policy
---

# Lesson Retirement Policy

The _Programming Historian_ editors do their best to maintain lessons as minor issues inevitably arise. 
However, as time passes, changes to either the underlying technologies or principles used by a given lesson can become so substantial that users will no longer be able to successfully complete the lesson.
In these situations, the _Programming Historian_ editorial team may decide to "retire" a lesson: keeping the page published, but removing it from our directory of active lessons and adding a warning to the top of the page noting that not all elements of the lesson may be working as originally intended.

We do not retire lessons lightly.
If the editorial team begins to receive reports about problems with a lesson, we will investigate the problem and take steps to address it.
Often, we will decide it is not necessary to retire the lesson:

- In cases where minor fixes are easily done, such as correcting the formatting of a lesson, or changing one or two broken URLs, we will generally do so.
- In cases where new methods for a task have emerged that may be preferred to the methods discussed in a lesson, but the original technology for a lesson still works and is available, we will **not** retire the lesson. The lesson may still prove a useful learning tool and a snapshot into the techniques of digital history when it was published

However, if it is clear that systemic changes to text, code, and/or figures are necessary, and that such changes are of a scale that would require complete re-testing of the entire lesson, then we will open a public issue to discuss the possibility of retiring the lesson between all the members of the editorial team.

In cases where members of the editorial team, or members of the larger community, are willing and able to volunteer their expertise, we may create an updated lesson derived from the original.
In accordance with our [CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en) licensing, this derivative will conspicuously attribute the creator of the original lesson, as well as the names of any contributors who aided in the production of the new lesson.

Whether or not a new derivative is created, the following steps will be taken with the retired lesson:

1. The lesson will be moved from `https://programminghistorian.org/lesson/LESSON-TITLE` TO `https://programminghistorian.org/lesson/retired/LESSON-TITLE`. A redirect will be established, so any links to the original URL will seamlessly point the user to the new URL.

2. Once retired, the lesson will no longer appear in the directory of lessons, and it will be removed from the Twitter announcement stream. In order to remove it from the Twitter stream, editors should consult the Programming Historian Wiki.

3. The following announcement will be added to the top of the retired lesson: 
    <div class="alert alert-warning">{{ site.data.snippets.retired-definition[page.lang] | markdownify }}

## Related Sustainability Guidelines

[Author Guidelines for Writing Sustainably](/author-guidelines#write-sustainably)

[Reviewer Guidelines for Assessing Lesson Sustainability](/reviewer-guidelines#sustainability)

[Editor Guidelines for Fostering Lesson Sustainability](/editor-guidelines#c-sustainability-review)

## Retired Lessons

{% assign retired = site.pages | where: "retired", "true" %}
{% for lesson in retired %}
[{{ lesson.title }}]({{ lesson.url }})
{% endfor %}
