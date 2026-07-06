from dataclasses import dataclass


@dataclass
class ExecutionResult:
    status: str
    runtime_ms: int | None
    passed_cases: int
    total_cases: int
    error: str | None

@dataclass
class SubmissionResult:
    verdict: str
    runtime_ms: int
    runtime_percentile: float
    memory_mb: float
    memory_percentile: float
    submission_id: str