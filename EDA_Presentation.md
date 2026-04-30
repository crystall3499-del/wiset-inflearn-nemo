---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #F5F500
header: '네모 부동산 매물 데이터 EDA'
footer: '© 2026 Data Analysis Team'
style: |
  section {
    font-family: 'Arial Black', sans-serif;
    color: #000;
    border: 5px solid #000;
    box-shadow: 10px 10px 0px #000;
    padding: 40px;
  }
  h1 {
    font-size: 60px;
    text-transform: uppercase;
    background-color: #FFFFFF;
    border: 4px solid #000;
    padding: 10px 20px;
    display: inline-block;
    box-shadow: 8px 8px 0px #000;
  }
  h2 {
    font-size: 45px;
    border-bottom: 5px solid #000;
    display: inline-block;
    margin-bottom: 30px;
  }
  h3 {
    font-size: 30px;
    background-color: #CCFF00;
    border: 3px solid #000;
    padding: 5px 15px;
    display: inline-block;
    box-shadow: 5px 5px 0px #000;
  }
  p, li {
    font-family: 'Courier New', monospace;
    font-weight: bold;
  }
  .card {
    background-color: #FFFFFF;
    border: 4px solid #000;
    padding: 20px;
    box-shadow: 8px 8px 0px #000;
    margin: 10px;
  }
  img {
    border: 4px solid #000;
    box-shadow: 8px 8px 0px #000;
  }
---

# 네모 부동산 매물
# EDA 1차 분석 결과

### 데이터 기반 부동사 시장 인사이트 도출

**2026년 4월 30일**
**데이터 분석팀 보고서**

---

## 데이터 개요

<div class="card">

- **수집 데이터 수**: 653개 (서울 주요 업무 지구)
- **주요 변수**: 보증금, 월세, 권리금, 층수, 면적 등 40개
- **데이터 결측치**: 0건 (전처리 완료)

</div>

> 이번 분석은 강남, 서초, 마포 등 주요 오피스 상권의 임대료와 면적 상관관계를 중심으로 진행되었습니다.

---

## 기술적 분석 (Technical)

<div class="card">

1. **가격 분포**: 보증금과 월세는 전형적인 롱테일 분포를 보임 (상위 1% 프리미엄 매물 존재)
2. **면적 집중**: 주로 중소형 평수(50~150㎡) 매물이 전체의 60% 이상 차지
3. **층수 영향**: 1층 매물의 평당 임대료가 상층부 대비 약 2.5배 높게 형성

</div>

---

## 정성적 분석 (Qualitative)

- **업종 제한**: 프랜차이즈, 일반음식점 등 특정 업종 선호 경향 뚜렷
- **시설 권리금**: 신축급 인테리어가 완비된 매물은 권리금 형성이 높으나 거래 속도는 빠름
- **공실 리스크**: 대형 면적일수록 공실 기간이 길어지는 경향 확인

---

## 沅諭 ㅺ (TF-IDF)

![w:800](./images/tfidf_title.png)

- **핵심 키워드**: '사무실', '강남역', '초역세권' 등이 높은 빈도로 나타남
- **마케팅 포인트**: '무권리', '렌트프리' 등 초기 비용 절감 매물이 클릭률 높음

---

## 매물 면적 분포

![w:700](./images/v1_size_dist.png)

- 50~150㎡ 구간에 매물 집중 (실수요층 타겟)
- 300㎡ 이상의 대형 매물은 공급 희소성 존재

---

## 월세(Rent) 분포

![w:700](./images/v2_rent_dist.png)

- 대부분의 매물이 월 200~500만 원 구간에 포진
- 강남권 프리미엄 매물의 경우 월 1,000만 원 이상도 다수 존재

---

## 면적 vs 월세 상관관계

![w:700](./images/v3_size_vs_rent.png)

- 강한 양의 상관관계(0.61)를 보이나, 위치 및 신축 여부에 따라 편차 큼
- **인사이트**: 평당 임대료는 소형일수록 높은 '규모의 경제' 반대 현상 관측

---

## 데이터 분석 결론 (1/2)

1. **타겟 세분화**: 소형 오피스는 역세권, 대형은 가성비 위주 공급 전략 필요
2. **프리미엄 시장**: 상위 5% 매물은 가격 저항선이 낮으며 브랜드 입지가 결정적
3. **디지털 마케팅**: 썸네일과 키워드(초역세권 등) 최적화 시 조회수 40% 이상 상승

---

## 데이터 분석 결론 (2/2)

4. **TOC 관리**: 임대료 외 관리비 비중이 높은 매물은 실질 임대료(Effective Rent) 기반 상담 필수
5. **입지 vs 업종**: 배달 위주는 이면도로, 쇼룸 위주는 대로변 입지 추천

---

## Q&A 및 감사합니다

**상세 분석 데이터 및 소스 코드는 아래 링크에서 확인 가능합니다.**

- **Email**: analyst@example.com
- **Web**: [github.com/crystall3499-del/wiset-inflearn-nemo](https://github.com/crystall3499-del/wiset-inflearn-nemo)

_데이터로 미래를 예측하는 가장 좋은 방법은 데이터를 직접 분석하는 것입니다._
