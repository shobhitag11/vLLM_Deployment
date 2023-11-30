# VLLM Deployment

## Overview

This readme provides instructions for deploying the LLM Models using vLLM.

## Prerequisites

Before deploying VLLM, ensure you have the following prerequisites:

1. **Hardware Requirements:**
   - Sufficient CPU and GPU resources
   - Recommended: NVIDIA GPU with CUDA support for optimized performance

2. **Software Requirements:**
   - Python 3.x
   - CUDA Toolkit (if using GPU)
   - Dependencies listed in `requirements.txt`

3. **Environment Setup:**
   - Create a virtual environment:
     ```bash
     python3 -m venv vllm-env
     source vllm-env/bin/activate  # On Windows, use `vllm-env\Scripts\activate`
     ```

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Deployment Steps

**Deploy the LLM Models:**
   ```bash
   python vllm_deployment.py
   ```
 This command launches the VLLM service, and it will be accessible at `http://localhost:8000` for llama2 and `http://localhost:8001` for mistral.

## API Usage
The VLLM service exposes a RESTful API for text generation. Send a POST request to `http://localhost:8000/generate` with a JSON payload:

```json
{
  "prompt": "Your text prompt here."
}
```
Example using cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Tell me a story."}' http://localhost:8000/generate
```

## Additional Notes

- **Security:**
  - Ensure the deployment environment is secure and follows best practices.
  - Consider enabling authentication and authorization mechanisms based on your deployment requirements.

- **Scaling:**
  - For high-demand environments, consider deploying VLLM behind a load balancer and scaling horizontally.

- **Monitoring:**
  - Implement monitoring for resource usage, error rates, and other relevant metrics.

## Troubleshooting

If you encounter issues during deployment, refer to the troubleshooting section in the documentation or seek assistance from the community.

---

**Congratulations on successfully deploying VLLM! 🎉**

*Note: Replace placeholders such as `[LLAMA_MODEL_PATH]` and `[MISTRAL_MODEL_PATH]` with the actual URLs or values specific to your deployment.*
