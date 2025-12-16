from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.bible_change.bible_relay.serializers.auth.relay_comment_input import (
    RelayCommentInputSerializer,
)
from apps.bible_change.bible_relay.serializers.auth.relay_comment_output import (
    RelayCommentOutputSerializer,
)
from apps.bible_change.bible_relay.services.relay_comment_service import (
    RelayCommentService,
)

class RelayCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = RelayCommentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = RelayCommentService.create_comment(
            user=request.user,
            relay=serializer.validated_data["relay"],
            content=serializer.validated_data["content"]
        )
        response_serializer = RelayCommentOutputSerializer(comment)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )