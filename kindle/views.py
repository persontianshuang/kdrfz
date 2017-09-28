from django.shortcuts import render

# Create your views here.

from kindle.models import Mark


from django.http import HttpResponse

from users.models import User
from .models import Book,Mark,Note

from first.read import clip_to_data



# from kindle.serializers import MarkSerializer
#
#
# from rest_framework import generics
# from rest_framework.pagination import PageNumberPagination
#
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 50
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
#     # http://localhost:8000/kindle/?offset=1660&page=3
#
# class MarkList(generics.ListCreateAPIView):
#     queryset = Mark.objects.all()
#     serializer_class = MarkSerializer
#     pagination_class = StandardResultsSetPagination





def year_archive(request):
    # User().objects.filter(id =1)   一个括号坑了我好久
    this_user = User.objects.filter(id =1)[0]
    kindle_mark = clip_to_data('/Users/user/pynew/project/kinde_drf/first/My Clippings.txt')
    for x in kindle_mark:
        print(x)
        book_name = x['book_raw_name']
        q = Book.objects.filter(raw_name=book_name)
        # print(q)
        if q:
            q = q[0]
        else:
            p = Book(
                raw_name = book_name,
                simple_name = x['book_simple_name'],
            )
            p.save()
            q = p
        # print(q.book_raw_name)


        m = Mark(
            user = this_user,
            book_from = q,
            content = x['content'],
            find_page = x['find_page'],
            add_time  = x['read_time']
        )
        m.save()

        if 'note' in x:
            n = Note(
                user = this_user,
                mark_from = m,
                content = x['note'],
                add_time  = x['read_time']
            )
            n.save()

    return HttpResponse("Hello, world. You're at the polls index.")
    # 接下来restful API   获取mark
