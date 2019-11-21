#! python


# def main():
#     side_index = open('./templates/side_index.html').read() 
#     top_index = open("./templates/top_index.html").read()
#     content_index = open("./content/content_index.html").read()
#     index = side_index + top_index + content_index
#     open("./index.html","w").write(index)

#     side_blog = open("./templates/side_blog-post_Cubell.html").read()
#     blog_post_Cubell = open("./content/blog-post_Cubell_content.html").read()
#     built_blog_post = side_blog + blog_post_Cubell
#     open("./built_blog_post.html","w").write(built_blog_post)

#     side_about = open("./templates/side_blog-post_Cubell.html").read()
#     content_about = open("./content/content_about.html").read()
#     built_about = side_about + content_about
#     open("./built_about.html","w").write(built_about)

#     side_blog_list = open("./templates/side_blog-list_Cubell.html").read()
#     side_blog_list_content =open("./content/blog-list_Cubell_content.html").read()
#     built_blog_list = side_blog_list + side_blog_list_content
#     open("./built_blog-list.html","w").write(built_blog_list)

# main()


#! python


def main():
    side_index = open('./templates/side_index.html').read() 
    top_index = open("./templates/top_index.html").read()
    content_index = open("./content/content_index.html").read()
    index = side_index + top_index + content_index
    open("./index.html","w").write(index)

    side_blog = open("./templates/side_blog-post_Cubell.html").read()
    blog_post_Cubell = open("./content/blog-post_Cubell_content.html").read()
    built_blog_post = side_blog + blog_post_Cubell
    open("./built_blog_post.html","w").write(built_blog_post)

    side_about = open("./templates/side_blog-post_Cubell.html").read()
    content_about = open("./content/content_about.html").read()
    built_about = side_about + content_about
    open("./built_about.html","w").write(built_about)

    side_blog_list = open("./templates/side_blog-list_Cubell.html").read()
    side_blog_list_content =open("./content/blog-list_Cubell_content.html").read()
    built_blog_list = side_blog_list + side_blog_list_content
    open("./built_blog-list.html","w").write(built_blog_list)

main()

pages = [
    {
        "filename": "/templates/side_index.html",
        "output": "/docs/index.html",
        "title": "Index",
    },
    {
        "filename": "/templates/top_index.html",
        "output": "/docs/index.html",
        "title": "Index",
    },
    {
        "filename": "/content/content_index.html",
        "output": "/docs/index.html",
        "title": "/Index",
    },
    {
        "filename": "/templates/side_blog-post_Cubell.html",
        "output": "docs/built_blog_post.html",
        "title": "Blog Posts"
    },
    {
        "filename": "/content/side_blog-post_Cubell_content.html",
        "output": "docs/built_blog_post.html",
        "title": "Blog Posts",
    },
    {
        "filename": "/templates/side_blog-post_Cubell.html",
        "output": "/docs/built_blog_post.html",
        "title": "About",
    },
    {
        "filename": "/content/blog-post_Cubell_content.html",
        "output": "/docs/built_blog_post.html",
        "title": "About",
    },
    {
        "filename": "/templates/side_blog-list_Cubell.html",
        "output": "/docs/built_blog-list_Cubell_content.html",
        "title": "Blog List",
    },

        "filename": "/content/blog-list_Cubell_content.html",
        "output": "/docs/built_blog-list.html",
        "title": "Blog List",
    }
]
for page in pages:
    print(pages)