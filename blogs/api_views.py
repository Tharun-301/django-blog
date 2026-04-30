from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer


@api_view(['GET'])
def blog_list_api(request):
    blogs = Blog.objects.filter(status='Published')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list_api(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)