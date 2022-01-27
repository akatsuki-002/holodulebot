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
    ],
    "UCD8HOxPs4Xvsm8H0ZxXGiBw": [
        "夜空メル",
        "https://yt3.ggpht.com/ytc/AKedOLS8pa1lDGBL7tieftDRgPjVsSexeMJ9YURgBTXDMg=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCFTLzh12_nrtzqBPsTCqenA": [
        "アキ・ローゼンタール",
        "https://yt3.ggpht.com/ytc/AKedOLT4XEPRFwXpb4gZ1qco_xCOt7ems7SrUsGOkmXX=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC1CfXB_kRs3C-zaeTG3oGyg": [
        "赤井はあと",
        "https://yt3.ggpht.com/rNj6bichsOoUjA2N9iXWxInEt9Y2Fo5fhG4S8oR17ip8ouCu_7wmX3PnQxt6OP6Rd9OlYXYcmw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCdn5BQ06XqgXoAxIhbqw5Rg": [
        "白上フブキ",
        "https://yt3.ggpht.com/ytc/AKedOLQmM8F8S-7GTcF5Lw7fBALF8FQC9yNKTb_nFHev2w=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCQ0UDLQCjY0rmuxCDE38FGg": [
        "夏色まつり",
        "https://yt3.ggpht.com/ytc/AKedOLQCXDfJbZoEZ-gtUiF4nSaGU8-qiq--BSTd92Sw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC1opHUrw8rvnsadT-iGp7Cg": [
        "湊あくあ",
        "https://yt3.ggpht.com/ytc/AKedOLTbU5ET3bgn0Iuz1jUBNjgSe9EW8kLxIhDUrtJlPw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCXTpFs_3PqI41qX2d9tL2Rw": [
        "紫咲シオン",
        "https://yt3.ggpht.com/AyUL9W0ltc_aJr_MysuZBx8hRfb1SIVNREgU9kiOO-lqmdhYkEsllmhagertVIwHwa3UAAKy=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC7fk0CB07ly8oSl0aqKkqFg": [
        "百鬼あやめ",
        "https://yt3.ggpht.com/XDGhKwPZcT16Ppg2gQmLHEIYRhw9sY4rqG0HWbeCH68LHkhlVQrrFgxd5hWUuMb2nLfDOhu6=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC1suqwovbL1kzsoaZgFZLKg": [
        "癒月ちょこ",
        "https://yt3.ggpht.com/ytc/AKedOLQn_VxZ1ApMgQahrkcTtSdSAr6Jpxi4eHQiMnIlsw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCvzGlP9oQwU--Y0r9id_jnA": [
        "大空スバル",
        "https://yt3.ggpht.com/ytc/AKedOLTf1BZdgOX5oC0SB-B_Uq16OlomzqRH81ADPPlPcA=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCp-5t9SrOQwXMU7iIjQfARg": [
        "大神ミオ",
        "https://yt3.ggpht.com/ytc/AKedOLRP0h31urAKtYcu_j1foVuGyPU65_Y-VNBqLgHB5Q=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCvaTdHTWBGv3MKj3KVqJVCw": [
        "猫又おかゆ",
        "https://yt3.ggpht.com/ytc/AKedOLT_TLZsRHyNXj_3v1QIfF5Z1LOEIKQPL_7HGH29=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UChAnqc_AY5_I3Px5dig3X1Q": [
        "戌神ころね",
        "https://yt3.ggpht.com/ytc/AKedOLSegxVNNn4QGDwO-jO89ZDcYLSyPUQS3a4KU6QPCw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC1DCedRgGHBdm81E1llLhOQ": [
        "兎田ぺこら",
        "https://yt3.ggpht.com/ytc/AKedOLSmHTeNNQp8A4AwsUPKzBa2ubDBWe6RSaG39mAYTw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCl_gCybOJRIgOXw6Qb4qJzQ": [
        "麗羽るしあ",
        "https://yt3.ggpht.com/ytc/AKedOLR1en3cN55loPrFL1C5K19o5xGhcKkmr0noD4cO=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCvInZx9h3jC2JzsIzoOebWg": [
        "不知火フレア",
        "https://yt3.ggpht.com/d9aIrGtZR0eI4k1Wnev5f_R4llIBsWnQOjkdsqkMycoAxA3g_zz-jyeBl8tEHfbm1iTg0SJj=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCdyqAaZDKHXg4Ahi7VENThQ": [
        "白銀ノエル",
        "https://yt3.ggpht.com/ytc/AKedOLS1MTrG3Gn7-Vf_rVNAZ2Ou8KrmUGUXO6TmkLxe=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCCzUftO8KOVkV4wQG1vkUvg": [
        "宝鐘マリン",
        "https://yt3.ggpht.com/ytc/AKedOLRFcdtwPHqI4573geBEyNL5h93BxtH5cMy_aL4zUw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCZlDXzGoo7d44bwdNObFacg": [
        "天音かなた",
        "https://yt3.ggpht.com/TlH8nz5O9UYo5JZ_5fo4JfXdT18N0Ck27wWrulni-c1g5bwes0tVmFiSKICzI1SW7itaTkk9GA=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCqm3BQLlJfvkTsX_hvm0UmA": [
        "角巻わため",
        "https://yt3.ggpht.com/ytc/AKedOLRWpyqOZzCmuSfmKGNo8TD2L_IRUYSw1wyhHXw-=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC1uv2Oq6kNxgATlCiez59hw": [
        "常闇トワ",
        "https://yt3.ggpht.com/meRnxbRUm5yPSwq8Q5QpI5maFApm5QTGQV_LGblQFsoO0yAV4LI-nSZ70GYwMZ_tbfSa_O8MTCU=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCa9Y57gfeY0Zro_noHRVrnw": [
        "姫森ルーナ",
        "https://yt3.ggpht.com/O7m_5HMY_O8yxR3Jhn9cEO1fLNL_GifMERExnAmfY7JrdTRsTjNijTcNYTPN97Llj3zGn8Susw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCFKOVgVbGmX65RxO3EtH3iw": [
        "雪花ラミィ",
        "https://yt3.ggpht.com/ytc/AKedOLQDR06gp26jxNNXh88Hhv1o-pNrnlKrYruqUIOx=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCAWSyEs_Io8MtpY3m-zqILA": [
        "桃鈴ねね",
        "https://yt3.ggpht.com/bMBMxmB1YVDVazU-8KbB6JZqUHn4YzmFiQRWwEUHCeqm5REPW7HHQChC5xE6e36aqqnXgK4a=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCUKD-uaobj9jiqB-VXt71mA": [
        "獅白ぼたん",
        "https://yt3.ggpht.com/ytc/AKedOLQXr6MeUpHI0-yNZIAaGXHvBVowhCWMwGx-zXYs=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCK9V2B22uJYu3N7eR_BT9QA": [
        "尾丸ポルカ",
        "https://yt3.ggpht.com/ytc/AKedOLQI_iYxOpfP8bJklQ_VnS4a9jdrwRRlre_JP1Yp=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCENwRMx5Yh42zWpzURebzTw": [
        "ラプラス・ダークネス",
        "https://yt3.ggpht.com/roGS60A8a_lDbVakIg1JU3u3hbtjHSTilMGHMizuPKh7tuoY2nl46raxuW2f_83IKFGMjL6Z=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCs9_O1tRPMQTHQ-N_L6FU2g": [
        "鷹嶺ルイ",
        "https://yt3.ggpht.com/KO_kRAeAQ4C4M5xJDFOFHZ79ycCRfMxttefXIDFurZE2fsVPnmlHkMdM5zjEsUTH1i97xnxKNw=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC6eWCld0KwmyHFbAqK3V-Rw": [
        "博衣こより",
        "https://yt3.ggpht.com/DNC5rGjlwA4Ae7rhpPmkv_QdjJPl8AfpQT9NcXTLvPbbriL-Y0Ni-gYfFH8uoiF6Ay1EP9VnZAk=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UCIBY1ollUsauvVi4hW4cumw": [
        "沙花叉クロヱ",
        "https://yt3.ggpht.com/_xNtPLKQcQxMTnOr4tAcGz0GEeESsi0bQX9mJEP3fx_50a8GUfUyOG1eyLIld2cCz6GvKABwpQ=s88-c-k-c0x00ffffff-no-rj"
    ],
    "UC_vMYWcDjmfdpH6r4TTn1MQ": [
        "風真いろは",
        "https://yt3.ggpht.com/YK_UCAbw_pFBHSOw_LGWI-WCJDdvMP3y9mmODQ1IFEnNVvcf-M3-q22Db5TLWuAbfboMNFTMIg=s88-c-k-c0x00ffffff-no-rj"
    ],
}

webhook_url_Hololive = 'https://discord.com/api/webhooks/936235678939906049/agCK1XYhb_iIrFTISDa27eSGXWzRtKl5lLj0cZ716W92s6-lHgXGAUZd2C-IQvLNKUuA'
webhook_url_Hololive_yotei = 'https://discord.com/api/webhooks/936235678939906049/agCK1XYhb_iIrFTISDa27eSGXWzRtKl5lLj0cZ716W92s6-lHgXGAUZd2C-IQvLNKUuA'
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
                if(!broadcast_data[video]['starttime']):
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
