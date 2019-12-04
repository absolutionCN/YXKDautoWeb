import page
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger


# 获取log日志
log = GetLogger().get_logger()


class PageFollowUpIndex(Base):

    # 点击随访管理标签
    def page_click_followup_management(self):
        log.info("[点击随访管理标签]对:{}元素进行点击".format(page.business_followup_management))
        self.base_click(page.business_followup_management)

    # 点击随访首页标签
    def page_click_followup_index(self):
        log.info("[点击随访首页标签]对:{}元素进行点击".format(page.business_followup_index))
        self.base_click(page.business_followup_index)

    # 点击设置客户分类span标签
    def page_click_customer_classification(self):
        log.info("[点击设置客户分类span标签]对:{}元素进行点击".format(page.business_customer_classification))
        self.base_click(page.business_customer_classification)

    # 页面退回
    def page_back(self):
        log.info("[页面退回]")
        self.base_page_forward()

    # 点击设置自动定制随访计划规则span标签
    def page_click_followup_fule(self):
        log.info("[点击设置自动定制随访计划规则span标签]对：{}元素进行点击".format(page.business_followup_rule))
        self.base_click(page.business_followup_rule)

    # 点击添加随访客户span标签
    def page_click_followup_rule(self):
        log.info("[点击添加随访客户span标签]对：{}元素进行点击".format(page.business_followup_add_user))
        self.base_click(page.business_followup_add_user)

    # 点击分配健康顾问span标签
    def page_click_allot_consultant(self):
        log.info("[点击分配健康顾问span标签]对:{}元素进行点击".format(page.business_allot_consultant))
        self.base_click(page.business_allot_consultant)

    # 点击手动调整随访计划span标签
    def page_click_change_followup_plan(self):
        log.info("[点击手动调整随访计划span标签]对:{}元素进行点击".format(page.business_change_followup_plan))
        self.base_click(page.business_change_followup_plan)

    # 点击随访执行span标签
    def page_click_followup_execute(self):
        log.info("[点击随访执行span标签]对：{}元素进行点击".format(page.business_followup_execute))
        self.base_click(page.business_followup_execute)

    # 获取当前网页的网址
    def page_get_url(self):
        log.info("[获取当前网页的网址]")
        self.base_get_page_url()

    #