from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import MenuResultSerializer, VoteInputSerializer
from . import services


def get_build_version(request) -> int:
    try:
        return int(request.headers.get("Build-Version", 1))
    except (ValueError, TypeError):
        return 1


class VoteView(APIView):
    @extend_schema(request=VoteInputSerializer)
    def post(self, request):
        menu_id = request.data.get("menu_id")
        if not menu_id:
            return Response({"detail": "menu_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = request.user.employee
        except ObjectDoesNotExist:
            return Response({"detail": "User has no employee profile."}, status=status.HTTP_403_FORBIDDEN)

        vote = services.cast_vote(employee, menu_id)
        return Response({"detail": "Vote accepted.", "vote_id": vote.id}, status=status.HTTP_201_CREATED)


class TodayResultsView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="Build-Version",
                location=OpenApiParameter.HEADER,
                description="1 — winner only (default), 2 — full ranked list",
                required=False,
                type=int,
            )
        ],
        responses=MenuResultSerializer(many=True),
    )
    def get(self, request):
        results = services.get_today_results()
        version = get_build_version(request)

        if version >= 2:
            data = MenuResultSerializer(results, many=True).data
        else:
            winner = results.first()
            data = MenuResultSerializer(winner).data if winner else {}

        return Response(data)
