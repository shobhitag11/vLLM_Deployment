from multiprocessing import Process
import subprocess
import os

# To download the models locally.
# Llama2: 
# git lfs install
# git clone https://huggingface.co/meta-llama/Llama-2-13b-chat
# Mistral:
# git lfs install
# git clone https://huggingface.co/mistralai/Mistral-7B-v0.1

LLAMA_MODEL_PATH = "/llama_model_path"
MISTRAL_MODEL_PATH = "/mistral_model_path"

# Assuming 4 GPUs:
# first two GPUs consumed for llama2 deployment.
# second two GPUs consumed for mistral deployment
# Setting this using CUDA_VISIBLE_DEVICES 

def host_llama2():
    os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
    subprocess.run([
        "python", "-m", "vllm.entrypoints.api_server",
        "--model", LLAMA_MODEL_PATH,
        "--host", "0.0.0.0",
        "--port", "8000",
        "--tensor-parallel-size", "2" #this is required if we want to shard the model accross multiple GPUs.
    ])

def host_mistral():
    os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"
    subprocess.run([
        "python", "-m", "vllm.entrypoints.api_server",
        "--model", MISTRAL_MODEL_PATH,
        "--host", "0.0.0.0",
        "--port", "8001",
        "--tensor-parallel-size", "2" #this is required if we want to shard the model accross multiple GPUs.
    ])

if __name__ == "__main__":
    # Create multiprocess Process
    process1 = Process(target=host_llama2)
    process2 = Process(target=host_mistral)

    # Start both the process
    process1.start()
    process2.start()

    # Wait for both the processes to finish
    process1.join()
    process2.join()
