from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    source_dir: Path
    good_dir: Path
    bad_dir: Path

@dataclass(frozen=True)
class DbOperationsConfig:
    source_dir: Path
    db_dir: Path
    db_name: Path
    training_dir: Path
    training_file: Path