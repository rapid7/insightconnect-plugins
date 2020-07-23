from insightconnect_plugin_runtime.exceptions import PluginException
import icon_rapid7_insight_agent.util.agent_typer as agent_typer


def get_all_agents(connection, logger):
    """
    Gets all available agents from the API

    :param connection: ICON connection object
    :param logger: Logger object
    :return: list (agent objects)
    """
    agents = []
    payload = {
        "query": "query($orgId: String!) {organization(id: $orgId) { assets(first: 10000) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } } ",
        "variables": {
            "orgId": connection.org_key
        }
    }

    logger.info(f"Getting agents from: {connection.endpoint}")
    results_object = connection.post_payload(payload)

    has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get("hasNextPage")
    agents.extend(get_agents_from_result_object(results_object))
    logger.info(f"Initial agents received.")

    # See if we have more pages of data, if so get next page and append until we reach the end
    while has_next_page:
        has_next_page, results_object = get_next_page_of_agents(agents, results_object, connection, logger)

    logger.info(f"Done getting all agents.")

    return agents

def get_next_page_of_agents(agents, results_object, connection, logger):
    """
    In the case of multiple pages of returned agents, this will go through each page and append
    those agents to the agents list

    :param agents: list (agent objects)
    :param results_object: dict
    :param connection: ICON connection
    :param logger: logger object
    :return: tuple (boolean, dict (results object))
    """
    logger.info(f"Getting next page of agents.")
    next_cursor = results_object.get("data").get("organization").get("assets").get("pageInfo").get("endCursor")
    payload = {
        "query": "query( $orgId:String! $nextCursor:String! ) { organization(id: $orgId) { assets( first: 1 after: $nextCursor ) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } }",
        "variables": {
            "orgId": connection.org_key,
            "nextCursor": next_cursor
        }
    }
    results_object = connection.post_payload(payload)

    has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get(
        "hasNextPage")

    next_agents = get_agents_from_result_object(results_object)

    agents.extend(next_agents)

    return has_next_page, results_object

def find_agent_in_agents(agents, agent_input, agent_type, logger):
    """
    Given a list of agent objects, find the agent that matches our input

    :param agents: list (agents)
    :param agent_input: String (Input value to look for)
    :param agent_type: String (What type of input to look for, MAC, IP_ADDRESS, or HOSTNAME)
    :param logger: logger object

    :return: dict (agent object)
    """
    logger.info(f"Searching for: {agent_input}")
    logger.info(f"Search type: {agent_type}")
    for agent in agents:
        if agent_type == agent_typer.IP_ADDRESS:
            if agent_input == agent.get("primaryAddress").get("ip"):
                return agent
        elif agent_type == agent_typer.HOSTNAME:
            # In this case, we have an alpha/numeric value. This could be the ID or the Hostname. Need to check both
            if agent_input == agent.get("id"):
                return agent
            for host_name in agent.get("hostNames"):
                if agent_input == host_name.get("name"):
                    return agent
        elif agent_type == agent_typer.MAC_ADDRESS:
            # Mac addresses can come in with : or - as a separator, remove all of it and compare
            stripped_input_mac = agent_input.replace("-", "").replace(":", "")
            stripped_target_mac = agent.get("primaryAddress").get("mac").replace("-", "").replace(":", "")
            if stripped_input_mac == stripped_target_mac:
                return agent
        else:
            raise PluginException(cause="Could not determine agent type.",
                                  assistance=f"Agent {agent_input} was not a Mac, IP, or Hostname.")

    raise PluginException(cause=f"Could not find agent matching {agent_input} of type {agent_type}.",
                          assistance=f"Check the agent input value and try again.")


def get_agents_from_result_object(results_object):
    """
    This will extract an agent object from the objec that's returned from the API

    :param results_object: dict (API result payload)
    :return: dict (agent object)
    """
    agent_list = []

    edges = results_object.get("data").get("organization").get("assets").get("edges")
    for edge in edges:
        agent = edge.get("node").get("host")
        agent_list.append(agent)

    return agent_list
