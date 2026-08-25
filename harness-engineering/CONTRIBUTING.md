# 기여 가이드

## 브랜치

```
main                 항상 배포 가능한 상태
feat/<범위>-<요약>    기능 추가        예) feat/router-fallback
prompt/<id>-<요약>    프롬프트 변경    예) prompt/sys-orchestrator-tone
eval/<범위>           평가셋 추가·수정
fix/<요약>            버그 수정
```

## 변경 유형별 필수 절차

| 변경 | 필수 |
|---|---|
| 프롬프트 수정 | `registry.yaml` 버전 증가 + 해당 스위트 통과 + 회귀 diff 첨부 |
| 툴 추가 | 스키마 + 어댑터 + `policy.yaml` 등록 + contract 테스트 |
| 가드레일 변경 | `evals/datasets/adversarial/` 케이스 추가 |
| 모델 교체 | 전체 스위트 재실행 + 비용·지연 비교표 |

## 프롬프트 승격 흐름

```
draft  →  candidate  →  active  →  deprecated
        (실험 브랜치)   (평가 통과)  (레지스트리 유지)
```

`scripts/promote_prompt.py`로만 상태를 바꾼다. 수동 편집 금지 —
승격 이력이 감사 로그로 남아야 한다.

## 리뷰 체크리스트

- [ ] 프롬프트 변경이 레지스트리에 반영됐는가
- [ ] 평가 점수가 기준선 대비 하락하지 않았는가 (하락 시 근거 기재)
- [ ] 새 툴에 권한 정책이 있는가
- [ ] PII·비용 관련 변경에 러너북이 갱신됐는가
- [ ] 하드코딩된 모델명·API 키가 없는가
