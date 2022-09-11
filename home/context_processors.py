from users.models import Notification


def get_notifications(request):
    
    try:
        user = request.user
        notification = Notification.objects.filter(user=user)
        count = notification.count()
    except Exception:
        notification = ""
        count = 0

    return {
        'noti_count': count,
        'noti_data' : notification
    } 