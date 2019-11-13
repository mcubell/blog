#! python
side_index = open('/home/matt/Kickstart Frontend/homework/homework_2/blog//templates/side_index.html').read() 
top_index = open("/home/matt/Kickstart Frontend/homework/homework_2/blog//templates/top_index.html").read()
content_index = open("/home/matt/Kickstart Frontend/homework/homework_2/blog//content/content_index.html").read()
index = side_index + top_index + content_index
open("/home/matt/Kickstart Frontend/homework/homework_2/blog/index.html","w").write(index)

side_blog = open("/home/matt/Kickstart Frontend/homework/homework_2/blog/templates/side_blog-post_Cubell.html").read()
blog_post_Cubell = open("/home/matt/Kickstart Frontend/homework/homework_2/blog/content/blog-post_Cubell_content.html").read()
built_blog_post = side_blog + blog_post_Cubell
open("/home/matt/Kickstart Frontend/homework/homework_2/blog/built_blog_post.html","w").write(built_blog_post)

side_about = open("/home/matt/Kickstart Frontend/homework/homework_2/blog/templates/side_blog-post_Cubell.html").read()
content_about = open("/home/matt/Kickstart Frontend/homework/homework_2/blog/content/content_about.html").read()
built_about = side_about + content_about
open("/home/matt/Kickstart Frontend/homework/homework_2/blog/built_about.html","w").write(built_about)

side_blog_list = open("/home/matt/Kickstart Frontend/homework/homework_2/blog/templates/side_blog-list_Cubell.html").read()
side_blog_list_content =open("/home/matt/Kickstart Frontend/homework/homework_2/blog/content/blog-list_Cubell_content.html").read()
built_blog_list = side_blog_list + side_blog_list_content
open("/home/matt/Kickstart Frontend/homework/homework_2/blog/built_blog-list.html","w").write(built_blog_list)
