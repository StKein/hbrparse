import logging
import requests
from celery import shared_task
from datetime import datetime
from django.utils.timezone import make_aware
from lxml import html
from prser.models import Post
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def parseHabr():
    logging.info('Started parsing')

    try:
        req = requests.get('https://habr.com/ru/top/')
    except Exception as e:
        logging.critical('Could not get response from site: {}'.format(e))
        return
    
    try:
        root = html.fromstring(str(req.content.decode(req.encoding)))
    except Exception as e:
        logging.critical('Could not get HTML from response: {}'.format(e))
        return
    
    try:
        links = root.xpath('//div[@class="posts_list"]')[0].find_class('post__title_link')
    except Exception as e:
        # If this happens, either page is incorrect or Habr changed content list template
        logging.critical('Could not get posts list from response')
        return
    
    saved_posts = 0
    logging.info('Found {} posts'.format(len(links)))
    for link in links:
        link = link.get('href')
        # No need to save duplicates
        if len(Post.objects.filter(link=link)) > 0:
            continue
        req = requests.get(link)
        try:
            root = html.fromstring(str(req.content.decode(req.encoding)))
            post = Post()
            post.title = root.find_class('post__title-text')[0].text
            post.link = link
            post.text = ''.join(root.find_class('post__text')[0].itertext())
            post.time = make_aware(datetime.strptime(
                root.find_class('post__time')[0].get('data-time_published'),
                '%Y-%m-%dT%H:%MZ'
            ))
            post.save()
            saved_posts += 1
        except Exception as e:
            logging.error('Could not save post from {}: {}'.format(link, e))
    logging.info('Finished. Saved {} posts'.format(saved_posts))

@shared_task
def testCel(**kwargs):
    logging.info('testcel task ran')
    logger.info('testcel task ran')
    print("Testing!")