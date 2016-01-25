from behave import *

use_step_matcher("re")

@step(u'I search for (?P<locator>.*)')
def step_impl(context, locator):
    context.germanium.S(locator)

@step(u'nothing happens')
def step_impl(context):
    pass