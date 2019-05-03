# mu-project

## Pre-requisite

In order to process, you should have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [docker](https://docs.docker.com/install/), and [docker-compose](https://docs.docker.com/compose/install/) installed (don't forget to run the [post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/) from the Docker doc).

For ElasticSearch to run well, you should also exec the following command:

```bash
sysctl -w vm.max_map_count=262144
```

## Git clone

```bash
git clone git@github.com:rvuong/mu-project.git
cd mu-project

```

## Run

Start the stack

```bash
docker-compose up --build
```

Then you should be able to request both the Elasticsearch and Kibana urls:

| Page                         | Url                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------ |
| Frontend home                | [http://localhost:80](http://localhost:80)                                     |    
| Elasticsearch home           | [http://localhost:9200](http://localhost:9200)                                 |
| Elasticsearch Cat. health    | [http://localhost:9200/_cat/health](http://localhost:9200/_cat/health)         |
| Elasticsearch Cluster health | [http://localhost:9200/_cluster/health](http://localhost:9200/_cluster/health) |
| Kibana home                  | [http://localhost:5601](http://localhost:5601)                                 |
