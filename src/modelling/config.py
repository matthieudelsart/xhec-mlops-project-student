from pathlib import Path

CATEGORICAL_COLS = ['Sex']
NUMERICAL_COLS = [
    'Length',
    'Diameter',
    'Height',
    'Whole weight',
    'Shucked weight',
    'Viscera weight',
    'Shell weight',
]

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
LOCAL_OBJECTS_DIRPATH = str(PROJECT_ROOT / "src/web_service/local_objects")