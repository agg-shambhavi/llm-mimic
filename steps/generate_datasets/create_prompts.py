from typing_extensions import Annotated
from zenml import get_step_context, step

from services.generate_datasets_service.generation import get_dataset_generator
from data_models.dataset import DatasetType
from data_models.prompt import GenerateDatasetSamplesPrompt
from data_models.documents import DataCategory


@step
def create_prompts(
    documents: Annotated[list, "queried_cleaned_documents"],
    dataset_type: Annotated[DatasetType, "dataset_type"],
) -> Annotated[dict[DataCategory, list[GenerateDatasetSamplesPrompt]], "prompts"]:
    dataset_generator = get_dataset_generator(dataset_type)
    grouped_prompts = dataset_generator.get_prompts(documents)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="prompts", metadata=_get_metadata(grouped_prompts))

    return grouped_prompts


def _get_metadata(grouped_prompts: dict[DataCategory, list[GenerateDatasetSamplesPrompt]]) -> dict:
    prompt_categories = list(grouped_prompts.keys())
    prompt_num_samples = {category: len(prompts) for category, prompts in grouped_prompts.items()}

    return {"data_categories": prompt_categories, "data_categories_num_prompts": prompt_num_samples}
