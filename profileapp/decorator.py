from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request,*args,**kwargs):
        target_profile = Profile.objects.get(pk = kwargs['pk']) #profile 모델의 정보 중 kwargs 의 pk 값을 가져온다
        if target_profile.user == request.user: #요청 유저랑 target user 랑 같은지
            return func(request,*args,**kwargs)
        else: #권한이 없는 곳에 접속
            return HttpResponseForbidden()

    return decorated