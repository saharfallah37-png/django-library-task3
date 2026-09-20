from django.http import Http404
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .sample_data import books, borrowings, members


def home(request):
    return render(request, "library/home.html")


def book_list(request):
    query = request.GET.get("q", "").strip()

    if query:
        search_text = query.casefold()

        filtered_books = [
            book
            for book in books
            if search_text in book["title"].casefold()
            or search_text in book["author"].casefold()
        ]
    else:
        filtered_books = books

    return render(
        request,
        "library/book_list.html",
        {
            "books": filtered_books,
            "query": query,
        },
    )


def member_list(request):
    return render(
        request,
        "library/member_list.html",
        {"members": members},
    )


def borrow_book(request):
    error = ""
    selected_book_id = ""
    selected_member_id = ""

    if request.method == "POST":
        selected_book_id = request.POST.get("book_id", "")
        selected_member_id = request.POST.get("member_id", "")

        book = next(
            (
                book
                for book in books
                if str(book["id"]) == selected_book_id
            ),
            None,
        )

        member = next(
            (
                member
                for member in members
                if str(member["id"]) == selected_member_id
            ),
            None,
        )

        if book is None:
            error = "لطفاً یک کتاب معتبر انتخاب کنید."

        elif member is None:
            error = "لطفاً یک عضو معتبر انتخاب کنید."

        elif not book["available"] or any(
            borrowing["book_id"] == book["id"]
            and borrowing["returned_at"] is None
            for borrowing in borrowings
        ):
            error = "این کتاب قبلاً امانت داده شده است."

        else:
            borrowings.append(
                {
                    "book_id": book["id"],
                    "member_id": member["id"],
                    "borrowed_at": timezone.localdate().isoformat(),
                    "returned_at": None,
                }
            )

            book["available"] = False
            book["borrow_count"] += 1

            return redirect("book_list")

    available_books = [
        book for book in books if book["available"]
    ]

    return render(
        request,
        "library/borrow_book.html",
        {
            "books": available_books,
            "members": members,
            "error": error,
            "selected_book_id": selected_book_id,
            "selected_member_id": selected_member_id,
        },
    )


@require_POST
def return_book(request, book_id):
    book = next(
        (book for book in books if book["id"] == book_id),
        None,
    )

    if book is None:
        raise Http404("کتاب پیدا نشد.")

    active_borrowing = next(
        (
            borrowing
            for borrowing in borrowings
            if borrowing["book_id"] == book_id
            and borrowing["returned_at"] is None
        ),
        None,
    )

    if active_borrowing is not None:
        active_borrowing["returned_at"] = (
            timezone.localdate().isoformat()
        )
        book["available"] = True

    return redirect("book_list")

def member_history(request, member_id):
    member = next(
        (
            member
            for member in members
            if member["id"] == member_id
        ),
        None,
    )

    if member is None:
        raise Http404("عضو پیدا نشد.")

    books_by_id = {
        book["id"]: book
        for book in books
    }

    active_borrowings = []
    returned_borrowings = []

    for borrowing in borrowings:
        if borrowing["member_id"] != member_id:
            continue

        book = books_by_id.get(borrowing["book_id"])

        history_item = {
            "book_title": (
                book["title"]
                if book is not None
                else "کتاب پیدا نشد"
            ),
            "borrowed_at": borrowing["borrowed_at"],
            "returned_at": borrowing["returned_at"],
        }

        if borrowing["returned_at"] is None:
            active_borrowings.append(history_item)
        else:
            returned_borrowings.append(history_item)

    return render(
        request,
        "library/history.html",
        {
            "member": member,
            "active_borrowings": active_borrowings,
            "returned_borrowings": returned_borrowings,
        },
    )

def statistics(request):
    total_books = len(books)
    total_members = len(members)

    available_books = sum(
        1 for book in books if book["available"]
    )

    borrowed_books = total_books - available_books

    most_borrowed_book = max(
        books,
        key=lambda book: book["borrow_count"],
        default=None,
    )

    if (
        most_borrowed_book is not None
        and most_borrowed_book["borrow_count"] == 0
    ):
        most_borrowed_book = None

    return render(
        request,
        "library/statistics.html",
        {
            "total_books": total_books,
            "total_members": total_members,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "most_borrowed_book": most_borrowed_book,
        },
    )