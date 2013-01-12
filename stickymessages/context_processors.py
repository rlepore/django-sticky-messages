from stickymessages.models import Message

def latest_sticky_message(request):
    """
    Retrieve the latest system message from the database and add it to the request
    context.
    """
    return {'sticky_message': Message.objects.get_latest_active() }
    