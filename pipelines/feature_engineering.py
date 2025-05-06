from zenml import pipeline

from steps.feature_eng import *


@pipeline
def feature_engineering(author_full_names: list[str], wait_for: str | list[str] | None = None) -> list[str]:
    raw_documents = query_data_warehouse(author_full_names, after=wait_for)

    cleaned_documents = clean_documents(raw_documents)
    last_step_1 = load_to_vector_db(cleaned_documents)

    embedded_documents = chunk_and_embed(cleaned_documents)
    last_step_2 = load_to_vector_db(embedded_documents)

    return [last_step_1.invocation_id, last_step_2.invocation_id]
