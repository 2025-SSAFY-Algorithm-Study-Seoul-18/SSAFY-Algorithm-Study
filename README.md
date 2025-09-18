# 🚀 Algorithm Study

> 매일 꾸준한 알고리즘 학습을 통한 실력 향상을 목표로 하는 스터디입니다.

## 📋 스터디 규칙

### 일일 목표
- **IM 난이도**: 3~5문제
- **A 난이도**: 2~3문제
- **사용 플랫폼**: 백준(메인), 프로그래머스, 코드트리, SWEA

### 진행 방식
1. **매일**: 개인 브랜치에서 문제 풀이 후 PR 생성
2. **온라인**: 간략한 코드 리뷰 진행
3. **오프라인 미팅**: 심화 코드 리뷰 (본인이 선택한 PR만)

## 👥 스터디원

| Name | GitHub | 역할 | 알고리즘 등급 |
|------|--------|-----------|---|
| 심미진 | [@azure-553](- [https://github.com/azure-553) |] 팀장 | X |
| 이준영 | [@junDevCodes](- [https://github.com/junDevCodes) | 팀원] | IM |
| 류연승 | [@winifred114](https://github.com/winifred114) | 팀원 | A |
| 송준서 | [@Junseo5](https://github.com/Junseo5) | 팀원 | A |
| ... | ... | ... |

## 📁 폴더 구조 및 네이밍 규칙

### 파일 명명 규칙
- **백준**: `BOJ_문제번호_문제명.확장자` (예: `BOJ_1234_스택.py`)
- **프로그래머스**: `PGS_레벨_문제명.확장자` (예: `PGS_L2_괄호변환.py`)
- **코드트리**: `CT_문제명.확장자` (예: `CT_트리순회.cpp`)
- **SWEA**: `SWEA_문제번호_문제명.확장자` (예: `SWEA_1234_암호.java`)

### 커밋 메시지 규칙
|타입 이름|내용|
|---|---|
|feat|	새로운 기능에 대한 커밋|
|fix|	버그 수정에 대한 커밋|
|build|	빌드 관련 파일 수정 / 모듈 설치 또는 삭제에 대한 커밋|
|chore|	그 외 자잘한 수정에 대한 커밋|
|ci|	ci 관련 설정 수정에 대한 커밋|
|docs|	문서 수정에 대한 커밋|
|style|	코드 스타일 혹은 포맷 등에 관한 커밋|
|refactor|	코드 리팩토링에 대한 커밋|
|test|	테스트 코드 수정에 대한 커밋|
|perf|	성능 개선에 대한 커밋|

- **ex)** feat: BOJ_1234_스택 문제 해결
- **ex)** refactor: PGS_L2_괄호변환 시간복잡도 개선
- **ex)** docs: week01 회고 작성

## 🔄 PR 규칙

### PR 제목 형식
`(MM/DD) 이름 - 일일 문제풀이`

### PR 내용 (템플릿 사용)
- 풀이한 문제 목록
- 어려웠던 점
- 새로 배운 개념
- 리뷰 받고 싶은 문제 (오프라인용)

### 브랜치 전략
- `main`: 모든 멤버의 승인된 코드 통합
- `feature/@username`: 개인 작업 브랜치
- 브랜치명 예시: `feature/azure-553`

### 개인 브랜치 관리 방식
- 각자 **본인 members/@username/ 폴더만** 작업
- PR시 **본인 폴더 변경사항만** 포함
- main 브랜치에는 **전체 멤버 통합 관리**

## 📚 학습 자료

### 플랫폼별 문제 추천
<details>
<summary>📘 백준 알고리즘 IM 대비</summary>

- [백준 알고리즘 IM 대비 1](https://www.acmicpc.net/workbook/view/23765)  
- [백준 알고리즘 IM 대비 2](https://www.acmicpc.net/workbook/view/14608)  
- [백준 알고리즘 IM 대비 3](https://www.acmicpc.net/workbook/view/8399)  
- [백준 알고리즘 IM 대비 4](https://www.acmicpc.net/workbook/view/14613)  
- [백준 알고리즘 IM 대비 5](https://www.acmicpc.net/workbook/view/7091)  
- [백준 알고리즘 IM 대비 6](https://www.acmicpc.net/workbook/view/19766)  
- [백준 알고리즘 IM 대비 7](https://www.acmicpc.net/workbook/view/19767)  

</details>

<details>
<summary>📙 백준 알고리즘 A형 대비</summary>

- [백준 알고리즘 A형 대비 1](https://www.acmicpc.net/workbook/view/2771)  
- [백준 알고리즘 A형 대비 2](https://www.acmicpc.net/workbook/view/1152)  
- [백준 알고리즘 A형 대비 3](https://www.acmicpc.net/workbook/view/13158)  
- [백준 알고리즘 A형 대비 4](https://www.acmicpc.net/workbook/view/13978)  
- [백준 알고리즘 A형 대비 5](https://www.acmicpc.net/workbook/view/3176)  
- [백준 알고리즘 A형 대비 6](https://www.acmicpc.net/workbook/view/15150)  

</details>

<details>
<summary>📕 백준 알고리즘 B형 대비</summary>

- [백준 알고리즘 B형 대비 1](https://www.acmicpc.net/workbook/by/ssomeones_coding)  
- [백준 알고리즘 B형 대비 2](https://www.acmicpc.net/workbook/view/2163)  

</details>

### 알고리즘 분류별 학습
- [ ] 구현
- [ ] 자료구조 (스택, 큐, 덱)
- [ ] 정렬
- [ ] 이분탐색
- [ ] BFS/DFS
- [ ] 그리디
- [ ] DP
- [ ] 그래프

## 📊 주간 통계

| 주차 | 참여자 수 | 총 해결 문제 수 | 평균 문제 수 |
|------|-----------|-----------------|--------------|
| 1주차 | 4명 | 0문제 | 0문제/인 |

## 🏆 이번 달 MVP

**ex)** **2024년 12월 MVP**: [멤버명] - 총 45문제 해결, 적극적인 코드 리뷰 참여

## 📞 연락처 및 미팅 정보

- **정기 미팅**: 매주 수요일 오후 6~8시
- **장소**: [카페]
- **온라인**: [zep 활용]
