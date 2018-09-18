from behave import *
from selenium import webdriver

use_step_matcher('re')
webdriver_path = r"C:\Users\test\PycharmProjects\chrome_driver\chromedriver"


# decorator that lets know behave lib. that when this is step occurs a gherkin function needs to be run
@given('I am on the homepage')
def step_impl(context):
    # if system PATH to chrome driver is not included you have to include file path
    context.browser = webdriver.Chrome(webdriver_path)  # launches chrome window
    context.browser.get('http://127.0.0.1:5000/')


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome(webdriver_path)  # launches chrome window
    context.browser.get('http://127.0.0.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url