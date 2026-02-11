import os
from pathlib import Path
import logging

# --------------------------------------------------------
# Logging Configuration
# --------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(levelname)s - %(message)s'
)

# --------------------------------------------------------
# Files & Folders to Create (ROOT LEVEL)
# --------------------------------------------------------
list_of_files = [

    # Root files
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    ".gitignore",
    ".env.example",

    # Configs
    "configs/base.yaml",
    "configs/experiment_01.yaml",
    "configs/experiment_02.yaml",
    "configs/tracking.yaml",

    # src
    "src/__init__.py",

    # data
    "src/data/__init__.py",
    "src/data/loader.py",
    "src/data/preprocessing.py",
    "src/data/dataset_registry.py",

    # models
    "src/models/__init__.py",
    "src/models/model_factory.py",
    "src/models/baseline.py",
    "src/models/deep_model.py",

    # training
    "src/training/__init__.py",
    "src/training/trainer.py",
    "src/training/evaluator.py",
    "src/training/metrics.py",

    # tracking
    "src/tracking/__init__.py",
    "src/tracking/base_tracker.py",
    "src/tracking/mlflow_tracker.py",
    "src/tracking/wandb_tracker.py",
    "src/tracking/clearml_tracker.py",
    "src/tracking/dagshub_tracker.py",

    # utils
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/reproducibility.py",
    "src/utils/helpers.py",

    # experiments
    "experiments/experiment_01/run.py",
    "experiments/experiment_01/notes.md",
    "experiments/experiment_02/run.py",
    "experiments/experiment_02/notes.md",
    "experiments/comparison/compare_results.py",

    # artifacts (gitkeep ensures folder tracked)
    "artifacts/models/.gitkeep",
    "artifacts/plots/.gitkeep",
    "artifacts/reports/.gitkeep",

    # logs
    "logs/.gitkeep",

    # tests
    "tests/test_models.py",
    "tests/test_training.py",
    "tests/test_tracking.py",

    # notebooks
    "notebooks/exploratory_analysis.ipynb",
    "notebooks/results_visualization.ipynb",
]

# --------------------------------------------------------
# Create Structure
# --------------------------------------------------------
for filepath in list_of_files:

    filepath = Path(filepath)
    filedir = filepath.parent

    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

logging.info("Project structure created successfully.")
