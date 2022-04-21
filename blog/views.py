from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from blog.serializers import BlogSerializer
from blog.models import Blog
from rest_framework.response import Response
from blog.utils import http_status

# Create your views here.


class ListBlogAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):

        try:
            model = Blog.objects.filter()
            serializer = BlogSerializer(model, many=True)
            if request.GET.get('limit') and request.GET.get('offset'):

                page = self.paginate_queryset(serializer.data)
            else:
                page = serializer.data

            status_code = http_status.OK
            response = {
                'success': True,
                'status_code': status_code,
                'message': 'Blogs Data fetched successfully',
                'count': model.count(),
                'data': page
            }

        except Exception as e:
            status_code = http_status.OK
            response = {
                'success': False,
                'status_code': http_status.BAD_REQUEST,
                'message': "Something is Wrong.",
                'error': str(e)
            }

        return Response(response, status=status_code)


class CreateBlogAPIView(CreateAPIView):
    """This endpoint allows for creation of a Blog"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def post(self, request, *args, **kwargs):

        try:
            blog_obj = self.create(request, *args, **kwargs)
            status_code = http_status.OK
            response = {
                'success': True,
                'status_code': status_code,
                'message': "blog successfully registered."
            }

        except Exception as e:
            status_code = http_status.OK
            response = {
                'success': False,
                'status_code': http_status.BAD_REQUEST,
                'message': "Something is Wrong.",
                'error': str(e)
            }

        return Response(response, status=status_code)


class UpdateBlogAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Blog by passing in the id of the Blog to update"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def put(self, request, pk):
        try:
            model = Blog.objects.get(blogID=pk, isDeleted=False)
            serializer = BlogSerializer(model, data=request.data)
            if serializer.is_valid() == True:
                serializer.save()
                status_code = http_status.OK
                response = {
                    'success': True,
                    'status_code':  status_code,
                    'message': 'Blogs details Updated Successfully',
                    'data': serializer.data
                }
            else:
                status_code = http_status.OK
                response = {
                    'success': False,
                    'status_code': http_status.BAD_REQUEST,
                    'message': 'something is wrong',
                }
        except Exception as e:
            status_code = http_status.OK
            response = {
                'success': False,
                'status_code': http_status.BAD_REQUEST,
                'message': "Something is Wrong.",
                'error': str(e)
            }
        return Response(response, status=status_code)


class DeleteBlogAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Blog from the database"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def delete(self, request, pk):
        try:
            model = Blog.objects.get(blogID=pk, isDeleted=False)
            model.isDeleted = True
            model.save()
            status_code = http_status.OK
            response = {
                "success": True,
                "message": "Data Deleted Successfully.",
                "status_code": status_code
            }

        except Exception as e:
            status_code = http_status.OK
            response = {
                "success": False,
                "status_code": http_status.BAD_REQUEST,
                'message': "Something is Wrong.",
                'error': str(e)
            }

        return Response(response, status=status_code)
