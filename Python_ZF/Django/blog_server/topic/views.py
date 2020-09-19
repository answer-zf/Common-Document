import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from topic.models import Topic
from user.models import UserProfile
from tools.login_decorator import login_check


@login_check("POST")
def topics(request, username=None):
    """
        文章模块路由
            GET: 获取用户数据
                /v1/topics/<username> 获取用户全部博客数据
            POST: 发表 blog
                /v1/topics/<username>
    :param username:
    :param request:
    :return:
    """

    if request.method == 'GET':
        print(username)
        # try:
        user = UserProfile.objects.get(username=username)
        # except UserProfile.DoesNotExist:
        #     user = None
        print(user)
        if not user:
            result = {"code": 307, "error": "user not exist"}
            return JsonResponse(result)

        user_topics = Topic.objects.filter(author=user)

        if not user_topics.exists():
            result = {"code": 200, "data": {}}
            return JsonResponse(result)

        topics_ = []
        nickname = user.nickname
        for topic in user_topics:
            dict_topic = {
                "id": topic.id,
                "title": topic.title,
                "category": topic.category,
                "create_time": topic.create_time,
                "content": topic.content,
                "introduce": topic.introduce,
                "author": nickname
            }
            topics_.append(dict_topic)

        result = {"code": 200, "data": {"nickname": nickname, "topics": topics_}}
        return JsonResponse(result)

    elif request.method == "POST":
        user = request.user
        json_str = request.body

        if not json_str:
            # 判断字符串是否为空
            result = {"code": 302, "error": "pl transfer json.."}
            return JsonResponse(result)

        json_obj = json.loads(json_str)

        title = json_obj.get('title')

        if not title:
            # 文章标题不存在
            result = {"code": 303, "error": "pl. transfer title"}
            return JsonResponse(result)

        content = json_obj.get('content')

        # 生成文章简介
        content_text = json_obj.get('content_text')
        introduce = content_text[:30]  # 数据库存三十个中文

        limit = json_obj.get('limit')

        if limit not in ("public", "private"):
            # 权限 必须在 public private
            result = {"code": 304, "error": "limit error.."}
            return JsonResponse(result)

        category = json_obj.get('category')

        if category not in ("tec", "no-tec"):
            # 权限 必须在 public private
            result = {"code": 305, "error": "category error.."}
            return JsonResponse(result)

        now = datetime.datetime.now()

        try:
            Topic.objects.create(
                title=title,
                category=category,
                limit=limit,
                content=content,
                introduce=introduce,
                create_time=now,
                modified_time=now,
                author=user
            )
        except Exception as e:
            print('Topic create error is %s' % e)
            result = {"code": 306, "error": "The create fail!!!"}
            return JsonResponse(result)

        result = {"code": 200, 'username': user.username}
        return JsonResponse(result)

    elif request.method == "PUT":
        pass

    return JsonResponse({'code': 200, 'data': 'this is text'})
