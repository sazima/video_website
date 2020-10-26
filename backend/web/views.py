from typing import List

from django.db.models import Q
from django_request_mapping import request_mapping
from django.views import View
from typing_extensions import TypedDict

from common.response import Response, NotFoundResponse
from .models import MacType, MacVod


@request_mapping('/api/index')
class IndexView(View):
    @request_mapping('/indexTree')
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
                                           'vod_time',
                                           'vod_id').filter(
                Q(type_id=type_id) |
                Q(type_id_1=type_id)
            ).order_by('-vod_id').all()[:6]
            return_list.append({
                'type_id': type_.get('type_id'),
                'type_name': type_.get('type_name'),
                'type_en': type_.get('type_en'),
                'type_sort': type_.get('type_sort'),
                'videos': [x for x in videos]
            })
        return Response(return_list)


@request_mapping('/api/video')
class VideoView(View):
    @request_mapping('/get_list')
    def get_list(self, request):
        type_en = request.GET.get('type_en')
        page = int(request.GET.get('page') or 1)
        per_page = int(request.GET.get('per_page'))
        start = (page - 1) * per_page
        type_by_type_en = MacType.objects.filter(type_en=type_en).first()  # type: MacType
        if not type_by_type_en:
            return NotFoundResponse()
        query_args = (Q(type_id=type_by_type_en.type_id) | Q(type_id_1=type_by_type_en.type_id))
        total = MacVod.objects.filter(query_args).count()
        videos = MacVod.objects.values(
            'vod_id', 'vod_name', 'vod_time', 'vod_pic'
        ).filter(query_args).order_by('-vod_id').all()[start: start + per_page]
        return Response({
            'total': total,
            'data': [x for x in videos]
        })


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
