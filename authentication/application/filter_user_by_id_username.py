from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def get_user_by_query_name(user_id=None, username=None):
    if user_id:
        user = get_object_or_404(User, id=user_id)
    elif username:
        user = get_object_or_404(User, username=username)
    else:
        return None
    return user