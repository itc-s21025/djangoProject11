from django.urls import path
from Ninjin import views

urlpatterns = [
    path("new/", views.ogiri_theme_new, name="theme_new"),
    path("new_reverse/", views.ogiri_theme_new_reverse, name="theme_new_reverse"),
    path("new_narikiri/", views.ogiri_theme_new_narikiri, name="theme_new_narikiri"),
    path("new_image/", views.ImagePostView.as_view(), name="theme_new_image"),
    path("category/", views.category, name="category"),
    path("answer_category", views.category_answer, name="answer_category"),
    path("<int:category_id>/", views.answer_list, name="answer_list"),
    path("detail/<int:post_id>/", views.answer_detail, name="answer_detail"),
    path("answer/<int:post_id>/", views.answer_new, name="answer_new"),
    path('like_for_post/', views.like_for_post, name='like_for_post'),
    path("tested/<int:pk>/", views.PostDetail.as_view(), name="tested"),
    path('like_for_comment/', views.like_for_comment, name='like_for_comment'),
]
