from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path # in python, we have data type 'path' 
    source_url: str # but we don't have 'url' type datatype, hence have to use str for url
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: dict # reading from schema.yaml, where we already store that what were the cols(features) present at the time of training


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path