def attachments_to_dict(attachments):
    results = []
    for attachment in attachments:
        attachment = dict(zip(('id', 'FileNameSize'), (attachment[0], attachment[1])))
        results.append(attachment)

    return results
