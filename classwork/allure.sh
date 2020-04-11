#!/bin/zsh

pytest --alluredir=allure-result .
sleep 1
allure serve allure-result