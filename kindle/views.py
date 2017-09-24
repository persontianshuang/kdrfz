from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from users.models import User
from .models import Book,Mark,Note




from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from kindle.models import Mark
from kindle.serializers import MarkSerializer



@csrf_exempt
def mark_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Mark.objects.all()
        print(snippets)
        serializer = MarkSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)





# from first.read import clip_to_data

# def year_archive(request):
#     # User().objects.filter(id =1)   一个括号坑了我好久
#     this_user = User.objects.filter(id =1)[0]
#     kindle_mark = clip_to_data('/Users/user/pynew/project/kinde_drf/first/My Clippings.txt')
#     for x in kindle_mark:
#         print(x)
#         book_name = x['book_raw_name']
#         q = Book.objects.filter(raw_name=book_name)
#         # print(q)
#         if q:
#             q = q[0]
#         else:
#             p = Book(
#                 raw_name = book_name,
#                 simple_name = x['book_simple_name'],
#             )
#             p.save()
#             q = p
#         # print(q.book_raw_name)
#
#
#         m = Mark(
#             user = this_user,
#             book_from = q,
#             content = x['content'],
#             find_page = x['find_page'],
#             add_time  = x['read_time']
#         )
#         m.save()
#
#         if 'note' in x:
#             n = Note(
#                 user = this_user,
#                 mark_from = m,
#                 content = x['note'],
#                 add_time  = x['read_time']
#             )
#             n.save()
#
#     return HttpResponse("Hello, world. You're at the polls index.")
#     # 接下来restful API   获取mark
