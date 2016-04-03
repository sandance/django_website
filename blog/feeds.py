from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    """
    item_tile() and item_description() methods receive
    each object returned by items() and returns the title
    and description for each item
    """
    def item_title(self, item):
        return item.title
    # We use the truncatewords built in template filter
    # to build the description of the blog post with the first
    # 30 words
    def item_description(self, item):
        return truncatewords(item.body, 30)
