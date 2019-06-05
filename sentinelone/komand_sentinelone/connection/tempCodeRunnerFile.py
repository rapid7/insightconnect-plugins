body = {
        "data": [{
            "hash": "some_value"
        }]
}

print("Adding Agent ID: " + "agent_id")
body.get("data")[0]["agentId"] = "agent_id"

print(body)