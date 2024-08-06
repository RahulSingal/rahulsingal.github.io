---
layout: default
title: Blog
permalink: /codingblog
---

## My Blog Posts

Free-flowing blogs written in the first person for various audiences.

<ul>
  {% for post in site.posts %}
  <li><a href="{{ post.url }}" class="post-preview">{{ post.title }}</a></li>
  {% endfor %}
</ul>