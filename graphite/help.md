# Description

[Graphite](https://graphiteapp.org/) Graphite is an enterprise-ready monitoring tool that runs equally well on cheap hardware or Cloud infrastructure. Teams use Graphite to track the performance of their websites, applications, business services, and networked servers. It marked the start of a new generation of monitoring tools, making it easier than ever to store, retrieve, share, and visualize time-series data. 

The Graphite plugin allows you to store, retrieve, and update your metrics. The plugin will also return a byte array of graphed data. 

This plugin utilizes the [Graphite API](https://graphite-api.readthedocs.io/en/latest/) to help you fetch metrics or render graphs from the time-series database.

# Key Features

* Store and retrieve data
* Graph data

# Requirements

* A Graphite server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|graphite_url|string|None|True|Graphite API Server URL|None|
|graphite_port|integer|8888|False|Graphite API Port Number|None|

## Technical Details

### Actions

#### Expand Metrics

This action is used to expands metrics with matching paths.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Search query|None|
|leaves_only|boolean|False|False|Display only leaves|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|metrics|[]string|False|List of matching metrics' names|

Example output:

```

{
  "metrics": [
    "carbon",
    "test"
  ]
}

```

#### Render Metrics

This action is used to render metrics data as a graph.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|templates|object|None|False|Values for template variables used in target|None|
|graph_params|graph_parameters|None|False|Parameters to control the rendered graph output|None|
|from|string|None|False|Beginning of required range (can be relative or absolute)|None|
|target|string|None|True|A path identifying one or several metrics, optionally with functions acting on those metrics|None|
|format|string|png|False|Rendered graph file format|['png', 'raw', 'csv', 'svg', 'pdf']|
|until|string|None|False|End of required range (can be relative or absolute)|None|

More information about relative and absolute from/until formats can be found [here](https://graphite-api.readthedocs.io/en/latest/api.html#from-until).
More information about the various graph parameters can be found [here](https://graphite-api.readthedocs.io/en/latest/api.html#graph-parameters).

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|graph|bytes|False|Rendered Graph in base64 format|

Example output:

```

{
  "graph": "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jFbq6q2qqq7rmqbpuu7xeMx63by6unl1FZoUgFWlXnsHAoFwOJxMJsPhcCAQqNAsAIqo1JPz4eHhtWvXDgwM3HLLLb/85S99Pl8lZgFQRKXiDaDqeFsLIBbxBsQi3oBYxBsQi3gDYhFvQKyrjHd/f/8NN9zQ0tLS19enKEpvb6/Dore31+y0Dv3whz8sWCly5oKVSnjuuefa2tq8Xu+uXbsURdm3b591R9afirEObdiwoWDF3mzWizSXVyQS+ehHP3rttdf+6Ec/yufzzz77rHVH3/nOd8xO69Cdd95ZsGIaHx9/4IEHWlpampqa7rzzzpGREftcFdrRsWPHbrzxxqampi1btmSz2SNHjlh3tGbNGrPTOmS8q8pemWRiYqKjo+MKm+eMfOlisZjH4zl58uTQ0ND111//5ptvWkfXrFmj67r5ZU9Pzw9+8ANrg71S5MzF5yqX0dFRVVVfe+21f/3rX4sWLTp+/Lh1dP369WfOnDG/fOKJJ9avX29tsFcmsTZctrks3n///ebm5iNHjgwPD3/yk5/8wx/+YB3dvn3766+/bn554MCBr3zlK9YGe8X04osvPvzww++++66u62vXrt2yZUvxucolm822trY+//zziUSivb3917/+tXV0586dr7zyivllJBL5/Oc/b22wVyZ5+OGHPR6P0XPZ5rniaq7ef/7znwOBwNKlS5csWfLlL385EomYQ2+88cY111xz3XXX9fb2mlfmvXv3ulyuJUuWPProowUrZrP9zEXmKqPjx48vX778lltuWbBgwde//vWXX37ZHDpz5syFCxcWLly4b98+82L7zDPPuFyutra2np6eghVrs5398LI7efJka2vr5z73uebm5nXr1ln/3OLx+FtvvXXzzTc/++yz5pX50KFDLpfrhhtu6OrqmpiYsFfM5ttvv3379u1NTU1Op7Ours74x3equcpoaGjI5XKtXr1aVdWNGzdaZ0kmk3/6059Wrlx55MgR82J77Ngxl8uladr3vve9TCZjr1ibT58+/fjjj+/Zs8c8p/3wOekq/knYs2fP1q1bjce7du164IEHzKHVq1dHo1H7IZcuXTpx4sTChQsPHz48VaXgmYvMVUb9/f2dnZ3G40cffXTz5s3mUGdn51/+8hf7IZlM5uTJkzfddNMzzzwzVcVkv2IXaS6LgwcPfulLXzIe/+Y3v7n77rvNoa1btz7//PP2Q7LZ7OnTp1esWPHYY49NVTEcOHDA+J/nU5/6VCqVKjJXGR09evTWW281Hr/00ku33367OfTggw/29/fbD8nlckNDQ5/97Ge7u7unquTz+UuXLrW3t584cWLSRbtg89xyNVdvVVXPnTtnPD537pz5A2F/+9vfUqmU3++3H1JXV7d8+fI1a9acOHFiqkrBM081V3lNmkVVVePx22+//dZbb9166632Q2pra5cuXfrNb37TXL+9UkRJzVdhqj+34eHhP/7xj3fccYf9kJqamhtvvHHjxo3mkuwVg/G8PR6Pf/zjH9+5c2dV/o7MWS5cuPDb3/72a1/7mv0Qp9O5ZMmSzZs3m+u3VxRFefXVV1977bUVK1YEAgHrJb1g8xxzFf8kWF8Pt7S0nD592qh/8YtffPHFFwseks1mT548uWTJErPBXil45qnmKq/z58+rqnr8+PF//vOfixYtOnbsmFH/xje+8fTTTxc8JJfLvfnmm0uXLjUb7BWT/epdpLks3n//fa/XG4lEjNfD5h/yfffd19fXV/CQiYmJoaGhT3/602aDvZLP51966aUnn3wymUzG4/HOzs7vfve7U81VXtls9iMf+cjvf//7c+fOtbe3/+pXvzLqXV1dP/nJT6Y66p133gkEAtYGe8Vkf8ldpHlOuJp45/P5J598UtM0n88XDoeNyl//+tePfexjuVzO+NK8f2a8vKypqWltbf3pT386VcW82WY/s71SCQcOHGhtbfV4PA899JBRGRwcXLBgwX/+8x/jSzOiTzzxhKIoTqdzwYIFO3bsmJiYKFixNpvWr19vb67Qjg4fPrx48eKmpqbvf//7xt9LLBZrbm5+7733zC0b12HjybbD4bj++uuNl5oFK0ZzKpXavHlzY2Pjddddd/fdd4+OjhacqxKOHj36iU98orGx8d57781kMvl8/t133/V6vefOnTMazHyar8x9Pt+9996bTqcLVqa6/WZvrtCOKo2fGAPE4m0tgFjEGxCLeANiEW9ALOINiEW8AbGINyAW8QbEIt6AWNP6EKKtW7cWb1i1atWqVaumMwWAqzbdzxhLpfZMNfShDx2e5skLcjhKfiPtVRwCCDDTT84dDkeFmsui+Iwzvx5gOnjtDYg1o/E2rn7Gb6hTFOXtt99euXKl2+32+/3GT8zv2rXL4/GYv8XO2my1c+fOa6+99qabbnr99dfNMzscjkWLFhm/R8l6HqPhZz/7mc/n8/l8v/vd76ynKj6j9bSTRu1TALPNjMbbeAFs/CSqoijr1q1bt27d+fPne3t7169fryhKb2/vQw89lEqlzB7zgZWqqmfPnt20adOmTZvMM2cymb179953332TzmM0uFyud95556mnntq+fbv1VMVntJ520qh9CmC2qeaT8zfeeKOzs9Plcn3hC184ffq0oiiPP/74008/7fP5HnzwwSIHdnZ2XnPNNd/61reMox577LG2trZ58+bddtttZ86cKXieTZs2uVyu22677d///rf1VEVmtJ/2Cg8EZovp/C6I+++//9vfzk/13z33HDp06NCkQ+bNmzc0NGQ8/sxnPrN///6LFy9O6nn11VfdbvekZpOiKHv37k2lUo888sjy5cvz+XxDQ8MLL7wwPDz83HPPWXdknsdaLLjlgjPaT2tfj3kgMAtN9xtjpbrnnntuvvlm4zltf3//li1b7r///mQyaeTHeB2rquqPf/zjSc3Wb24lEokFCxa0tLT09/crirJ9+/a1a9e63W7zdw9POo+debYiM9pPO2k9xacAqm5a3xDeunVr8e9733GHwttagGqZ7tW7yHtXamr+oSiLp3l+AFdtWvG+3JV58eLFxBuoGt6tCYjFu9YAsYg3IBbxBsQi3oBYxBsQ6/8AzUrSCfYWnXYAAAAASUVORK5CYII="
}

```

#### Retrieve Metrics

This action is used to retrieve raw metrics data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|templates|object|None|False|Values for template variables used in target|None|
|from|string|None|False|Beginning of required range (can be relative or absolute)|None|
|target|string|None|True|A path identifying one or several metrics, optionally with functions acting on those metrics|None|
|until|string|None|False|End of required range (can be relative or absolute)|None|

More information about relative and absolute from/until formats can be found [here](https://graphite-api.readthedocs.io/en/latest/api.html#from-until).

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|metrics|[]metric_raw|False|Target metrics in JSON format|

Example output:

```

{
  "metrics": [
    {
      "target": "test.bash.stats",
      "datapoints": [
        [
          null,
          1498809300
        ]
      ]
    }
  ]
}

```

#### Index Metrics

This action is used to walks the metrics tree and returns every metric found.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|metrics|[]string|False|List of indexed metrics' names|

Example output:

```

{
  "metrics": [
    "carbon.agents.ubuntu-xenial-a.activeConnections",
    "carbon.agents.ubuntu-xenial-a.avgUpdateTime",
    "carbon.agents.ubuntu-xenial-a.blacklistMatches",
    "carbon.agents.ubuntu-xenial-a.cache.bulk_queries",
    "carbon.agents.ubuntu-xenial-a.cache.overflow",
    "carbon.agents.ubuntu-xenial-a.cache.queries",
    "carbon.agents.ubuntu-xenial-a.cache.queues",
    "carbon.agents.ubuntu-xenial-a.cache.size",
    "carbon.agents.ubuntu-xenial-a.committedPoints",
    "carbon.agents.ubuntu-xenial-a.cpuUsage",
    "carbon.agents.ubuntu-xenial-a.creates",
    "carbon.agents.ubuntu-xenial-a.droppedCreates",
    "carbon.agents.ubuntu-xenial-a.errors",
    "carbon.agents.ubuntu-xenial-a.memUsage",
    "carbon.agents.ubuntu-xenial-a.metricsReceived",
    "carbon.agents.ubuntu-xenial-a.pointsPerUpdate",
    "carbon.agents.ubuntu-xenial-a.updateOperations",
    "carbon.agents.ubuntu-xenial-a.whitelistRejects",
    "test.bash.stats"
  ]
}

```

#### Find Metrics

This action is used to find metrics under a given path.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|wildcards|boolean|False|False|Use wildcard result|None|
|query|string|None|True|Search Query|None|
|from|date|None|False|Beginning of required range|None|
|until|date|None|False|End of required range|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|metrics|[]metric|False|List of metrics|

Example output:

```

{
  "metrics": [
    {
      "allow_children": true,
      "is_leaf": false,
      "name": "carbon",
      "path": "carbon",
      "is_expandable": true
    },
    {
      "allow_children": true,
      "is_leaf": false,
      "name": "test",
      "path": "test",
      "is_expandable": true
    }
  ]
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Graphite](https://graphiteapp.org/)
* [Graphite API](https://graphite-api.readthedocs.io)

