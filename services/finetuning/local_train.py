# local_train.py
import subprocess
from pathlib import Path
from loguru import logger
from configs import settings
import os
from huggingface_hub import HfApi

def run_finetuning_locally(
    finetuning_type: str,
    num_train_epochs: int,
    per_device_train_batch_size: int,
    learning_rate: float,
    dataset_huggingface_workspace: str = "agg-shambhavi",
    is_dummy: bool = False,
) -> None:
    # Set environment variables
    env = {
        **dict(os.environ),
        "HUGGING_FACE_HUB_TOKEN": settings.HUGGINGFACE_ACCESS_TOKEN,
        "COMET_API_KEY": settings.COMET_API_KEY,
        "COMET_PROJECT_NAME": settings.COMET_PROJECT,
    }

    api = HfApi()
    user_info = api.whoami(token=settings.HUGGINGFACE_ACCESS_TOKEN)
    huggingface_user = user_info["name"]
    logger.info(f"Current Hugging Face user: {huggingface_user}")

    # Build training command
    base_cmd = [
        "python", "finetune.py",
        f"--finetuning_type={finetuning_type}",
        f"--num_train_epochs={num_train_epochs}",
        f"--per_device_train_batch_size={per_device_train_batch_size}",
        f"--learning_rate={learning_rate}",
        f"--dataset_huggingface_workspace={dataset_huggingface_workspace}",
        f"--model_output_huggingface_workspace={huggingface_user}",
    ]
    
    if is_dummy:
        base_cmd.append("--is_dummy")

    # Run training
    try:
        subprocess.run(base_cmd, check=True, env=env)
        logger.success("Training completed successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Training failed with error: {e}")
        raise
