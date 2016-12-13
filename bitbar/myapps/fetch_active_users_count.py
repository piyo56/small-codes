#!/usr/local/var/pyenv/versions/anaconda3-2.5.0/bin/python3
# coding:utf-8

"""
Google AnalyticsのAPIを使って現在のアクティブユーザー数を取得する
シバンとconfig.jsonの中身・パスは適宜変更して下さい
"""
import sys, os
import json
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

def get_service(api_name, api_version, scope, key_file_location, service_account_email):
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        service_account_email=service_account_email,
        filename=key_file_location,
        scopes=scope)
    http = credentials.authorize(httplib2.Http())

    # Build the service object.
    service = build(api_name, api_version, http=http)

    return service

if __name__=="__main__":
    #config_file_path = "config_files/config.json"
    config_file_path = os.environ["HOME"] +"/Desktop/github/small-codes/bitbar/deploy/config_files/config.json"

    if not os.path.exists(config_file_path):
        print("error\n---\nconfig.jsonを同じディレクトリにおいてください")
        sys.exit()

    # APIを利用するのに必要な情報を読み込む
    config_file = open(config_file_path)
    config = json.load(config_file)
    config_file.close()

    # APIに利用する情報（スコープ、メールアドレス）
    scope = ["https://www.googleapis.com/auth/analytics.readonly"]
    service_account_email = config["email"]
    key_file              = config["key"]
    view_id               = config["view_id"]

    # サービスオブジェクト
    service = get_service('analytics', 'v3', scope, key_file, service_account_email)

    # アクティブユーザーを取得
    data = service.data().realtime().get(
        ids='ga:' + view_id,
        metrics='rt:activeUsers'
    ).execute()

    # 表示
    active_users_count = data['totalsForAllResults']['rt:activeUsers']
    print(":fire:{}".format(active_users_count))

