import json
import random

from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer, CommentsUndetailedSerializer
from .models import Post, Comment

"""
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""
class PostCreationView(CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = (AllowAny, )


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    # permission_classes = (AllowAny,)

    def get_queryset(self):
        post_name = self.kwargs['post_name']
        return Comment.objects.filter(post__title=post_name)

class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        post_name = self.kwargs['post_name']
        return Comment.objects.filter(post__title=post_name)

    def create(self, *args, **kwargs):
        post_comment = Comment.objects.create(user=self.request.user)
        post_comment.content = CommentSerializer(self.request.data["content"])
        post_name = self.kwargs['post_name']
        post = Post.objects.get(title=post_name)
        post_comment.post.id = post.id
        post_comment.save()


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class CreateCommentsView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsUndetailedSerializer
"""
END OF:
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""

# #posts list
def post_list_view(request):
    posts = Post.objects.all()
    serialized = PostDetailSerializer(posts, many=True).data
    posts_json_string = json.dumps(serialized)
    return render(request, 'views/blog.html', { 'posts' : posts_json_string})


def post_list(request):
    posts = Post.objects.all()
    posts_quantity = posts.count()
    if type(posts_quantity/12) == type(1.6):
        page_numbers = int(posts_quantity/12)  + 1
    else:
        page_numbers = int(posts_quantity/12)


    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    serialized = PostSerializer(posts, many=True).data
    post_json_string = json.dumps(serialized)

    page_data = {"number_of_pages" : page_numbers, "current_page" : page}
    json_page_data = json.dumps(page_data)
    context = {
        'posts' : post_json_string,
        'pageData' : json_page_data,
    }
    return render(request, 'views/blog.html', context)




def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    serialized_post = PostDetailSerializer(post).data
    post_json_string = json.dumps(serialized_post)

    posts = Post.objects.all()

    latest_posts = posts.order_by("-pk")[:5]
    serialized_latest_post = PostDetailSerializer(latest_posts, many=True).data
    json_latest_string = json.dumps(serialized_latest_post)

    random_posts = random.sample(list(posts), 5)
    serialized_random_post = PostDetailSerializer(random_posts, many=True).data
    json_random_string = json.dumps(serialized_latest_post)



    if request.method == "POST":
        post = Post.objects.get(slug=slug)
        username = request.POST.get("username", "")
        content = request.POST.get("content", "")
        if username and content:
            comment = Comment.objects.create(
                username=username,
                content=content,
                post=post,
            )
            redirect_url = reverse("blog:post-detail", kwargs={"slug" : slug})
            data = {
                'msg' :  "نظر شما با موفقیت ثبت شد",
                "redirect_url" : redirect_url,
            }
            return JsonResponse(data, safe=False)
        else:
            redirect_url = reverse("blog:post-detail", kwargs={"slug" : slug})
            data = {
                'msg' : "لطفا فرم را درست وارد کنید",
                "redirect_url" : redirect_url,
            }
            return JsonRespone(data, safe=False)

    context = {
        'post' : post_json_string,
        'random_posts' : json_random_string,
        'latest_posts' : json_latest_string,
    }
    return render(request, 'views/singleBlogPost.html', context)


def post_by_category(request, name):
    posts = Post.objects.filter(categories__title=name)
    sered_post = PostDetailSerializer(posts, many=True).data
    json_post = json.dumps(sered_post)

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts" : json_post,
    }

    return render(request, "views/blog.html", context)
