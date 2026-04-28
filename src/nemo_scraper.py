import requests
import pandas as pd
import sqlite3
import os

def scrape_nemo():
    # API URL 설정
    url = "https://www.nemoapp.kr/api/store/search-list"
    
    # 공통 헤더 설정
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    all_items = []
    page_index = 1
    
    while True:
        params = {
            "Subway": "222",
            "Radius": "1000",
            "CompletedOnly": "false",
            "NELat": "37.626497913782195",
            "NELng": "127.38606088945265",
            "SWLat": "37.27536124492425",
            "SWLng": "126.9455178909255",
            "Zoom": "15",
            "SortBy": "29",
            "PageIndex": str(page_index)
        }
        
        print(f"페이지 {page_index} 수집 중...")
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            items = data.get("items", [])
            if not items:
                print("더 이상 수집할 데이터가 없습니다.")
                break
                
            all_items.extend(items)
            print(f"현재까지 총 {len(all_items)}개 아이템 수집 완료.")
            
            page_index += 1
            # 서버 부하를 줄이기 위한 짧은 대기
            import time
            time.sleep(0.5)
            
        except Exception as e:
            print(f"페이지 {page_index} 수집 중 오류 발생: {e}")
            break

    if not all_items:
        print("수집된 데이터가 전혀 없습니다.")
        return

    try:
        # pandas json_normalize를 사용하여 딕셔너리 구조 평탄화
        df = pd.json_normalize(all_items)
        
        # 리스트 형태인 컬럼들은 문자열로 변환
        import json
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, list)).any():
                df[col] = df[col].apply(lambda x: json.dumps(x, ensure_ascii=False) if isinstance(x, list) else x)
        
        # data 폴더 확인 및 생성
        os.makedirs("data", exist_ok=True)
        db_path = os.path.join("data", "nemo_data.db")
        
        # SQLite DB에 저장
        print(f"총 {len(df)}개의 데이터를 {db_path}에 저장 중...")
        with sqlite3.connect(db_path) as conn:
            df.to_sql("stores", conn, if_exists="replace", index=False)
        print("저장이 완료되었습니다.")
            
    except Exception as e:
        print(f"데이터 처리 또는 저장 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    scrape_nemo()
