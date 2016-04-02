from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """
    changefreq and priority represents
    change of frequency of your posts and their
    relevance in your website
    """
    changefreq = 'weekly'
    priority = 0.9

    # items mod returns the queryset of objects
    # to include in  this sitemap
    def items(self):
        return Post.published.all()

    # it receives each object returned by items
    # and returns last time the object was modified
    def lastmod(self,obj):
        return obj.publish
