import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from topic.models import Topic
from user.models import UserProfile
from tools.login_decorator import login_check, get_user_by_request


@login_check("POST", "DELETE")
def topics(request, username=None):
    """
        文章模块路由
            GET:
                获取用户博客列表
                    /v1/topics/<username>
                        访问者是博主，显示所有博客列表
                            根据查询参数 ?category=xx, 做分类筛选
                        访问者是其他人 或 未登录用户 只显示 limit 值为 public 的博客列表
                获取博客内容
                    /v1/topics/<username>?....
            POST: 发表 blog
                /v1/topics/<username>
    :param username: 所访问的博客 博主 用户名
    :param request:
    :return:
    """

    if request.method == 'GET':

        # 获取博客作者
        authors = UserProfile.objects.filter(username=username)
        if not authors:
            res = {"code": 307, "error": "The current author is not existed"}
            return JsonResponse(res)
        author = authors[0]

        # 获取访问者
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username

        category = request.GET.get('category')
        if visitor_name == username:
            # 拿所有博客
            #   分类筛选
            #   /v1/topics/username?category=tec/no-tec
            if category in ('tec', 'no-tec'):
                view_topics = Topic.objects.filter(author_id=username, category=category)
            else:
                view_topics = Topic.objects.filter(author_id=username)
        else:
            # 拿到 public 权限的博客
            #   分类筛选
            if category in ('tec', 'no-tec'):
                view_topics = Topic.objects.filter(author_id=username, limit='public', category=category)
            else:
                view_topics = Topic.objects.filter(author_id=username, limit='public')

        res = make_topics_res(author, view_topics)

        return JsonResponse(res)

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
    elif request.method == "DELETE":
        # /v1/topics/<username>?t_id=1111
        id_ = request.GET.get("t_id")
        if not id_:
            result = {"code": 308, "error": "You can't do it !!"}
            return JsonResponse(result)

        try:
            topic = Topic.objects.get(id=id_)
        except Exception as e:
            print("--delete blog -- db error...")
            result = {"code": 309, "error": "-- delete blog - topic not exist"}
            return JsonResponse(result)

        topic.delete()
        return JsonResponse({'code': 200})


def make_topics_res(author, author_topics):
    res = {"code": 200, "data": {}}
    topics_res = []

    for topic in author_topics:
        dict_topic = dict()
        dict_topic['id'] = topic.id
        dict_topic['title'] = topic.title
        dict_topic['category'] = topic.category
        dict_topic['create_time'] = topic.create_time.strftime("%Y-%m-%d %H:%M:%S")
        dict_topic['introduce'] = topic.introduce
        dict_topic['author'] = author.nickname

        topics_res.append(dict_topic)

    res['data']['topics_res'] = topics_res
    res['data']['nickname'] = author.nickname

    return res
