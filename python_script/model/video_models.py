# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, String, Text, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MacActor(Base):
    __tablename__ = 'mac_actor'

    actor_id = Column(INTEGER(10), primary_key=True)
    type_id = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    type_id_1 = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    actor_name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    actor_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    actor_alias = Column(String(255), nullable=False, server_default=text("''"))
    actor_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    actor_lock = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    actor_letter = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    actor_sex = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    actor_color = Column(String(6), nullable=False, server_default=text("''"))
    actor_pic = Column(String(255), nullable=False, server_default=text("''"))
    actor_blurb = Column(String(255), nullable=False, server_default=text("''"))
    actor_remarks = Column(String(100), nullable=False, server_default=text("''"))
    actor_area = Column(String(20), nullable=False, index=True, server_default=text("''"))
    actor_height = Column(String(10), nullable=False, server_default=text("''"))
    actor_weight = Column(String(10), nullable=False, server_default=text("''"))
    actor_birthday = Column(String(10), nullable=False, server_default=text("''"))
    actor_birtharea = Column(String(20), nullable=False, server_default=text("''"))
    actor_blood = Column(String(10), nullable=False, server_default=text("''"))
    actor_starsign = Column(String(10), nullable=False, server_default=text("''"))
    actor_school = Column(String(20), nullable=False, server_default=text("''"))
    actor_works = Column(String(255), nullable=False, server_default=text("''"))
    actor_tag = Column(String(255), nullable=False, index=True, server_default=text("''"))
    actor_class = Column(String(255), nullable=False, index=True, server_default=text("''"))
    actor_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    actor_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    actor_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    actor_time_hits = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    actor_time_make = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    actor_hits = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    actor_hits_day = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    actor_hits_week = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    actor_hits_month = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    actor_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    actor_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    actor_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    actor_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    actor_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    actor_tpl = Column(String(30), nullable=False, server_default=text("''"))
    actor_jumpurl = Column(String(150), nullable=False, server_default=text("''"))
    actor_content = Column(Text, nullable=False)


class MacAdmin(Base):
    __tablename__ = 'mac_admin'

    admin_id = Column(SMALLINT(6), primary_key=True)
    admin_name = Column(String(30), nullable=False, index=True, server_default=text("''"))
    admin_pwd = Column(CHAR(32), nullable=False, server_default=text("''"))
    admin_random = Column(CHAR(32), nullable=False, server_default=text("''"))
    admin_status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    admin_auth = Column(Text, nullable=False)
    admin_login_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    admin_login_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    admin_login_num = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    admin_last_login_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    admin_last_login_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class MacArt(Base):
    __tablename__ = 'mac_art'

    art_id = Column(INTEGER(10), primary_key=True)
    type_id = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    type_id_1 = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    group_id = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    art_name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    art_sub = Column(String(255), nullable=False, server_default=text("''"))
    art_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    art_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    art_letter = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    art_color = Column(String(6), nullable=False, server_default=text("''"))
    art_from = Column(String(30), nullable=False, server_default=text("''"))
    art_author = Column(String(30), nullable=False, server_default=text("''"))
    art_tag = Column(String(100), nullable=False, index=True, server_default=text("''"))
    art_class = Column(String(255), nullable=False, server_default=text("''"))
    art_pic = Column(String(255), nullable=False, server_default=text("''"))
    art_pic_thumb = Column(String(255), nullable=False, server_default=text("''"))
    art_pic_slide = Column(String(255), nullable=False, server_default=text("''"))
    art_blurb = Column(String(255), nullable=False, server_default=text("''"))
    art_remarks = Column(String(100), nullable=False, server_default=text("''"))
    art_jumpurl = Column(String(150), nullable=False, server_default=text("''"))
    art_tpl = Column(String(30), nullable=False, server_default=text("''"))
    art_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    art_lock = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    art_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    art_points_detail = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    art_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_hits = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_hits_day = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_hits_week = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_hits_month = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    art_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    art_time_hits = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    art_time_make = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    art_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    art_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    art_rel_art = Column(String(255), nullable=False, server_default=text("''"))
    art_rel_vod = Column(String(255), nullable=False, server_default=text("''"))
    art_pwd = Column(String(10), nullable=False, server_default=text("''"))
    art_pwd_url = Column(String(255), nullable=False, server_default=text("''"))
    art_title = Column(MEDIUMTEXT, nullable=False)
    art_note = Column(MEDIUMTEXT, nullable=False)
    art_content = Column(MEDIUMTEXT, nullable=False)


class MacCard(Base):
    __tablename__ = 'mac_card'

    card_id = Column(INTEGER(10), primary_key=True)
    card_no = Column(String(16), nullable=False, index=True, server_default=text("''"))
    card_pwd = Column(String(8), nullable=False, index=True, server_default=text("''"))
    card_money = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    card_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    card_use_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    card_sale_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    card_add_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    card_use_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))


class MacCash(Base):
    __tablename__ = 'mac_cash'

    cash_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    cash_status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    cash_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    cash_money = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    cash_bank_name = Column(String(60), nullable=False, server_default=text("''"))
    cash_bank_no = Column(String(30), nullable=False, server_default=text("''"))
    cash_payee_name = Column(String(30), nullable=False, server_default=text("''"))
    cash_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    cash_time_audit = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class MacCjContent(Base):
    __tablename__ = 'mac_cj_content'

    id = Column(INTEGER(10), primary_key=True)
    nodeid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    url = Column(CHAR(255), nullable=False)
    title = Column(CHAR(100), nullable=False)
    data = Column(MEDIUMTEXT, nullable=False)


class MacCjHistory(Base):
    __tablename__ = 'mac_cj_history'

    md5 = Column(CHAR(32), primary_key=True, index=True)


class MacCjNode(Base):
    __tablename__ = 'mac_cj_node'

    nodeid = Column(SMALLINT(6), primary_key=True)
    name = Column(String(20), nullable=False)
    lastdate = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    sourcecharset = Column(String(8), nullable=False)
    sourcetype = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    urlpage = Column(Text, nullable=False)
    pagesize_start = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    pagesize_end = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    page_base = Column(CHAR(255), nullable=False)
    par_num = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    url_contain = Column(CHAR(100), nullable=False)
    url_except = Column(CHAR(100), nullable=False)
    url_start = Column(CHAR(100), nullable=False, server_default=text("''"))
    url_end = Column(CHAR(100), nullable=False, server_default=text("''"))
    title_rule = Column(CHAR(100), nullable=False)
    title_html_rule = Column(Text, nullable=False)
    type_rule = Column(CHAR(100), nullable=False)
    type_html_rule = Column(Text, nullable=False)
    content_rule = Column(CHAR(100), nullable=False)
    content_html_rule = Column(Text, nullable=False)
    content_page_start = Column(CHAR(100), nullable=False)
    content_page_end = Column(CHAR(100), nullable=False)
    content_page_rule = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    content_page = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    content_nextpage = Column(CHAR(100), nullable=False)
    down_attachment = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    watermark = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    coll_order = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    customize_config = Column(Text, nullable=False)
    program_config = Column(Text, nullable=False)
    mid = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class MacCollect(Base):
    __tablename__ = 'mac_collect'

    collect_id = Column(INTEGER(10), primary_key=True)
    collect_name = Column(String(30), nullable=False, server_default=text("''"))
    collect_url = Column(String(255), nullable=False, server_default=text("''"))
    collect_type = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    collect_mid = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    collect_appid = Column(String(30), nullable=False, server_default=text("''"))
    collect_appkey = Column(String(30), nullable=False, server_default=text("''"))
    collect_param = Column(String(100), nullable=False, server_default=text("''"))
    collect_filter = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    collect_filter_from = Column(String(255), nullable=False, server_default=text("''"))
    collect_opt = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class MacComment(Base):
    __tablename__ = 'mac_comment'

    comment_id = Column(INTEGER(10), primary_key=True)
    comment_mid = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    comment_rid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    comment_pid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    comment_status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    comment_name = Column(String(60), nullable=False, server_default=text("''"))
    comment_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    comment_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    comment_content = Column(String(255), nullable=False, server_default=text("''"))
    comment_up = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    comment_down = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    comment_reply = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    comment_report = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))


class MacGbook(Base):
    __tablename__ = 'mac_gbook'

    gbook_id = Column(INTEGER(10), primary_key=True)
    gbook_rid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    gbook_status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    gbook_name = Column(String(60), nullable=False, server_default=text("''"))
    gbook_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    gbook_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    gbook_reply_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    gbook_content = Column(String(255), nullable=False, server_default=text("''"))
    gbook_reply = Column(String(255), nullable=False, index=True, server_default=text("''"))


class MacGroup(Base):
    __tablename__ = 'mac_group'

    group_id = Column(SMALLINT(6), primary_key=True)
    group_name = Column(String(30), nullable=False, server_default=text("''"))
    group_status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    group_type = Column(Text, nullable=False)
    group_popedom = Column(Text, nullable=False)
    group_points_day = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    group_points_week = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    group_points_month = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    group_points_year = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    group_points_free = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class MacLink(Base):
    __tablename__ = 'mac_link'

    link_id = Column(SMALLINT(6), primary_key=True)
    link_type = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    link_name = Column(String(60), nullable=False, server_default=text("''"))
    link_sort = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    link_add_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    link_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    link_url = Column(String(255), nullable=False, server_default=text("''"))
    link_logo = Column(String(255), nullable=False, server_default=text("''"))


class MacMsg(Base):
    __tablename__ = 'mac_msg'

    msg_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    msg_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    msg_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    msg_to = Column(String(30), nullable=False, server_default=text("''"))
    msg_code = Column(String(10), nullable=False, index=True, server_default=text("''"))
    msg_content = Column(String(255), nullable=False, server_default=text("''"))
    msg_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))


class MacOrder(Base):
    __tablename__ = 'mac_order'

    order_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    order_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    order_code = Column(String(30), nullable=False, index=True, server_default=text("''"))
    order_price = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    order_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    order_points = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    order_pay_type = Column(String(10), nullable=False, server_default=text("''"))
    order_pay_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    order_remarks = Column(String(100), nullable=False, server_default=text("''"))


class MacPlog(Base):
    __tablename__ = 'mac_plog'

    plog_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_id_1 = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    plog_type = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    plog_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    plog_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    plog_remarks = Column(String(100), nullable=False, server_default=text("''"))


class MacRole(Base):
    __tablename__ = 'mac_role'

    role_id = Column(INTEGER(10), primary_key=True)
    role_rid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    role_name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    role_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    role_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    role_lock = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    role_letter = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    role_color = Column(String(6), nullable=False, server_default=text("''"))
    role_actor = Column(String(255), nullable=False, index=True, server_default=text("''"))
    role_remarks = Column(String(100), nullable=False, server_default=text("''"))
    role_pic = Column(String(255), nullable=False, server_default=text("''"))
    role_sort = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    role_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    role_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    role_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    role_time_hits = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    role_time_make = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    role_hits = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    role_hits_day = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    role_hits_week = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    role_hits_month = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    role_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    role_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    role_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    role_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    role_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    role_tpl = Column(String(30), nullable=False, server_default=text("''"))
    role_jumpurl = Column(String(150), nullable=False, server_default=text("''"))
    role_content = Column(Text, nullable=False)


class MacTanmu(Base):
    __tablename__ = 'mac_tanmu'

    tanmu_id = Column(INTEGER(11), primary_key=True)
    vod_id = Column(INTEGER(11), index=True, comment='视频id')
    play_url = Column(String(255), comment='播放链接')
    content = Column(String(255))
    current_time = Column(Float, comment='时间')
    current_time_int = Column(INTEGER(11), comment='时间取整')
    styles = Column(MEDIUMTEXT, comment='样式')
    user_id = Column(INTEGER(11))
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    vod_play_from = Column(String(255), comment='名称, 比如kakam3u8')
    play_name = Column(String(255))


class MacTopic(Base):
    __tablename__ = 'mac_topic'

    topic_id = Column(SMALLINT(6), primary_key=True)
    topic_name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    topic_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    topic_sub = Column(String(255), nullable=False, server_default=text("''"))
    topic_status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    topic_sort = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    topic_letter = Column(CHAR(1), nullable=False, server_default=text("''"))
    topic_color = Column(String(6), nullable=False, server_default=text("''"))
    topic_tpl = Column(String(30), nullable=False, server_default=text("''"))
    topic_type = Column(String(255), nullable=False, server_default=text("''"))
    topic_pic = Column(String(255), nullable=False, server_default=text("''"))
    topic_pic_thumb = Column(String(255), nullable=False, server_default=text("''"))
    topic_pic_slide = Column(String(255), nullable=False, server_default=text("''"))
    topic_key = Column(String(255), nullable=False, server_default=text("''"))
    topic_des = Column(String(255), nullable=False, server_default=text("''"))
    topic_title = Column(String(255), nullable=False, server_default=text("''"))
    topic_blurb = Column(String(255), nullable=False, server_default=text("''"))
    topic_remarks = Column(String(100), nullable=False, server_default=text("''"))
    topic_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    topic_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    topic_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_hits = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_hits_day = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_hits_week = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_hits_month = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    topic_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    topic_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    topic_time_hits = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    topic_time_make = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    topic_tag = Column(String(255), nullable=False, server_default=text("''"))
    topic_rel_vod = Column(Text)
    topic_rel_art = Column(Text)
    topic_content = Column(Text)
    topic_extend = Column(Text)


class MacType(Base):
    __tablename__ = 'mac_type'

    type_id = Column(SMALLINT(6), primary_key=True)
    type_name = Column(String(60), nullable=False, index=True, server_default=text("''"))
    type_en = Column(String(60), nullable=False, index=True, server_default=text("''"))
    type_sort = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    type_mid = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'1'"))
    type_pid = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    type_status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    type_tpl = Column(String(30), nullable=False, server_default=text("''"))
    type_tpl_list = Column(String(30), nullable=False, server_default=text("''"))
    type_tpl_detail = Column(String(30), nullable=False, server_default=text("''"))
    type_tpl_play = Column(String(30), nullable=False, server_default=text("''"))
    type_tpl_down = Column(String(30), nullable=False, server_default=text("''"))
    type_key = Column(String(255), nullable=False, server_default=text("''"))
    type_des = Column(String(255), nullable=False, server_default=text("''"))
    type_title = Column(String(255), nullable=False, server_default=text("''"))
    type_union = Column(String(255), nullable=False, server_default=text("''"))
    type_extend = Column(Text)
    type_logo = Column(String(255), nullable=False, server_default=text("''"))
    type_pic = Column(String(255), nullable=False, server_default=text("''"))
    type_jumpurl = Column(String(150), nullable=False, server_default=text("''"))


class MacUlog(Base):
    __tablename__ = 'mac_ulog'

    ulog_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    ulog_mid = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    ulog_type = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    ulog_rid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    ulog_sid = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    ulog_nid = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    ulog_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    ulog_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class MacUser(Base):
    __tablename__ = 'mac_user'

    user_id = Column(INTEGER(10), primary_key=True)
    group_id = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    user_name = Column(String(30), nullable=False, index=True, server_default=text("''"))
    user_pwd = Column(String(32), nullable=False, server_default=text("''"))
    user_nick_name = Column(String(30), nullable=False, server_default=text("''"))
    user_qq = Column(String(16), nullable=False, server_default=text("''"))
    user_email = Column(String(30), nullable=False, server_default=text("''"))
    user_phone = Column(String(16), nullable=False, server_default=text("''"))
    user_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    user_portrait = Column(String(100), nullable=False, server_default=text("''"))
    user_portrait_thumb = Column(String(100), nullable=False, server_default=text("''"))
    user_openid_qq = Column(String(40), nullable=False, server_default=text("''"))
    user_openid_weixin = Column(String(40), nullable=False, server_default=text("''"))
    user_question = Column(String(255), nullable=False, server_default=text("''"))
    user_answer = Column(String(255), nullable=False, server_default=text("''"))
    user_points = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_points_froze = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_reg_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_reg_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_login_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_login_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_last_login_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_last_login_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_login_num = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    user_extend = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    user_random = Column(String(32), nullable=False, server_default=text("''"))
    user_end_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_pid = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_pid_2 = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    user_pid_3 = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class MacVisit(Base):
    __tablename__ = 'mac_visit'

    visit_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), index=True, server_default=text("'0'"))
    visit_ip = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    visit_ly = Column(String(100), nullable=False, server_default=text("''"))
    visit_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))


class MacVod(Base):
    __tablename__ = 'mac_vod'

    vod_id = Column(INTEGER(10), primary_key=True)
    type_id = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    type_id_1 = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    group_id = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    vod_name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    vod_sub = Column(String(255), nullable=False, server_default=text("''"))
    vod_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    vod_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    vod_letter = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    vod_color = Column(String(6), nullable=False, server_default=text("''"))
    vod_tag = Column(String(100), nullable=False, index=True, server_default=text("''"))
    vod_class = Column(String(255), nullable=False, index=True, server_default=text("''"))
    vod_pic = Column(String(255), nullable=False, server_default=text("''"))
    vod_pic_thumb = Column(String(255), nullable=False, server_default=text("''"))
    vod_pic_slide = Column(String(255), nullable=False, server_default=text("''"))
    vod_actor = Column(String(255), nullable=False, index=True, server_default=text("''"))
    vod_director = Column(String(255), nullable=False, index=True, server_default=text("''"))
    vod_writer = Column(String(100), nullable=False, server_default=text("''"))
    vod_behind = Column(String(100), nullable=False, server_default=text("''"))
    vod_blurb = Column(String(255), nullable=False, server_default=text("''"))
    vod_remarks = Column(String(100), nullable=False, server_default=text("''"))
    vod_pubdate = Column(String(100), nullable=False, server_default=text("''"))
    vod_total = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_serial = Column(String(20), nullable=False, server_default=text("'0'"))
    vod_tv = Column(String(30), nullable=False, server_default=text("''"))
    vod_weekday = Column(String(30), nullable=False, server_default=text("''"))
    vod_area = Column(String(20), nullable=False, index=True, server_default=text("''"))
    vod_lang = Column(String(10), nullable=False, index=True, server_default=text("''"))
    vod_year = Column(String(10), nullable=False, index=True, server_default=text("''"))
    vod_version = Column(String(30), nullable=False, index=True, server_default=text("''"))
    vod_state = Column(String(30), nullable=False, index=True, server_default=text("''"))
    vod_author = Column(String(60), nullable=False, server_default=text("''"))
    vod_jumpurl = Column(String(150), nullable=False, server_default=text("''"))
    vod_tpl = Column(String(30), nullable=False, server_default=text("''"))
    vod_tpl_play = Column(String(30), nullable=False, server_default=text("''"))
    vod_tpl_down = Column(String(30), nullable=False, server_default=text("''"))
    vod_isend = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    vod_lock = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    vod_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    vod_copyright = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    vod_points = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    vod_points_play = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    vod_points_down = Column(SMALLINT(6), nullable=False, index=True, server_default=text("'0'"))
    vod_hits = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_hits_day = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_hits_week = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_hits_month = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_duration = Column(String(10), nullable=False, server_default=text("''"))
    vod_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    vod_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    vod_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    vod_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    vod_time_hits = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    vod_time_make = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    vod_trysee = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    vod_douban_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    vod_douban_score = Column(DECIMAL(3, 1), nullable=False, server_default=text("'0.0'"))
    vod_reurl = Column(String(255), nullable=False, server_default=text("''"))
    vod_rel_vod = Column(String(255), nullable=False, server_default=text("''"))
    vod_rel_art = Column(String(255), nullable=False, server_default=text("''"))
    vod_pwd = Column(String(10), nullable=False, server_default=text("''"))
    vod_pwd_url = Column(String(255), nullable=False, server_default=text("''"))
    vod_pwd_play = Column(String(10), nullable=False, server_default=text("''"))
    vod_pwd_play_url = Column(String(255), nullable=False, server_default=text("''"))
    vod_pwd_down = Column(String(10), nullable=False, server_default=text("''"))
    vod_pwd_down_url = Column(String(255), nullable=False, server_default=text("''"))
    vod_content = Column(Text, nullable=False)
    vod_play_from = Column(String(255), nullable=False, server_default=text("''"))
    vod_play_server = Column(String(255), nullable=False, server_default=text("''"))
    vod_play_note = Column(String(255), nullable=False, server_default=text("''"))
    vod_play_url = Column(MEDIUMTEXT, nullable=False)
    vod_down_from = Column(String(255), nullable=False, server_default=text("''"))
    vod_down_server = Column(String(255), nullable=False, server_default=text("''"))
    vod_down_note = Column(String(255), nullable=False, server_default=text("''"))
    vod_down_url = Column(MEDIUMTEXT, nullable=False)
    vod_plot = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    vod_plot_name = Column(MEDIUMTEXT, nullable=False)
    vod_plot_detail = Column(MEDIUMTEXT, nullable=False)


class MacWebsite(Base):
    __tablename__ = 'mac_website'

    website_id = Column(INTEGER(10), primary_key=True)
    type_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    type_id_1 = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    website_name = Column(String(60), nullable=False, index=True, server_default=text("''"))
    website_sub = Column(String(255), nullable=False, server_default=text("''"))
    website_en = Column(String(255), nullable=False, index=True, server_default=text("''"))
    website_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    website_letter = Column(CHAR(1), nullable=False, index=True, server_default=text("''"))
    website_color = Column(String(6), nullable=False, server_default=text("''"))
    website_lock = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    website_sort = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    website_jumpurl = Column(String(255), nullable=False, server_default=text("''"))
    website_pic = Column(String(255), nullable=False, server_default=text("''"))
    website_logo = Column(String(255), nullable=False, server_default=text("''"))
    website_area = Column(String(20), nullable=False, server_default=text("''"))
    website_lang = Column(String(10), nullable=False, server_default=text("''"))
    website_level = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    website_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    website_time_add = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    website_time_hits = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    website_time_make = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    website_hits = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_hits_day = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_hits_week = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_hits_month = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_score = Column(DECIMAL(3, 1), nullable=False, index=True, server_default=text("'0.0'"))
    website_score_all = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_score_num = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_up = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_down = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_referer = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_referer_day = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_referer_week = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_referer_month = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    website_tag = Column(String(100), nullable=False, index=True, server_default=text("''"))
    website_class = Column(String(255), nullable=False, index=True, server_default=text("''"))
    website_remarks = Column(String(100), nullable=False, server_default=text("''"))
    website_tpl = Column(String(30), nullable=False, server_default=text("''"))
    website_blurb = Column(String(255), nullable=False, server_default=text("''"))
    website_content = Column(MEDIUMTEXT, nullable=False)
