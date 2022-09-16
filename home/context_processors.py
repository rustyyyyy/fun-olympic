from users.models import Notification
from home.models import News


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
    

def get_news(request):
    news = News.objects.all().order_by('-id')
    return {'news':news}