from selene.support.shared import browser
from selene import be


def test_check_first_name(browser_actions):
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Ivan')