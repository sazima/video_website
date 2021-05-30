# coding: utf-8
from sqlalchemy import Column, Float, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Type(Base):
    __tablename__ = 'type'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), server_default=text("''"), comment='名称')
    parent_type = Column(INTEGER(11), server_default=text("'0'"), comment='父级分类')
    sort = Column(INTEGER(11), server_default=text("'0'"))


class Video(Base):
    __tablename__ = 'video'

    id = Column(INTEGER(11), primary_key=True)
    type_id1 = Column(INTEGER(11), server_default=text("'0'"), comment='分类1')
    type_id2 = Column(INTEGER(11), server_default=text("'0'"))
    name = Column(String(255), server_default=text("''"), comment='名称')
    picture = Column(String(255), server_default=text("''"), comment='图片')
    content = Column(Text, comment='简介内容')
    av = Column(String(255), comment='编码')
    update_time = Column(INTEGER(11), server_default=text("'0'"))
    api_update_time = Column(INTEGER(11), nullable=True)


class VideoLink(Base):
    __tablename__ = 'video_link'

    id = Column(INTEGER(11), primary_key=True)
    video_id = Column(INTEGER(11), nullable=False)
    from_name = Column(String(255), server_default=text("'播放地址1'"), comment='播放来源')
    play_name = Column(String(255), server_default=text("'第一集'"), comment='选集')
    play_url = Column(String(255), server_default=text("''"), comment='播放url')


class VideoTanmu(Base):
    __tablename__ = 'video_tanmu'

    id = Column(INTEGER(11), primary_key=True)
    video_link_id = Column(INTEGER(11), nullable=False)
    content = Column(String(255), server_default=text("''"), comment='弹幕内容')
    style = Column(String(255), server_default=text("''"), comment='样式')
    from_name = Column(String(255), server_default=text("'播放地址1'"), comment='播放来源')
    play_name = Column(String(255), server_default=text("'第一集'"), comment='选集')
    play_url = Column(String(255), server_default=text("''"), comment='播放url')
    current_time = Column(Float(5), server_default=text("'0.00'"), comment='弹幕时间')
    current_time_int = Column(INTEGER(11), server_default=text("'0'"), comment='时间取整数')
    video_id = Column(INTEGER(11), nullable=False)


class ThirdApi(Base):
    __tablename__ = 'third_collection_api'

    id = Column(INTEGER(11), primary_key=True)
    key = Column(String(255), comment='唯一标志')
    url = Column(String(255), comment='链接')
    name = Column(String(255), comment='名称')
    bind_id = Column(Text,  comment='分类绑定设置， json字符串')
