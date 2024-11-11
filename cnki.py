from DrissionPage import ChromiumPage
from urllib.parse import unquote
import time
from lxml import etree

def get_metadata(d):
    r = {}
    for i in d:
        r[i["name"]] = i["value"]
    return r

def get_metrics(d):
    r = {}
    for i in d:
        r[i["name"]] = i["value"]
    return r

page = ChromiumPage()
page.listen.start(["group/singleresult", "kns8s/brief/grid","group/result"])
page.get("https://kns.cnki.net/kns8s/AdvSearch")
print("等待搜索")
while True:
    arti = page.eles(
        'xpath://*[@id="gridTable"]/div/div/div/table/tbody/tr[1]', timeout=1
    )
    if arti:
        break
print("搜索完成")

# 获取各分类数量
category_count = {}
category_list = []
doctype_menus = page.eles(
    'xpath://ul[contains(@class,"doctype-menu")]//a[@name="classify"]', timeout=2
)
for i in doctype_menus:
    t = i.ele("xpath://span").text
    n = i.ele("xpath://em").text
    category_count[t] = n
    category_list.append({"value": n, "name": t})

# 侧边计数点击
divGroups = page.eles('xpath://div[@id="divGroup"]/dl/dt[@class="tit"]/b')
for i in divGroups:
    i.click(by_js=True)

# 翻页
while True:
    PageNext = page.ele("#PageNext", timeout=2)
    if PageNext:
        PageNext.click()
        time.sleep(1)
    else:
        break

# 获取监听数据
subject_count = {}  # 左侧分类计数
subject_count_list = {}  # 左侧分类计数列表
search_author_url = {}
articles = []  # 文章列表
for i in page.listen.steps(timeout=2):
    url = i.request.url
    data = i.response.body
    if "kns8s/brief/grid" in url:  # 主体内容
        h = etree.HTML(data)
        items = h.xpath('//table[@class="result-table-list"]/tbody/tr')
        for item in items:
            temp = {}
            temp["url"] = item.xpath('./td[@class="name"]//a/@href')[0]
            temp["title"] = item.xpath('./td[@class="name"]//a/text()')[0]
            authors = []
            author = item.xpath('./td[@class="author"]//a')
            for i in author:
                author_url = i.xpath("./@href")[0]
                author_name = i.xpath(".//text()")[0]

                if "javascript" in author_url:
                    authors = [
                        {"name": i, "url": None}
                        for i in "".join(i.xpath(".//text()")).split("，")
                    ]
                else:
                    if i.xpath('./font[@color="red"]'):
                        search_author_url[author_name] = author_url
                    authors.append({"name": author_name, "url": author_url})

            temp["author"] = item.xpath('./td[@class="author"]//a//text()')
            temp["source"] = item.xpath('./td[@class="source"]//a/text()')[0]
            temp["date"] = item.xpath('./td[@class="date"]//text()')[0]  # 时间
            temp["data"] = item.xpath('./td[@class="data"]//span/text()')  # 数据库
            temp["data"] = temp["data"][0] if temp["data"] else None
            temp["quote"] = item.xpath('./td[@class="quote"]//span/text()')
            temp["quote"] = temp["quote"][0] if temp["quote"] else None
            temp["download"] = item.xpath('./td[@class="download"]//a/text()')  # 下载
            temp["download"] = temp["download"][0] if temp["download"] else None
            articles.append(temp)
    elif "group/singleresult" in url:  # 左侧计数信息
        h = etree.HTML(data)
        tit = h.xpath("//dd/@tit")[0]
        items = h.xpath("//li")
        temp = {}
        temp_list = []
        for item in items:
            name = item.xpath("./a/text()")[0]
            value = item.xpath("./span/text()")[0]
            value = value.replace("(", "").replace(")", "")
            if "万" in value:
                value = float(value.replace("万", "")) * 10000
            temp[name] = float(value)
            temp_list.append({"name": name, "value": float(value)})
        subject_count[tit] = temp
        subject_count_list[tit] = temp_list
    elif 'group/result' in url:  # 左侧计数信息
        h = etree.HTML(data)
        items = h.xpath('//dl/dd')
        for item in items:
            tit = item.xpath("./@tit")[0]
            listitem = item.xpath(".//ul/li")
            if not listitem:
                continue
            temp = {}
            temp_list = []
            for li in listitem:
                name = li.xpath("./a/text()")[0]
                value = li.xpath("./span/text()")[0]
                value = value.replace("(", "").replace(")", "")
                if "万" in value:
                    value = float(value.replace("万", "")) * 10000
                temp[name] = float(value)
                temp_list.append({"name": name, "value": float(value)})
            subject_count[tit] = temp
            subject_count_list[tit] = temp_list
            
               
subject_count_percent = {}
for k, v in subject_count.items():
    value_sum = sum(v.values())
    print(k, value_sum, v.values())
    subject_count_percent[k] = {key: round(value / value_sum * 100, 2) for key, value in v.items()}
 
page.listen.stop()



# 计量可视化分析

anisys_all = page.ele('xpath://li[@id="anisys_all"]')
anisys_all.click(by_js=True)
time.sleep(1)


while True:
    try:
        anisys_tab = page.get_tab(title="计量可视化分析")
        break
    except:
        time.sleep(1)
anisys_tab.listen.start(["getGroupData"])
anisys_tab.refresh()
while True:
    j = anisys_tab.eles("基金", timeout=0.2)
    time.sleep(0.5)
    if j:
        break
time.sleep(2)
anisys_data = {}
for i in anisys_tab.listen.steps(timeout=5):
    url = i.request.url
    postData = unquote(i.request.postData)
    print(url, postData.split("&")[3].split("=")[1])
    data = i.response.body
    if not data:
        continue
    for d in data:
        if "y" in d:
            d["value"] = d["y"]
    if "getGroupData" in url:
        anisys_data[postData.split("&")[3].split("=")[1]] = data
anisys_tab.close()

result = {
    "category_count": category_list,
    "subject_count": subject_count_list,
    "subject_count_dict": subject_count,
    "subject_count_percent":subject_count_percent,
    "search_author_url": search_author_url,
    "search_author_info": [],
    "articles":articles,
}


# 获取用户信息
def get_user_info(
    name=None,
    url="https://kns.cnki.net/kcms2/author/detail?v=Nyg97wmOeE7B23i7DB-Wq31WeINiF06xmgTmoBoMx0sXtkAxZJoDot5NMIzLQfaSh-HhvifSwPKRh-ZDhdGYQAYlnz35f_S2ZwyPVVXbED3805Z7yyKKIC4yiYR3YObe&uniplatform=NZKPT&language=CHS",
):
    userinfo = {
        "funds_rank": [],
        "coauthors_nodes": [],
        "coauthors_links": [],
        "quote_rank": [],
        "download_rank": [],
        "conferences_rank": [],
        "journals_rank": [],
        "domains":[],
    }

    try:
        author_tab = page.get_tab(title="作者")
    except:
        author_tab = page.new_tab()
    author_tab.listen.start("experts")
    author_tab.get(url)
    for i in range(50):
        time.sleep(1)
        author_tab.scroll.to_bottom()
        recvideotitle = author_tab.ele('xpath://h2[@id="recvideotitle"]', timeout=0.5)
        if recvideotitle:
            print("到底了")
            break

    author_data = {}
    author_data["names"] = {
        "detail": "作者详情",
        "query": "同名作者",
        "domains": "作者关注领域",
        "quote_rank": "最高被引",
        "download_rank": "最高下载",
        "journal": "发表在期刊的文献",
        "meeting": "发表在会议的文献",
        "thesis": "发表在硕博的文献",
        "newspaper": "发表在报纸的文献",
        "max_pubjournals": "最高发表期刊",
        "max_pubconferences": "最高发表会议",
        "max_pubdegreeunits": "最高发表硕博",
        "max_pubnewspapers": "最高发表报纸",
        "overReferences": "曾参考文献",
        "tutors": "导师",
        "coauthors": "合作者",
        "funds": "作者基金",
        "videos": "视频",
    }
    for i in author_tab.listen.steps(timeout=2):
        url = i.request.url
        t = url.split("?")[0].split("/")[-1]
        data = i.response.body
        params = i.request.params
        if "detail" in url:  # 作者详情
            author_data["detail"] = data.get("data", {})
        elif "query" in url:  # 同名作者
            userinfo["query"] = data.get("data", {})
        elif "domains" in url:  # 作者关注领域
            author_data["domains"] = data.get("data", {}).get("data", {})
        elif "resources" in url:

            resource = params.get("resource")
            sequence = params.get("sequence")
            if resource == "SCDB" and sequence == "CF":  # 最高被引
                author_data["quote_rank"] = data.get("data", {}).get("data", {})
                userinfo["pub_count"] = data.get("data", {}).get("total", None)
            elif resource == "SCDB" and sequence == "DFR":  # 最高下载
                author_data["download_rank"] = data.get("data", {}).get("data", {})
            elif resource == "CJFD" and sequence == "PT":  # 发表在期刊的文献
                author_data["journal"] = data.get("data", {}).get("data", {})
                userinfo["journal_count"] = data.get("data", {}).get("total", None)
            elif resource == "CIPD" and sequence == "PT":  # 发表在会议的文献
                author_data["meeting"] = data.get("data", {}).get("data", {})
                userinfo["meeting_count"] = data.get("data", {}).get("total", None)
            elif resource == "CDMD" and sequence == "PT":  # 发表在硕博的文献
                author_data["thesis"] = data.get("data", {}).get("data", {})
                userinfo["thesis_count"] = data.get("data", {}).get("total", None)
            elif resource == "CCND" and sequence == "PT":  # 发表在报纸的文献
                author_data["newspaper"] = data.get("data", {}).get("data", {})
                userinfo["newspaper_count"] = data.get("data", {}).get("total", None)
        elif "publications" in url:  # 发表文献
            if params.get("type") == "journals":  # 最高发表期刊
                author_data["max_pubjournals"] = data.get("data", {}).get("data", {})
            elif params.get("type") == "conferences":  # 最高发表会议
                author_data["max_pubconferences"] = data.get("data", {}).get("data", {})
            elif params.get("type") == "degreeunits":  # 最高发表在硕博的文献的单位
                author_data["max_pubdegreeunits"] = data.get("data", {}).get("data", {})
            elif params.get("type") == "newspapers":  # 最高发表在报纸的文献的单位
                author_data["max_pubnewspapers"] = data.get("data", {}).get("data", {})
        elif "literature/overReferences" in url:  # 曾参考文献
            author_data["overReferences"] = data.get("data", {}).get("data", {})
        elif "tutors" in url:  # 作者导师
            author_data["tutors"] = data.get("data", [])
        elif "coauthors" in url:  # 作者合作
            author_data["coauthors"] = data.get("data", {}).get("data", {})
        elif "funds" in url:  # 作者基金
            author_data["funds"] = data.get("data", {}).get("data", {})
        elif "videos" in url:  # 作者视频
            author_data["videos"] = data.get("data", {}).get("data", {})

    author_tab.close()

    metadata = {}
    metadata["url"] = author_data["detail"]["relations"][0]["url"]

    for i in author_data["detail"]["metadata"]:
        metadata[i["name"]] = i["value"]
    userinfo["author"] = {
        "cnki_id": metadata["CODE"],
        "id": metadata["NAME"],
        "name": metadata["NAME"],
        "value": sum(int(j["value"]) for j in author_data["detail"]["metrics"]),
        "symbolSize": sum(int(j["value"]) for j in author_data["detail"]["metrics"]) / 5000,
        "itemStyle": {"borderWidth": 1, "borderColor": "#fff"},
        "label": {
            "show": True,
        },
        "url": metadata["url"],
    }
    
    
    for i in author_data["domains"]:
        userinfo["domains"].append({
            "name": i["item"],
            "url": i["relations"][0]["url"],
        })
    
    for i in author_data["detail"]["metrics"]:
        userinfo["author"][i["name"]] = i["value"]
    userinfo["coauthors_nodes"].append(userinfo["author"])

    for i in author_data["funds"]:
        userinfo["funds_rank"].append(
            {
                "name": i["title"],
                "value": i["metrics"][0]["value"],
                "PUC": i["metrics"][0]["value"],
                "url": i["relations"][0]["url"],
            }
        )
    for i in author_data["coauthors"]:
        userinfo["coauthors_nodes"].append(
            {
                "cnki_id": i["id"],
                "id": i["title"],
                "name": i["title"],
                "value": sum(int(j["value"]) for j in i["metrics"]),
                "symbolSize": sum(int(j["value"]) for j in i["metrics"]) / 5000,
                "PUC": i["metrics"][0]["value"],
                "DTC": i["metrics"][1]["value"],
                "CTC": i["metrics"][2]["value"],
                "url": i["relations"][0]["url"],
                "label": {
                    "show": True,
                },
            }
        )
        userinfo["coauthors_links"].append(
            {
                "source": userinfo["author"]["name"],
                "target": i["title"],
            }
        )

    for i in author_data["quote_rank"]:
        md = get_metadata(i["metadata"])
        metrics = get_metrics(i["metrics"])
        authors = []
        for author in i["authors"]:
            authors.append(
                {
                    "name": author["title"],
                    "url": (
                        author["relations"][0]["url"] if author["relations"] else None
                    ),
                    "cnki_id": author.get("id", None),
                }
            )
        userinfo["quote_rank"].append(
            {
                "title": md["TI"],
                "authors": authors,
                "metrics": metrics,
                "url": i["relations"][0]["url"] if i["relations"] else None,
                "metadata": md,
            }
        )
    for i in author_data["download_rank"]:
        md = get_metadata(i["metadata"])
        metrics = get_metrics(i["metrics"])
        authors = []
        for author in i["authors"]:
            authors.append(
                {
                    "name": author["title"],
                    "url": (
                        author["relations"][0]["url"] if author["relations"] else None
                    ),
                    "cnki_id": author.get("id", None),
                }
            )
        userinfo["download_rank"].append(
            {
                "title": md["TI"],
                "authors": authors,
                "metrics": metrics,
                "url": i["relations"][0]["url"] if i["relations"] else None,
                "metadata": md,
            }
        )

    for i in author_data["max_pubconferences"]:
        metrics = get_metrics(i["metrics"])
        userinfo["conferences_rank"].append(
            {
                "name": i["title"],
                "Value": metrics["PUC"],
                "url": i["relations"][0]["url"] if i["relations"] else None,
            }
        )

    for i in author_data["max_pubjournals"]:
        metrics = get_metrics(i["metrics"])
        userinfo["journals_rank"].append(
            {
                "name": i["title"],
                "Value": metrics["PUC"],
                "url": i["relations"][0]["url"] if i["relations"] else None,
            }
        )

    return userinfo


for i in search_author_url:
    userinfo = get_user_info(i)
    result["search_author_info"].append(userinfo)


# 获取所有文章信息
# try:
#     article_tab = page.get(url='article/abstract')
# except:
#     article_tab = page.new_tab()
# for index,a in enumerate(articles):
#     if not a.get('detail'):
#         time.sleep(3)
#         article_tab.get(a['url'])
#         print(a['title'], a['url'])
#         desc = article_tab.eles('xpath://div[@class="doc"]//div[@class="row"]')
#         r = []``
#         for i in (desc):
#             # print(i.text)
#             if '摘要' in i.text:
#                 r.append('摘要')
#                 r.append(i.text.split('摘要', 1)[1].strip())
#             elif '：' in i.text or '\n' in i.text:
#                 for j in i.text.split('：'):
#                     for k in j.split('\n'):
#                         if k != '':
#                             r.append (k.strip())
#             else:
#                 r.append(i.text.strip())
#         r = {r[i]:r[i+1] for i in range(0,len(r),2)}
#         print(r)
#         articles[index]['detail'] = r

# 保存数据

page.close()

import json


# with open("subject_count.json", "w", encoding="utf-8") as f:
#     json.dump(subject_count, f, ensure_ascii=False, indent=4)
# with open("articles.json", "w", encoding="utf-8") as f:
#     json.dump(articles, f, ensure_ascii=False, indent=4)
# with open("anisys_data.json", "w", encoding="utf-8") as f:
#     json.dump(anisys_data, f, ensure_ascii=False, indent=4)
# with open("category_count.json", "w", encoding="utf-8") as f:
#     json.dump(category_count, f, ensure_ascii=False, indent=4)

with open("result_subject.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)