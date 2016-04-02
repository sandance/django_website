from django import template
from django.db.models import Count
register = template.Library()

from ..models import Post
# simple tag process the data and returns a string
@register.simple_tag
def total_posts():
    return Post.published.count()

# inclustion tag process

@register.inclusion_tag('blog/post/latest.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
"""
 assignment tags
 assignments tags are like simple tags but they store the
 result in a given variables
"""

@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


"""
We are going to create a custom filter to be able to use markdown
syntax in our blog posts and then convert the post contents to HTML in the templates
"""
"""
from django.utils.safestring import mark_safe
import markdown

@register.filter(name='markdown')
def markdown_format(text):
    #We use the mark_safe function provided by Django to mark the result as safe HTML to be rendered in the template
    return mark_safe(markdown.markdown(text))

"""