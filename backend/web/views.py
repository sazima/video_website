from typing import List

from django.db.models import Q
from django_request_mapping import request_mapping
from django.views import View
from typing_extensions import TypedDict

from common.response import Response, NotFoundResponse
from .models import MacType, MacVod


@request_mapping('/index')
class IndexView(View):
    @request_mapping('/index_tree')
    def get_index_tree(self, request):
        return_list = list()  # type: List[_IndexTreeReturnDict]
        root_type = MacType.objects.values(
            'type_id',
            'type_name',
            'type_en',
            'type_sort'
        ).filter(type_pid=0).order_by('type_sort').all()
        for type_ in root_type:
            type_id = type_.get('type_id')
            videos = MacVod.objects.values('vod_pic',
                                          'vod_name',
                                          'vod_time').filter(
                Q(type_id=type_id) |
                Q(type_id_1=type_id)
            ).order_by('-vod_id').all()[:5]
            return_list.append({
                'type_id': type_.get('type_id'),
                'type_name': type_.get('type_name'),
                'type_en': type_.get('type_en'),
                'type_sort': type_.get('type_sort'),
                'videos': [x for x in videos]
            })
        return Response(return_list)


@request_mapping('/video')
class VideoView(View):
    @request_mapping('/get_by_type_en')
    def get_by_type_en(self, request):
        type_en = request.GET.get('type_en')
        type_by_type_en = MacType.objects.filter(type_en=type_en).first()  # type: MacType
        if not type_by_type_en:
            return NotFoundResponse()
        video_by_type = MacVod.objects.filter(Q(type_id=type_by_type_en.type_id) |
                                              Q(type_id_1=type_by_type_en.type_id))


class _IndexTreeReturnDict(TypedDict):
    class Videos(TypedDict):
        vod_name: str
        vod_pic: str
        vod_time: str

    type_id: int
    type_name: str
    type_en: str
    type_sort: int
    videos: List['Videos']
