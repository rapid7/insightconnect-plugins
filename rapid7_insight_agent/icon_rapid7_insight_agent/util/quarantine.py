from insightconnect_plugin_runtime.exceptions import PluginException

def quarantine(advertisement_period, agent_id, quarantine_state, connection, logger):
    if quarantine_state:
        quarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String! $advPeriod:Long! ) { quarantineAssets( orgId:$orgID assetIds: [$agentID] input: {advertisementPeriod: $advPeriod} ) { results { assetId failed } } }",
            "variables": {
                "orgID": connection.org_key,
                "agentID": agent_id,
                "advPeriod": advertisement_period
            }
        }
    else:
        quarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }",
            "variables": {
                "orgID": connection.org_key,
                "agentID": agent_id
            }
        }

    action_verb = "quarantine" if quarantine_state else "unquarantine"
    logger.info(f"Attempting to {action_verb} asset {agent_id} at {connection.endpoint}")

    results_object = connection.post_payload(quarantine_payload)

    if quarantine_state:
        failed = results_object.get("data").get("quarantineAssets").get("results")[0].get("failed")
    else:
        failed = results_object.get("data").get("unquarantineAssets").get("results")[0].get("failed")

    return (not failed)
