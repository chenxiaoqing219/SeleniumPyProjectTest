# -*- coding: UTF-8 -*-

Feature: Register User

  As a developer
  This is my first bdd project
  Scenario: I open register website
    When I open the register website "http://www.5itest.cn/register"
    Then I expect that the title is "注册"

  #Scenario: input username

  Scenario: input username
    When I set with useremail "xiaoxiao002@qq.com"
    And I set with username "xiaoxiao002"
    And I set with password "111111"
    And I set with code "xeass"
    And I click with registerbutton
    Then I expect that text "验证码错误"