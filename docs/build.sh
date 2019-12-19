#!/bin/bash

cat ./templates/side_index.html ./templates/top_index.html ./content/content_index.html > ./index.html

cat ./templates/side_blog_post_Cubell.html ./content/blog_post_Cubell_content.html > ./built_blog_post.html

cat ./templates/side_about.html ./content/content_about.html>./built_about.html

cat ./templates/side_blog_list_Cubell.html ./content/blog_list_Cubell_content.html>./built_blog_list.html
