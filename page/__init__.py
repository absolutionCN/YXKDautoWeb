from selenium.webdriver.common.by import By

'''项目服务器地址'''

URL = "https://test.selfhealth.com.cn/admin/"
URL_CUSTOMER = "https://test.selfhealth.com.cn/"

'''登录B端涉及元素配置信息'''
# 用户名
login_B_username = By.XPATH, '//div/input[@ng-model="data.userName"]'
# 密码
login_B_pwd = By.XPATH, '//div/input[@ng-model="data.password"]'
# 登录按钮
login_B_btn = By.XPATH, '//div/button'
# 错误提示信息
login_err_info = By.XPATH, '//div/div[@class="error show"]'
# 批次管理元素
login_page_info = By.XPATH, '//a[@class="ng-binding active1"]'
# 注销按钮
login_logout_link = By.XPATH, '//div/i[3]'

'''B端登录后新增批次元素'''
# 测评管理标签
business_measurement_management = By.CSS_SELECTOR, 'a.ng-binding'
# 批次管理子标签
business_batch_management = By.XPATH, '//*/div/ul/li[1]/ul/li[1]'

# 新增批次按钮
business_add_batch = By.XPATH, '//div//div/button[1]'
# 批次名称
business_batch_name = By.XPATH, '//div/input[@name="batchName"]'
# 批次类型
business_batch_type = By.XPATH, '//div/select[@name="BatchType"]'
# 测评卡数量
business_card_total = By.XPATH, '//div/input[@name="totalCard"]'
# 推荐套餐按钮
business_package_toggle = By.XPATH, '//*[@id="switch"]/div[4]'
# 打折方式下拉框
business_able_discount = By.XPATH, '//div/select[@class="ng-pristine ng-untouched ng-valid ng-scope ng-not-empty"]'
# 体检区下拉框
business_check_Area = By.XPATH, '//div/select[@name="checkArea"]'
# 套餐类型1+X
business_package_fixed = By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[5]/div[2]/div[5]/div/label[1]/input'
# 套餐类型固定套餐
business_package_fixed_physical_exam = By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[5]/div[2]/div[5]/div/label[2]/input'
# 套餐类型X
business_package_x = By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[5]/div[2]/div[5]/div/label[3]/input'
# 减免费用
business_payment = By.XPATH, '//div/input[@name="payment"]'
# 是否显示减免费用
business_show_payment = By.XPATH, '//div/label/input[@name="enableShowPayment"]'
# 添加全部按钮
business_add_all_package = By.XPATH, '//div/a[@ng-click="itemPushAll()"]'
# 操作信息
business_return_info = By.XPATH, '/html/body/div[6]/div'
# 保存按钮
business_save_setting = By.XPATH, '//div/button[2][@class="modal-btn"]'
# 导入批次按钮
business_add_excel = By.XPATH, '//div/section/div/button[5]'
# 导入批次选择文件按钮
business_choice_file = By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[4]/div/button'
# 导入批次模板下的套餐类型1+X
business_upload_excel_package = By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[6]/div[4]/div/label[1]/input'
# 导入批次模板下的提交按钮
business_upload_save_settings = By.XPATH, '//div/button[@class="modal-btn ng-binding"]'
# 发送短信按钮
business_send_message = By.XPATH, '//div/div/nav/button[1]'
# 不发送短信按钮
business_not_send_message = By.XPATH, '//div/div/nav/button[2]'
# 返回报错信息
business_err_info = By.XPATH, '/html/body/div[5]'
# 返回正确信息
business_right_info = By.XPATH, '/html/body/div[3]/div'
# 批次管理勾选按钮
business_check_button = By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/section/div/section[3]/div[1]/table/tbody/tr[1]/td[1]/div/label/input'
# 追加批次按钮
business_additional_button = By.XPATH, '//div/section/div/button[6]'
# 追加方式，按测评卡数量追加
bussiness_add_card_by_number = By.XPATH, '//div/label/input[@value="number"]'
# 追加测评卡数量
bussiness_add_card_number = By.XPATH, '//div/div/input[@name="cardNumeber"]'
# 追加批次提交按钮
business_additional_put_button = By.XPATH, '//div/button[@class="modal-btn ng-binding"]'
# 测评卡管理标签
business_card_management = By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/ul/li[1]/ul/li[2]/a'
# 卡号详情信息
business_card_info = By.CSS_SELECTOR, 'tr.table-tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > span:nth-child(3)'
# 卡号详情 账号
business_card_username_info = By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[1]'
# 卡号详情 密码
business_card_pwd_info = By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]'
# 添加批次报错信息
business_add_batch_error_msg = By.XPATH, '/html/body/div[1]/div/div/div[1]/h4'
# 预约管理标签
business_booking_label = By.XPATH, '//div/ul/li[2]/a'
# 预约配置子标签
business_booking_setting = By.XPATH, '//div/ul/li[2]/ul/li[1]/a'
# 预约统计子标签
business_booking_statistics = By.XPATH, '//div/ul/li[2]/ul/li[2]/a'
# 预约配置页面下的编辑按钮
business_booking_button = By.XPATH, '//div/section/div/section/div/button'
# 预约配置页面下的可预约时间段输入框   5~730
businsee_booking_timePeriod = By.XPATH, '//div/section/form/div/span/input[@name="timePeriod"]'
# 预约配置页面下的特殊时间设置 时间输入框    24小时制   12:23
business_booking_intervalLastTime = By.XPATH, '//div/section/form/div/span/input[@name="intervalLastTime"]'
# 预约配置页面下的intervalTime 输入框   1~5
businsee_booking_intervalTime = By.XPATH, '//div/section/form/div/span/input[@name="intervalTime"]'
# 预约配置页面下的添加体检区按钮
business_booking_addCheckAreas = By.XPATH, '//div/button[@data-title="添加体检区"]'
# 预约配置页面下的添加体检区tr标签
bussiness_booking_add_tr = By.XPATH, '//div/form/table/tbody/tr'
# 预约配置页面下的保存按钮
business_save_booking_button = By.XPATH, '//*/div/section/div/button[@ng-click="vm.save()"]'
# 预约配置页面下保存成功信息
bussiness_save_success_msg = By.XPATH, '//div/div[@class="success show"]'
# 套餐推荐标签
business_recommendad_packages = By.XPATH, '//*/div/ul/li[4]/a'
# 套餐推荐标签下项目类别管理子标签
business_recommendad_item_classification = By.XPATH, '//*/div/ul/li[4]/ul/li[1]'
# 项目类别页面新增按钮
bussiness_item_classification_add = By.XPATH, '//*/div/section[2]/div/button[1]'
# 新增编辑页面下类别序号输入框
bussiness_category_number = By.XPATH, '//*/div/form/div[1]/div/input'
# 新增编辑页面下编码输入框
business_encoding_number = By.XPATH, '//*/div/form/div[2]/div/input'
# 新增编辑页面下类别名称输入框
business_category_name = By.XPATH, '//*/div/form/div[3]/div/input'
# 新增编辑页面下保存按钮
business_item_classification_add_button = By.XPATH, '//*/div[3]/button[2]'
# 项目类别管理页面的checkbox
business_item_classification_checkbox = By.XPATH, '//*/tr[1]/td/div/label/input'
# 项目类别管理下的编辑按钮
bussiness_item_classification_edit_button = By.XPATH, '//*/div/section/div/section[2]/div/button[2]'
# # 项目类别管理下报错信息
# business_item_classification_err_msg = By.XPATH, '//*/div/div[@class="error show"]'
# 随访管理标签
business_followup_management = By.XPATH, '//*/div/ul/li[8]/a'
# 随访首页标签
business_followup_index = By.XPATH, '//*/div/ul/li[8]/ul/li[1]/a'
# 设置客户分类span
business_customer_classification = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[1]/span[1]/strong/a'
# 设置设置自动定制随访计划规则span
business_followup_rule = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[1]/span[2]/strong/a'
# 添加随访客户span标签
business_followup_add_user = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[1]/span[3]/strong/a'
# 分配健康顾问span标签
business_allot_consultant = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[3]/span[3]/strong/a'
# 手动调整随访计划span标签
business_change_followup_plan = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[3]/span[2]/strong/a'
# 随访执行span标签
business_followup_execute = By.XPATH, '//*/div/section/div/section/div/div/div/div[1]/p[3]/span[1]/strong/a'



'''C端元素'''
# 卡号输入
customer_username_input = By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[1]/section/form/div[1]/div[1]/input'
# 密码输入
customer_pwd_input = By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/section/form/div[1]/div[2]/input'
# 验证码
customer_verification_code = By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/section/form/div[1]/div[3]/div[1]/input'
# 登陆按钮
customer_login_button = By.CSS_SELECTOR, '.btn'
# 报告管理
customer_report_management = By.CSS_SELECTOR, '.menu-nav > li:nth-child(2) > a:nth-child(1)'
# 报告管理页面下的查看报告
customer_check_the_report = By.CSS_SELECTOR, '.report-content-msg > div:nth-child(2) > span:nth-child(1) > a:nth-child(1) > button:nth-child(1)'
# 报告管理页面下的答题详情
customer_answer_detail = By.CSS_SELECTOR, '.right-btn > a:nth-child(1) > button:nth-child(1)'
# 预约套餐界面
customer_choice_package = By.XPATH, '//*[@id="app"]/div/div/header/div[2]/nav/ul/li[3]/a'
# 定制套餐按钮
customer_package_btn = By.CSS_SELECTOR, 'button.btn:nth-child(1)'
# 我的订单
customer_my_order = By.CSS_SELECTOR, '.menu-nav > li:nth-child(4) > a:nth-child(1)'
# 输入预算金额
customer_input_budget = By.CSS_SELECTOR, '.input_box > input:nth-child(1)'
# 输入预算后的确定按钮
customer_confirm_button = By.CSS_SELECTOR, 'button.btn:nth-child(2)'
# 预约时间
customer_choice_time = By.CSS_SELECTOR, '.ant-calendar-picker-input'
# 具体的预约时间
customer_time = By.CSS_SELECTOR, '.ant-calendar-tbody > tr:nth-child(4) > td:nth-child(4) > div:nth-child(1)'
# 预约时间确定按钮
customer_time_btn = By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[57]/div/p/button'
