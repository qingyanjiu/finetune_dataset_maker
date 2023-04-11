# -*- coding: utf-8 -*-
# pip install rpa

import tagui as t

t.init(visual_automation = True)
# t.url('http://localhost:8080')
# t.type('//*[@name="username"]', 'admin')
# t.type('//*[@name="password"]', 'admin')
# t.click('//*[@class="login100-form-btn"]')
# t.wait() # ensure results are fully loaded
# # t.run('console.log()')
# t.snap('page', 'results.png')
# title = t.read('//*[@class="page-title"]')
# print(title)

t.url('http://124.112.64.97:9003/bsdt/login')
# 读取验证码图片
# url = t.read('//*[@class="rand-cordor-mage"]/@src')
# print(url)
t.hover('//*[@class="rand-cordor-mage"]')
print(t.read(t.mouse_x(), t.mouse_y(), t.mouse_x() + 69, t.mouse_y() + 23))
t.close()