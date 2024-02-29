from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path # in python, we have data type 'path' 
    source_url: str # but we don't have 'url' type datatype, hence have to use str for url
    local_data_file: Path
    unzip_dir: Path