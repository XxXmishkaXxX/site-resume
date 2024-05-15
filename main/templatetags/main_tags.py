from django import template

register = template.Library()


@register.filter
def remove_middle_name(full_name):
    return ' '.join(full_name.split()[0:2])


@register.filter
def get_name(full_name):
    return full_name.split()[1]


@register.filter
def get_name2(full_name):
    return full_name.split()[0]


@register.filter
def get_middle_name(full_name):
    return full_name.split()[2]

@register.filter
def is_liked_by(post, user):
    return bool(post.like_for_post.filter(user_profile=user.userprofile))