---
layout: default
title: Short Stories
permalink: /shortstories
---

## Short Stories

Creative writings in the form of Short Stories.

<ul>
  {% for shortstories in site.shortstories %}
  <li><a href="{{ shortstories.url }}" class="shortstories-preview">{{ shortstories.title }}</a></li>
  {% endfor %}
</ul>


<form>
  <!-- Form stuff -->
</form>