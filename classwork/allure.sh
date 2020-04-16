#!/bin/zsh

pytest --alluredir=allure-results .
sleep 1
allure serve allure-results