from selenium import webdriver
chrome_capabilities ={
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}
browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_capabilities=chrome_capabilities)
browser.get("https://weixin.sogou.com/weixin?type=1&s_from=input&query=定州日报")
label = browser.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a')
label.click()

the_new_handle = browser.window_handles[-1]
browser.switch_to.window(the_new_handle)    
print(browser.current_url)
browser.quit()

