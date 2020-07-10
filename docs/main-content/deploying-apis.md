# Deploying APIs

New API services should be built into Docker containers and deployed via GitLab's continuous integration tools.

## Building and deploying containers

### docker-compose + Ansible approach

The [Palaeosaurus API project](https://kwvmxgit.ad.nerc.ac.uk/apis/api-services/palaeosaurus-api) uses docker-compose and Ansible to deploy the API services.
This approach allows developers to run and test the software locally and requires minimal configuration on the host server.
An overview of the files is given here; see the repository for details.

#### Configuration files

The following files are used for deployment:

```
.
├── ...
├── deploy
│   ├── deploy.yml
│   ├── host_files
│   │   └── docker-compose.yml
│   └── hosts.yml
├── docker-compose-local.yml
├── Dockerfile
├── .gitlab-ci.yml
├── ...
```

**Local development**

The `Dockerfile` is used to build the container, and developers can build and run the service locally with:

```bash
docker-compose -f docker-compose-local.yml up --build
```

Port mappings, environment variables and volume mounts are be described in `docker-compose-local.yml`.  It is possible to describe a multi-container service.

**Deployment**

The `deploy` folder contains files used for deployment.  `deploy.yml` is an Ansible playbook that will:

+ Create a deployment directory on the target server
+ Copy over files from the `host_files` directory
+ Create a `.env` file on the target server containing environment variables required by Docker compose
+ Pull container(s) and start the service

These are generic commands and the same `deploy.yml` can be used for nearly all projects.  The `docker-compose.yml` file is similar to the one used locally, but with variables such as Docker registry, container tag and port number are read from the `.env` file.
`hosts.yml` contains lists of servers for each environment, deployment directory settings and a mapping between GitLab CI environment variables and the `.env` file.

**CI pipelines**

The CI pipeline and deployment environments are defined in `.gitlab-ci.yml`.  The environments are as follows:

| Environment | Branch | Deployed by | Container Tag |
| ------ | ------ | ------ | ------ |
| Review | feature-branch | manually | review | 
| Develop | main | merge into main | main |
| Staging | staging | merge into staging | staging |
| Production | staging | making a new tag |  v1.2.3 |

The `build-*` stages build the container, run tests and linting and push to the container registry.
The existing `main` container is pulled from the GitLab registry so that the Docker build can use `--cache-from` to run faster.
The `build-for-review` stage pushes feature branches with the `review` tag to avoid filling the registry with unused containers for each branch.
`build-for-deploy` tags containers with their deployment environment or version number.

The `deploy-*` stages use our [Ansible Deployer](https://kwvmxgit.ad.nerc.ac.uk/devops/ansible-deployer) container to run the `deploy.yml` playbook against target servers.
Connections are made as the `deploy` user, which requires SSH keys to be configured on the target server and in the project's GitLab CI variables.
Each stage calls `.deploy-common` and settings are configured via environment variables.  Default values are defined at the top of `.gitlab-ci.yml` and can be overridden in the individual deployment tasks e.g. `deploy-review`.
The `environment` sections define URLs where the running services can be accessed.
These appear as links in the GitLab web UI's Operations/Environments pages.
As they are used by human beings, the links should point to the API's Swagger UI if available.

This deployment pipeline is relatively generic.  The main changes between projects will be to the `.build-common` stage and the environment variables defined at the top of the file and in the `deploy-*` stages.

## API servers

There are currently 3 servers in the Edinburgh DevOps cluster for API projects.

+ hwlapi01.bgslcdevops.test
+ hwlapi02.bgslcdevops.test
+ hwlapi03.bgslcdevops.test

The servers are configured via Ansible playbook here: https://kwvmxgit.ad.nerc.ac.uk/devops/api-servers.
They have a custom `deploy` user SSH public key for CI jobs.  See the [Palaeosaurus project CI variables](https://kwvmxgit.ad.nerc.ac.uk/apis/api-services/palaeosaurus-api/-/settings/ci_cd) for the private key.


## Proxy server

BGS API Proxy servers provides a single point of access to multiple API services.  There is one for each deployment environment.

+ [Review](http://hwlapi01.bgslcdevops.test:9080)
+ [Develop](http://hwlapi01.bgslcdevops.test:8080)
+ [Staging](http://hwlapi02.bgslcdevops.test:8080)
+ [Production](http://hwlapi03.bgslcdevops.test:8080)

Instructions for adding a new API to the proxy service are here:
https://kwvmxgit.ad.nerc.ac.uk/apis/proxy

## Internal (intranet) 
	
* {LINK TO PROXY}
* {JAVA SERVERS}
* {VMS/DOCKER}
	
## External (*.bgs.ac.uk)

* {LICENCES AND DATA OWNERSIHP}
* {LINK TO PROXY}
* {JAVA SERVERS}
* {VMS/DOCKER}

## Security
	
SSL provided by F5 ...
		
## External Caching
		
Varnish or similar or maybe F5?

## Logging/auditing

Central logging system?

## Performance/monitoring

?
