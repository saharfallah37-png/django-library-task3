books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True,
        "borrow_count": 2,
    },
    {
        "id": 2,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
        "borrow_count": 5,
    },
    {
        "id": 3,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "year": 1999,
        "available": False,
        "borrow_count": 3,
    },
]


members = [
    {
        "id": 1,
        "name": "Ali",
        "email": "ali@example.com",
    },
    {
        "id": 2,
        "name": "Sara",
        "email": "sara@example.com",
    },
    {
        "id": 3,
        "name": "Reza",
        "email": "reza@example.com",
    },
]


borrowings = [
    {
        "book_id": 3,
        "member_id": 1,
        "borrowed_at": "2026-09-05",
        "returned_at": None,
    },
    {
        "book_id": 1,
        "member_id": 1,
        "borrowed_at": "2026-08-10",
        "returned_at": "2026-08-17",
    },
    {
        "book_id": 2,
        "member_id": 2,
        "borrowed_at": "2026-08-20",
        "returned_at": "2026-08-28",
    },
    {
        "book_id": 3,
        "member_id": 3,
        "borrowed_at": "2026-08-01",
        "returned_at": "2026-08-09",
    },
]