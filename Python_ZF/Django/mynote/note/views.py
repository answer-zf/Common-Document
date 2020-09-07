from django.shortcuts import render


# Create your views here.
def note_list(request):
    """
        笔记列表
    """
    page_name = 'Note_List'
    return render(request, 'list.html', locals())
