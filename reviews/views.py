from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe
from .models import Review,Comment
from .forms import ReviewForm, CommentForm
from Restaurant.models import Restaurant
# Create your views here.

@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user 
            review.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('reviews:index')
    else: 
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/form.html', context=context)

def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comments': review.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user: 
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('reviews:detail', review.pk)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            'review_form': review_form
        }
        return render(request, 'reviews/form.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('reviews:detail', review.pk)

@login_required
def comment_create(request, pk):
    print(request.POST)
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
        return JsonResponse(context)
@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect("reviews:detail", pk)

@login_required
def like(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user in review.like_users.all(): 
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': review.like_users.count()}
    return JsonResponse(context)

@login_required
def review_create(request, pk):
    info = Restaurant.objects.get(pk=pk)
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new = review_form.save(commit=False)
            new.Restaurant_id = info.pk
            new.user = request.user
            new.save()
            return redirect("Restaurant:detail", info.pk)
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/form.html", context=context)

def review_detail(request,Restaurant_pk,review_pk):
    info = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    context = {
        "info": info,
        "comment_form": comment_form,
        "comments": info.comment_set.all(),
    }
    return render(request, "reviews/review_detail.html", context)