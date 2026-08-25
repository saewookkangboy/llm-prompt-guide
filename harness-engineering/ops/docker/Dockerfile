FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir -e .

COPY harness/ ./harness/
COPY evals/ ./evals/
COPY scripts/ ./scripts/

# 프롬프트와 정책 파일은 이미지에 포함된다 — 실행 시점에 외부에서 주입하면
# 트레이스에 기록된 버전과 실제 실행이 어긋날 수 있다.

ENV ATLAS_ENV=prod
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "harness.orchestration.graph"]
