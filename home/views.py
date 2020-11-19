from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def post_list(request):
    new_post = Post.objects.all()
    serializer = PostSerializers(new_post, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')



def post_detail(request, pk):
    new_post = Post.objects.get(id=pk)
    serializer = PostSerializers(new_post)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


# def post_detail(request):
#     new_post = Post.objects.get(id=1)
#     print(new_post)
#     serializer = PostSerializers(new_post)
#     print(serializer)
#     print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     print(json_data)
#     return HttpResponse(json_data, content_type = 'application/json')




    
