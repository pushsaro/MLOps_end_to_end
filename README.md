## End to end MLOps project

# Software and tools requirements

1. [Github Account](https://github.com)
   
2. [Amazon Web Services Account](https://aws.amazon.com/free/?trk=16847e0c-46fb-467d-91ee-6e259e339665&sc_channel=ps&s_kwcid=AL!4422!10!72086958325164!72087482393523&ef_id=de197eca60e313e469e91ba207a0345a:G:s&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
   
3. [VS Code IDE](https://code.visualstudio.com/)
   
4. [Docker Hub](https://hub.docker.com)

Create a new environment for project

...
conda create -p venv python==3.7 -y
...

# Docker setup in EC2 commands to be executed

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
