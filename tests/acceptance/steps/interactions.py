from behave import *

use_step_matcher('re')

@when('I click on the link id "(.*)"')
def step_impl(context):
    link = context.browser.find_element_by_id('blog-link')
    link.click()

