---
layout: default
title: Essays
permalink: /essay/
---

## Essays (Substack)

Crafted thoughts on technology and life.

<ul>
  {% for essay in site.essay %}
  <li><a href="{{ essay.url }}" class="essay-preview">{{ essay.title }}</a></li>
  {% endfor %}
</ul>


<form>
  <!-- Form stuff -->
</form>
