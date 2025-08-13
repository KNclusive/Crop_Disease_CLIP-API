# FarmSight — Vigilant monitoring of crop health.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

**FarmSight** is an API that leverages OpenAI's CLIP (Contrastive Language–Image Pretraining) model to identify diseases in crop imagery. Upload a photo, and FarmSight analyses it to recommend potential disease diagnoses—ideal for both researchers and agritech developers.

## Features

- **CLIP-based disease detection**: Uses image–text matching to classify crop conditions.
- **Simple RESTful interface**: Upload images and receive JSON-formatted predictions.
- **Customizable labels**: Easily extend detection categories.
- **Lightweight & efficient**: Built for low-latency inference.

## Notes:
- For reference on training a CLIP model, please refer to this [repository](https://github.com/KNclusive/CLIP)
- The repository Assumes the fine-tuned CLIP model is available in huggingface (Great choice now with XET replacing LFS)
- The `test.py` is an inference enabled python file to test the API. To run the file, replace the base_url with the public IP of your container. Provide image paths from the Inference_set or any other image.

## Quick Start

### 1. Clone the repository:

```bash
git clone https://github.com/KNclusive/AgriCLIP.git
run "python test.py"
```

## Deployment to AWS:
- Assuming here you have alredy contenerized your api application. (This repository uses docker to contenerize)
- Push docker image to docker hub. (docker push <yourreponame>/<yourapplicationname>:<yourtagname>)
- Create an account on aws if not already present. (This demo functions within the free tier limits of AWS ECS for more information visit [here](https://aws.amazon.com/free/webapps/?p=ft&z=subnav&loc=3)
- Open your AWS Console and proceede to ECS (Elastic container service).
- Create an task definition where in you would:
   - Give a name to your container (task).
   - Define compute requirements. (This project functions 1cpu 3gb configurations which is the default)
   - Provide your container url (url of the container pushed on docker hub i.e. <yourreponame>/<yourapplicationname>:<yourtagname>)
   - Provide host and port mapping accordingly. (While creating the application the container host and post mapping is already done on 0.0.0.0 [means listen on all hosts] and 8000 port)
   - Proceede to create the task definition but clicking on create.
- Create a cluster
- Inside the cluster you have two options:
   - Task for repetitive/ periodic/ batched requests (Static).
   - Service (for dynamic web apps; usually better for API's which is our case.)
- Create an service by selecting the task definition created before.
- This should spin up your container, inside the created service navigate towards network where you can find public IP on which your container will be available at the port mentioned by you.

## Future Scope
Creating an chatbot around this API, along with RAG [here](https://github.com/KNclusive/Retrieval-Augmented-Generation)
