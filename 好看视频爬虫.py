import requests

def get_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
    else:
        print('请求失败')
    return data


# 获取视频列表
def get_video_list(data):
    video_lists = data['data']['response']['videos']
    return video_lists


def save_vedio(vedio_lists):
    # page = 0
    # while True:
    #     page += 1
    #     print('=' * 20 + '正在下载第{}页'.format(page) + '='*20)
    for vedio_list in vedio_lists:
        try:
            vedio_url = vedio_list['play_url']
            vedio_title = vedio_list['title'] + '.mp4'
            time.sleep(5)
​
            vedio = requests.get(vedio_url, headers=headers).content
            if not os.path.exists('vedio'):
                os.mkdir('vedio')
            with open('./vedio/{}'.format(vedio_title), mode='wb') as f:
                f.write(vedio)
​
        except Exception as e:
            break
    print('下载完成\n\n')


print(get_data(url))
