# Crop_Disease_CLIP-API
This repository contains code and procedure to build API inference endpoints using FastAPI for an custom CLIP model trained on crop-disease dataset and pushed to huggingface.

For reference on training a CLIP model, please refer to this repository https://github.com/KNclusive/CLIP

For Deploying the API on hosted server Amazon AWS was choosen. Below are the steps to deploy API on AWS:
1. Assuming here you have alredy contenerized your api application. (This repository uses docker to contenerize)
2. Push docker image to docker hub. (docker push <yourreponame>/<yourapplicationname>:<yourtagname>)
3. Create an account on aws if not already present. (This demo functions within the free tier limits of AWS ECS for more information visit here: https://aws.amazon.com/free/webapps/?p=ft&z=subnav&loc=3)
4. Open your AWS Console and proceede to ECS (Elastic container service).
5. Create an task definition where in you would:
   a. Give a name to your container (task)
   b. Define compute requirements. (This project functions 1cpu 3gb configurations which is the default)
   c. provide your container url (url of the container pushed on docker hub i.e. <yourreponame>/<yourapplicationname>:<yourtagname>)
   d. provide host and port mapping accordingly. (While creating the application the container host and post mapping is already done on 0.0.0.0 [means listen on all hosts] and 8000 port)
   e. proceede to create the task definition but clicking on create.
6. Create a cluster
7. Inside the cluster you have two options:
   a. Task for repetitive/ periodic/ batched requests (Static).
   b. service (for dynamic web apps; usually better for API's which is our case.)
8. Create an service by selecting the task definition created before.
9. This should spin up your container, inside the created service navigate towards network where you can find public IP on which your container will be available at the port mentioned by you.


The Test.py is an inference enabled python file to test the API. To run the file, replace the base_url with the public IP of your container. Provide image paths from the Inference_set or any other image.
