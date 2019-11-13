#!/bin/bash

cat ./templates/side_index.html ./templates/top_index.html ./content/content_index.html > ./builds/built_index.html

cat ./templates/side_blog-post_Cubell.html ./content/blog-post_Cubell_content.html > ./builds/built_blog-post.html

cat ./templates/side_about.html ./content/content_about.html>./builds/built_about.html

cat ./templates/side_blog-list_Cubell.html ./content/blog-list_Cubell_content.html>./builds/built_blog-list.html
