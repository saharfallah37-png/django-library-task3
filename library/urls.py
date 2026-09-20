from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("members/", views.member_list, name="member_list"),
    path("borrow/", views.borrow_book, name="borrow_book"),
    path(
        "return/<int:book_id>/",
        views.return_book,
        name="return_book",
    ),
    path(
        "history/<int:member_id>/",
        views.member_history,
        name="member_history",
    ),
    path(
        "statistics/",
        views.statistics,
        name="statistics",
    ),
]