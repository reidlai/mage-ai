from enum import Enum


class ChartDataSourceType(str, Enum):
    BLOCK = 'block'
    BLOCK_RUNS = 'block_runs'
    CHART_CODE = 'chart_code'
    PIPELINES = 'pipelines'
    PIPELINE_RUNS = 'pipeline_runs'
    PIPELINE_SCHEDULES = 'pipeline_schedules'
