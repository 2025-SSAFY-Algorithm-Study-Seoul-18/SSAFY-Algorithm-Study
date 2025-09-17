# 개인 브랜치 워크플로우
🔄 브랜치 작업 방식
1단계: 개인 브랜치 생성 및 설정

```bash
# main에서 최신 상태로 업데이트
git checkout main
git pull origin main

# 개인 브랜치 생성 (날짜 기반)
git checkout -b feature/본인이름-1201

# 본인 폴더만 작업 (다른 폴더는 건드리지 않음)
# members/본인이름/ 에서만 작업
2단계: 파일 추가 및 커밋
```

```bash
# 본인 폴더에만 파일 추가
git add members/본인이름/BOJ/BOJ_1234_스택.py
git commit -m "feat: BOJ_1234_스택 문제 해결"

git add members/본인이름/Programmers/PGS_L2_괄호변환.py
git commit -m "feat: PGS_L2_괄호변환 문제 해결"

# 다른 멤버 폴더는 절대 건드리지 않음
# members/다른사람/ 폴더는 수정하지 않음
3단계: PR 생성
```
```bash
git push origin feature/본인이름-1201
# GitHub에서 PR 생성
# 변경사항을 확인하여 본인 폴더만 포함되었는지 체크
```