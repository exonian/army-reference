from django.http import JsonResponse

from armies.models import Game


def health_check(self):
    if Game.objects.exists():
        return JsonResponse({'db-access': True}, status=200)
    else:
        return JsonResponse({'db-access': False}, status=503)
