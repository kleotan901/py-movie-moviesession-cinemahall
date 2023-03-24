from typing import Optional

from django.shortcuts import get_object_or_404
import init_django_orm  # noqa: F401
import datetime
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: Optional[str] = None) -> MovieSession:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(
            show_time__date=session_date
        )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> MovieSession:
    queryset_session = MovieSession.objects.get(
        id=session_id
    )
    if show_time is not None:
        queryset_session.show_time = show_time
    if movie_id is not None:
        queryset_session.movie_id = movie_id
    if cinema_hall_id is not None:
        queryset_session.cinema_hall_id = cinema_hall_id
    return queryset_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_object_or_404(MovieSession, id=session_id)
    movie_session.delete()
