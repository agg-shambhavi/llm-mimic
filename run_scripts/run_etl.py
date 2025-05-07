# run_etl.py
from pipelines.data_etl import digital_data_etl
import yaml


if __name__ == "__main__":
    
    config = yaml.safe_load(open("/Users/shambhavi/Documents/Projects/llm-mimic/configs/data_configs/digital_data.yaml"))
    user_full_name = config['parameters']['user_full_name']
    links = config['parameters']['links']
    digital_data_etl(user_full_name=user_full_name, links=links)
