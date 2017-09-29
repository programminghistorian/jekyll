---
title: Archiving Policy
layout: blank
---

# Archiving Policy

The Programming Historian editors do their best to maintain lessons as minor issues inevitably arise. 
However, as time passes, changes to either the underlying technologies or principles used by a given lesson can become so substantial that users will no longer be able to successfully complete the lesson.
In these situations, the _Programming Historian_ editorial team may decide to "archive" a lesson: keeping the page published, but removing it from our directory of active lessons and adding a warning to the top of the page noting that not all elements of the lesson may be working as originally intended.

We do not archive lessons lightly.
If the editorial team begins to receive reports about problems with a lesson, we will investigate the problem and take steps to address it.
Often, we will decide it is not necessary to archive the lesson:

- In cases where minor fixes are easily done, such as correcting the formatting of a lesson, or changing one or two broken URLs, we will generally do so.
- In cases where new methods for a task have emerged that may be preferred to the methods discussed in a lesson, but the original technology for a lesson still works and is available, we will **not** archive the lesson. The lesson may still prove a useful learning tool and a snapshot into the techniques of digital history when it was published

However, if it is clear that systemic changes to text, code, and/or figures are necessary, of a scale that would require complete re-testing of the entire lesson, then we will open a public issue to discuss the possibility of archiving the lesson between all the members of the editorial team.

In cases where members of the editorial team, or members of the larger community, are willing and able to volunteer their expertise, we may create an updated lesson derived from the original.
In accordance with our [CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en) licensing, this derivative will conspicuously attribute the creator of the original lesson, as well as the names of any contributors who aided in the production of the new lesson.

Whether or not a new derivative is created, the following steps will be taken with the archived lesson:

1. The lesson will be moved from `https://programminghistorian.org/lesson/LESSON-TITLE` TO `https://programminghistorian.org/lesson/archived/LESSON-TITLE`. A redirect will be established, so any links to the original URL will seamlessly point the user to the new URL.

2. The following announcement will be added to the top of the archived lesson:
    <div class="alert alert-warning">{{ site.data.snippets.deprecated[page.lang] }}</div>

3. Once archived, the lesson will no longer appear in the directory of lessons.
