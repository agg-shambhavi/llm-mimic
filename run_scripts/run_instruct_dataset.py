from pipelines.generate_datasets import generate_datasets
import yaml

if __name__ == "__main__":
    config = yaml.safe_load(open("/Users/shambhavi/Documents/Projects/llm-mimic/configs/data_configs/generate_instruct_datasets.yaml"))
    dataset_type = config['parameters']['dataset_type']
    push_to_huggingface = config['parameters']['push_to_huggingface']
    dataset_id = config['parameters']['dataset_id']
    test_split_size = config['parameters']['test_split_size']
    mock = config['parameters']['mock']
    generate_datasets(dataset_type = dataset_type,
    test_split_size = test_split_size,
    push_to_huggingface = push_to_huggingface,
    dataset_id = dataset_id,
    mock = mock)
    
    