import time
import requests
import json
import copy
from datetime import timedelta, datetime

Hololive = {
    "UCp6993wxpyDPHUpavwDFqgg": [
        "ときのそら",
        "https://yt3.ggpht.com/a/AATXAJzGvZJuJ92qM5WcfBcDZqPFSj_CGIEYp9VFmA=s288-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCDqI2jOz0weumE8s7paEk6g": [
        "ロボ子さん",
        "https://yt3.ggpht.com/ytc/AKedOLTVWKjrovP0tGtguup9TYZicykceA45olVmEr2kvQ=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC-hM6YJuNYVAmUWxeIr9FeA": [
        "さくらみこ",
        "https://yt3.ggpht.com/ytc/AKedOLQlZnbXr-RooUQezemDKu7alJrZcEMy8_5P07ILug=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC5CwaMl1eIgY8h02uZw7u8A": [
        "星街すいせい",
        "https://yt3.ggpht.com/ytc/AKedOLSAm13gTESsu39zgJ1TYb649BiGqYa_XCv5C6Lu=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC0TXe_LYZ4scaW2XMyi5_kw": [
        "AZKi",
        "https://yt3.ggpht.com/ytc/AKedOLQQhnWKHLOLxjnXksGHHC8bnVS2UniL8Od6JTEPWQ=s88-c-k-c0x00ffffff-no-rj"
    ]
}

webhook_url_Hololive = 'https://discord.com/api/webhooks/936235678939906049/agCK1XYhb_iIrFTISDa27eSGXWzRtKl5lLj0cZ716W92s6-lHgXGAUZd2C-IQvLNKUuA'
webhook_url_Hololive_yotei = 'https://discord.com/api/webhooks/936429380119429130/qiCemXwY2RVboccD62OEgVxAM4fhTKrkHuU0m_WAlG0s8ru5QxE_v7Q1-7fRPqsKChDj'
broadcast_data = {}

YOUTUBE_API_KEY = ['AIzaSyAlCdPecfxoUIqtErjDVYhgsCs8juHB364', 'AIzaSyBIs6-dAh7M5D5MTCrrf21bMtMux2ZO4Ag', 'AIzaSyDQq85rjZdfYJY-k8UPUZ4-nOar5ePUW-Y',
                   'AIzaSyCmxIfCRe1wMSG4t00s-Ml3ekSvF-MsasE', 'AIzaSyBHc-qmCOl-ZbdE3t0ZSQaY2EywWXHOCTk', 'AIzaSyA8O0O3ujZSPh6KaTsZ3SRW4IbDgLWDP-A']

def dataformat_for_python(at_time):
    at_year = int(at_time[0:4])
    at_month = int(at_time[5:7])
    at_day = int(at_time[8:10])
    at_hour = int(at_time[11:13])
    at_minute = int(at_time[14:16])
    at_second = int(at_time[17:19])
    return datetime(at_year, at_month, at_day, at_hour, at_minute, at_second)

def replace_JST(s):
    a = s.split("-")
    u = a[2].split(" ")
    t = u[1].split(":")
    time = [int(a[0]), int(a[1]), int(u[0]), int(t[0]), int(t[1]), int(t[2])]
    if(time[3] >= 15):
        time[2] += 1
        time[3] = time[3] + 9 - 24
    else:
        time[3] += 9
    return (str(time[0]) + "/" + str(time[1]).zfill(2) + "/" + str(time[2]).zfill(2) + " " + str(time[3]).zfill(2) + "-" + str(time[4]).zfill(2) + "-" + str(time[5]).zfill(2))

def post_to_discord(userId, videoId):
    haishin_url = "https://www.youtube.com/watch?v=" + videoId
    content = "配信中！\n" + haishin_url
    main_content = {
        "username": Hololive[userId][0],
        "avatar_url": Hololive[userId][1],
        "content": content
    }
    requests.post(webhook_url_Hololive, main_content)
    broadcast_data.pop(videoId)

def get_information():
    tmp = copy.copy(broadcast_data)
    api_now = 0
    for idol in Hololive:
        api_link = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + idol + "&key=" + YOUTUBE_API_KEY[api_now] + "&eventType=upcoming&type=video"
        api_now = (api_now + 1) % len(YOUTUBE_API_KEY)
        aaa = requests.get(api_link)
        v_data = json.loads(aaa.text)
        try:
            for item in v_data['items']:
                broadcast_data[item['id']['videoId']] = {'channelId': item['snippet']['channelId']}
            for video in broadcast_data:
                a = broadcast_data[video]['starttime']
                try:
                    a
                except KeyError:
                    aaaa = requests.get("https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + video + "&key=" + YOUTUBE_API_KEY[api_now])
                    api_now = (api_now + 1) % len(YOUTUBE_API_KEY)
                    vd = json.loads(aaaa.text)
                    print(vd)
                    broadcast_data[video]['starttime'] = vd['items'][0]['liveStreamingDetails']['scheduledStartTime']
        except KeyError:
            continue
    for vi in broadcast_data:
        if(not(vi in tmp)):
            print(broadcast_data[vi])
            try:
                post_broadcast_schedule(broadcast_data[vi]['channelId'], vi, broadcast_data[vi]['starttime'])
            except KeyError:
                continue

def check_schedule(now_time, broadcast_data):
    for bd in list(broadcast_data):
        try:
            sd_time = datetime.strptime(broadcast_data[bd]['starttime'], '%Y-%m-%dT%H:%M:%SZ')
            sd_time += timedelta(hours=9)
            if(now_time >= sd_time):
                post_to_discord(broadcast_data[bd]['channelId'], bd)
        except KeyError:
            continue

def post_broadcast_schedule(userId, videoId, starttime):
    st = starttime.replace('T', ' ')
    sst = st.replace('Z', '')
    ssst = replace_JST(sst)
    haishin_url = "https://www.youtube.com/watch?v=" + videoId
    content = ssst + "に配信予定！\n" + haishin_url
    main_content = {
        "username": Hololive[userId][0],
        "avatar_url": Hololive[userId][1],
        "content": content
    }
    requests.post(webhook_url_Hololive_yotei, main_content)


while True:
    now_time = datetime.now() + timedelta(hours=9)
    if((now_time.minute == 0) and (now_time.hour % 2 == 0)):
        get_information()
    check_schedule(now_time, broadcast_data)
    time.sleep(60)
