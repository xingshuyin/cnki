import time
from lxml import html
def get_lunwen(download=False, max_page=10, download_path='C:\\Users\\li\\Desktop\\论文'):
    import os
    from lxml import html
    import pandas as pd
    if not os.path.exists(download_path):
        os.mkdir(download_path)

    from DrissionPage import ChromiumPage, ChromiumOptions
    import time
    co = ChromiumOptions()
    # co.no_imgs(True).mute(True)
    # co.headless()
    # co.set_argument('--no-sandbox')
    results= []
    broswer = ChromiumPage(co)
    detail = broswer.new_tab()
    broswer.get("https://kns.cnki.net/kns8s/AdvSearch")
    for page in range(max_page):
        while True:
            arti = broswer.eles('xpath://*[@id="gridTable"]/div/div/div/table/tbody/tr[1]')
            if arti:
                break
            time.sleep(2)
            print(1)
            
        arti = broswer.eles('xpath://*[@id="gridTable"]/div/div/div/table/tbody/tr')
        for index, i in enumerate(arti):
            print(index+1)

            title = i.ele('css:.fz14').html
            title = ''.join(html.fromstring(title).xpath('//text()')).strip()
            
            source = i.ele('css:.source').html
            source = ''.join(html.fromstring(source).xpath('//text()')).strip()
            
            t = i.ele('css:.date').html
            t = ''.join(html.fromstring(t).xpath('//text()')).strip()    
            
            quote = i.ele('css:.quote').html
            quote = ''.join(html.fromstring(quote).xpath('//text()')).strip()  
            
            download_count = i.ele('css:.download').html
            download_count = ''.join(html.fromstring(download_count).xpath('//text()')).strip()  
            
            databse = i.ele('css:.data').html
            databse = ''.join(html.fromstring(databse).xpath('//text()')).strip()
            
            
            url = i.ele('css:.fz14').link
            print(index+1, title, source, t, databse, quote, download_count, url)
            if databse not in ['期刊', '硕士', '报纸']:
                continue
            detail.get(url)
            ChDivSummaryMore = detail.ele('css:#ChDivSummaryMore')
            if ChDivSummaryMore:
                if ChDivSummaryMore.states.has_rect:
                    ChDivSummaryMore.click()
            if databse=='期刊':
            # time.sleep(2)
                ChDivSummary = detail.ele('css:#ChDivSummary').text
                author = detail.ele('css:.author').text
                keywords= detail.ele('css:.keywords').text
                zhuanji = detail.ele('专辑：').next('tag:p').text
                zhuanti = detail.ele('专题：').next('tag:p').text
                fenleihao = detail.ele('分类号：').next('tag:p').text
                # banhao = None
                # DOI = detail.ele('DOI：').next('tag:p').text
            elif databse=='报纸':
                ChDivSummary = detail.ele('css:.abstract-text').text
                author = detail.ele('css:.author').text
                keywords= detail.ele('css:.keywords').text
                zhuanji = detail.ele('专辑：').next('tag:p').text
                zhuanti = detail.ele('专题：').next('tag:p').text
                fenleihao = None
                # banhao = detail.ele('版号：').next('tag:p').text
                # DOI = detail.ele('DOI：').next('tag:p').text
            elif databse=='硕士':
                ChDivSummary = detail.ele('css:.abstract-text').text
                author = detail.ele('css:.author').text
                keywords= detail.ele('css:.keywords').text
                zhuanji = detail.ele('专辑：').next('tag:p').text
                zhuanti = detail.ele('专题：').next('tag:p').text
                fenleihao = None
                # banhao = detail.ele('版号：').next('tag:p').text
                # DOI = detail.ele('DOI：').next('tag:p').text
            else:
                continue
            print(index+1, ChDivSummary, zhuanji)
            if download:
                pdf_down = detail.ele('#pdfDown')
                if pdf_down:
                    mission = pdf_down.click.to_download(download_path, title+'.pdf')
                    mission.wait()
                else:
                    print('pdf下载失败')
            results.append({
                '标题': title if title else None,
                '作者': author if author else None,
                '来源': source if source else None,
                'url':url if url else None,
                '时间': t if t else None,
                '数据库': databse if databse else None,
                '被引': quote if quote else None,
                '下载': download_count if download_count else None,
                '摘要': ChDivSummary if ChDivSummary else None,
                '关键词': keywords if keywords else None,
                '专辑': zhuanji if zhuanji else None,
                '专题': zhuanti if zhuanti else None,
                '分类号': fenleihao if fenleihao else None,
                # '版号':banhao if banhao else None,
                # 'DOI':DOI,
            })

        next = broswer.ele('#PageNext')
        if next:
            next.click()
        else:
            break
    broswer.close()
    d  = pd.DataFrame(results)
    d.to_excel(download_path+'\\'+'lunwen.xlsx', index=False)
    
def merge_pdf():
    import os
    from PyPDF2 import PdfMerger
    # pip3 install PyPDF2
    # pip install pycryptodome
    target_path = r'C:\Users\xingshuyin\Documents\WeChat Files\wxid_xe18fcqg80qt22\FileStorage\File\2024-05\新建文件夹(1)'
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
    pdf_lst.sort(key=lambda x: int(x.split('.')[0]))
    print(pdf_lst)
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfMerger()
    for pdf in pdf_lst:
        file_merger.append(pdf)     # 合并pdf文件

    file_merger.write(r"C:\Users\xingshuyin\Desktop\merged2.pdf")


def pdf_to_word():
    # pip install pdf2docx
    from pdf2docx import Converter

    pdf_file = r'C:\Users\xingshuyin\Desktop\merged2.pdf'
    docx_file = r'C:\Users\xingshuyin\Desktop\merged.docx'

    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file) # 默认参数start=0, end=None
    cv.close()


if __name__ == '__main__':
    get_lunwen()
    # merge_pdf()
    # pdf_to_word()
