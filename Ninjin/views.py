from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import CreateView
from Ninjin.models import Post, Answer, LikeForComment, LikeForPost
from Ninjin.forms import OgiriThemeForm, OgiriThemeImageForm, AnswerForm, ImagePostForm
from django.contrib import messages
# Create your views here.

def top(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "ningins/top.html", context)

def category(request):
    return render(request, 'ningins/theme_category.html')

def category_answer(request):
    return render(request, 'ningins/answer_category.html')

def answer_list(request, category_id):

    posts = Post.objects.filter(
        post_category=category_id).order_by('-posted_at')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)

    context = {"orderby_records": pages}
    return render(request, "ningins/answer_list.html", context)

def answer_list_image(request, category_id):

    posts = Post.objects.filter(
        post_category=category_id).order_by('-posted_at')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)

    context = {"orderby_records": pages}

    return render(request, "ningins/answer_list_image.html", context)


def theme_success(request):
    return render(request, 'ningins/success_theme.html')

def answer_success(request):
    return (render(request, 'ningins/success_answer.html'))

@login_required
def ogiri_theme_new(request):
    initial_values = {"post_category": 1}
    if request.method == "POST":
        form = OgiriThemeForm(request.POST,initial_values)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.post_by_user = request.user
            theme.save()
            messages.add_message(request, messages.SUCCESS,
                                 "お題を作成しました。")
            return redirect(theme_success)
        else:
            messages.add_message(request, messages.ERROR,
                                 "お題の作成に失敗しました。")
    else:
        form = OgiriThemeForm(initial_values)
    return render(request, "ningins/theme_new.html", {'form': form})

@login_required
def ogiri_theme_new_reverse(request):
    initial_values = {"post_category": 3}
    if request.method == "POST":
        form = OgiriThemeForm(request.POST,initial_values)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.post_by_user = request.user
            theme.save()
            messages.add_message(request, messages.SUCCESS,
                                 "お題を作成しました。")
            return redirect(answer_detail, post_id=theme.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "お題の作成に失敗しました。")
    else:
        form = OgiriThemeForm(initial_values)
    return render(request, "ningins/theme_new_reverse.html", {'form': form})

@login_required
def ogiri_theme_new_narikiri(request):
    initial_values = {"post_category": 4}
    if request.method == "POST":
        form = OgiriThemeForm(request.POST,initial_values)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.post_by_user = request.user
            theme.save()
            messages.add_message(request, messages.SUCCESS,
                                 "お題を作成しました。")
            return redirect(answer_detail, post_id=theme.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "お題の作成に失敗しました。")
    else:
        form = OgiriThemeForm(initial_values)
    return render(request, "ningins/theme_new_narikiri.html", {'form': form})

@method_decorator(login_required, name='dispatch')
class ImagePostView(CreateView):
    form_class = ImagePostForm

    template_name = "ningins/theme_new_image.html"

    success_url = reverse_lazy('top')
    def get_initial(self):
        initial = super().get_initial()
        initial["post_category"] = 2
        return initial

    def form_valid(self, form):
        theme = form.save(commit=False)
        theme.post_by_user = self.request.user
        theme.save()
        return super().form_valid(form)

@login_required
def ogiri_theme_new_image(request):
    initial_values = {"post_category": 2}
    if request.method == "POST":
        form = OgiriThemeImageForm(request.POST,initial_values, request.FILES)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.post_by_user = request.user
            theme.save()
            messages.add_message(request, messages.SUCCESS,
                                 "お題を作成しました。")
            return redirect(answer_detail, post_id=theme.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "お題の作成に失敗しました。")
    else:
        form = OgiriThemeImageForm(initial_values, request.FILES)
    return render(request, "ningins/theme_new_image.html", {'form': form})

@login_required
def ogiri_theme_new_kaku(request):
    initial_values = {"post_category": 5}
    if request.method == "POST":
        form = OgiriThemeForm(request.POST,initial_values)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.post_by_user = request.user
            theme.save()
            messages.add_message(request, messages.SUCCESS,
                                 "お題を作成しました。")
            return redirect(answer_detail, post_id=theme.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "お題の作成に失敗しました。")
    else:
        form = OgiriThemeForm(initial_values)
    return render(request, "ningins/theme_new_kaku.html", {'form': form})


@login_required
def answer_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    answers = Answer.objects.filter(answer_to=post_id).all()
    answer_form = AnswerForm()

    return render(request, "ningins/answer_new.html", {
        'posts': post,
        'answers': answers,
        'answer_form': answer_form,
    })


@login_required
def answer_new(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.answer_to = post
        answer.answer_by = request.user
        answer.save()
        messages.add_message(request, messages.SUCCESS,
                             "コメントを投稿しました。")
    else:
        messages.add_message(request, messages.ERROR,
                             "コメントの投稿に失敗しました。")
    return redirect('success_answer',)

class PostDetail(generic.DetailView):
    template_name = 'ningins/detail_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_post_count = self.object.likeforpost_set.count()
        context['like_for_post_count'] = like_for_post_count
        # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_post = False
        if not self.request.user.is_anonymous:
            if self.object.likeforpost_set.filter(user=self.request.user).exists():
                is_user_liked_for_post = True
        context['is_user_liked_for_post'] = is_user_liked_for_post


        # {'pk':{'count':コメントに対するイイネ数,'is_user_like_for_comment':bool},}という辞書を追加していく
        d = {}
        for comment in self.object.answer_set.all():
            like_for_comment_count = comment.likeforcomment_set.count()
            is_user_liked_for_comment = False
            if not self.request.user.is_anonymous:
                if comment.likeforcomment_set.filter(like_for_user_id=self.request.user).exists():
                    is_user_liked_for_comment = True
            d[comment.pk] = {'count': like_for_comment_count, 'is_user_liked_for_comment': is_user_liked_for_comment}

        context['comment_like_data'] = d

        return context

def like_for_post(request):
    post_pk = request.POST.get('post_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    post = get_object_or_404(Post, pk=post_pk)
    like = LikeForPost.objects.filter(target=post, user=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=post, user=request.user)
        context['method'] = 'create'

    context['like_for_post_count'] = post.likeforpost_set.count()

    return JsonResponse(context)

def like_for_comment(request):
    comment_pk = request.POST.get('comment_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    comment = get_object_or_404(Answer, pk=comment_pk)
    like = LikeForComment.objects.filter(like_for_to=comment, like_for_user=request.user)
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(like_for_to=comment, like_for_user=request.user)
        context['method'] = 'create'

    context['like_for_comment_count'] = comment.likeforcomment_set.count()

    return JsonResponse(context)

class ImageDetail(generic.DetailView):
    template_name = 'ningins/detail_image_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_post_count = self.object.likeforpost_set.count()
        context['like_for_post_count'] = like_for_post_count
        # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_post = False
        if not self.request.user.is_anonymous:
            if self.object.likeforpost_set.filter(user=self.request.user).exists():
                is_user_liked_for_post = True
        context['is_user_liked_for_post'] = is_user_liked_for_post


        # {'pk':{'count':コメントに対するイイネ数,'is_user_like_for_comment':bool},}という辞書を追加していく
        d = {}
        for comment in self.object.answer_set.all():
            like_for_comment_count = comment.likeforcomment_set.count()
            is_user_liked_for_comment = False
            if not self.request.user.is_anonymous:
                if comment.likeforcomment_set.filter(like_for_user_id=self.request.user).exists():
                    is_user_liked_for_comment = True
            d[comment.pk] = {'count': like_for_comment_count, 'is_user_liked_for_comment': is_user_liked_for_comment}

        context['comment_like_data'] = d

        return context

