from collections import defaultdict
import csv
import os
import requests
import time

def get_nginx_status():
    """
    nginx 상태 정보를 받아와 숫자 값 반환
    """
    res = requests.get("http://localhost:8949/nginx_status")
    res_text = res.text.split()
    return (int(i) for i in res_text if i.isdigit())

def count_status(res):
    """
    nginx 상태 정보를 딕셔너리로 변환
    """
    status = ["ac", "accepts", "handled", "requests", "reading", "writing", "waiting"]
    status_cnt = defaultdict(int)
    status_cnt["TimeStamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    
    for i, cnt in enumerate(res):
        status_cnt[status[i]] += cnt
    
    return status_cnt

def append_to_file(data):
    """
    csv 파일에 데이터 저장
    """
    file_path = "./note/nginx_stats/nginx_stats.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file_exists = os.path.exists(file_path)
    
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def execute_nginx_stats(duration):
    """
    입력한 시간 초 동안 10초마다 데이터 수집 후 저장
    """
    start_time = time.time()
    while (time.time() - start_time) < float(duration + 1):
        res = get_nginx_status()
        data = count_status(res)
        append_to_file(data)
        
        print(f"[{data['TimeStamp']}] nginx status logged.")
        
        time.sleep(10)

if __name__ == "__main__":
    duration = int(input("테스트 실행 시간: "))
    execute_nginx_stats(duration)