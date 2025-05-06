from pipelines.feature_engineering import feature_engineering
import yaml


if __name__ == "__main__":
    
    config = yaml.safe_load(open("/Users/shambhavi/Documents/Projects/llm-mimic/configs/data_configs/feature_eng.yaml"))

    author_full_names = config['parameters']['author_full_names']  
    # set wait_for if you want to process only new/updated docs
    wait_for = None

    # Run the pipeline
    result = feature_engineering(author_full_names, wait_for=wait_for)
    

