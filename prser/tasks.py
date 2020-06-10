import requests
from lxml import html
from .models import Post

def parseHabr():
    req = requests.get("https://habr.com/ru/top/")
    root = html.fromstring(str(req.content.decode(req.encoding)))
    links = root.xpath('//div[@class="posts_list"]')[0].find_class("post__title_link")

    for link in links:
        link = link.get('href')
        if len(Post.objects.filter(link=link)) > 0:
            continue
        req = requests.get(link)
        try:
            root = html.fromstring(str(req.content.decode(req.encoding)))
            post = Post()
            post.title = root.find_class('post__title-text')[0].text
            post.link = link
            post.text = ''.join(root.find_class('post__text')[0].itertext())
            post.save()
        except BaseException:
            continue