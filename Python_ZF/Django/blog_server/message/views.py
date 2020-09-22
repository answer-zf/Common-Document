import json
from datetime import datetime

from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.
from message.models import Message
from tools.login_decorator import login_check
from topic.models import Topic


@login_check("POST")
def messages(request, topic_id):
    if request.method == "POST":

        if not topic_id:
            result = {"code": 601, "error": "pl. transfer topic_id"}
            return JsonResponse(result)

        try:
            topic_ = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {"code": 602, "error": "-- post message - select topic for id error is %s" % e}
            return JsonResponse(result)

        user_ = request.user

        str_msg = request.body
        obj_msg = json.loads(str_msg)

        if not obj_msg:
            result = {"code": 603, "error": "-- post message - not transfer JSON"}
            return JsonResponse(result)

        content = obj_msg.get('content')
        parent_id = obj_msg.get('parent_id')

        try:
            Message.objects.create(
                content=content,
                create_time=datetime.now(),
                user=user_,
                topic=topic_,
                parent_id=parent_id
            )
        except Exception as e:
            result = {"code": 604, "error": "-- post message - create message for id error is %s" % e}
            return JsonResponse(result)

        result = {"code": 200, "data": {}}
        result["data"]['content'] = content
        return JsonResponse(result)
