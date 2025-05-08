from pipelines.training import training
import yaml

if __name__ == "__main__":
    config = yaml.safe_load(open("/Users/shambhavi/Documents/Projects/llm-mimic/configs/data_configs/sft_training.yaml"))
    finetuning_type = config['parameters']['finetuning_type']
    num_train_epochs = config['parameters']['num_train_epochs']
    per_device_train_batch_size = config['parameters']['per_device_train_batch_size']
    learning_rate = config['parameters']['learning_rate']
    dataset_huggingface_workspace = config['parameters']['dataset_huggingface_workspace']
    is_dummy = config['parameters']['is_dummy']
    training(
    finetuning_type = finetuning_type,
    num_train_epochs= num_train_epochs,
    per_device_train_batch_size = per_device_train_batch_size,
    learning_rate= learning_rate,
    dataset_huggingface_workspace = dataset_huggingface_workspace,
    is_dummy = is_dummy,
)
