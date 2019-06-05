import string
from datetime import datetime
from tempfile import NamedTemporaryFile


def extract_isodate(stamp):
    if type(stamp) is not str:
        return datetime.utcfromtimestamp(stamp).isoformat()
    else:
        return stamp


def image_to_json(image):
    return {
        'id': image.attrs.get('Id', ''),
        'parent_id': image.attrs.get('ParentId', ''),
        'created_at': extract_isodate(image.attrs.get('Created', '')),
        'labels': image.attrs.get('Labels', {}),
        'size': image.attrs.get('Size', -1),
        'shared_size': image.attrs.get('SharedSize', -1),
        'virtual_size': image.attrs.get('VirtualSize', -1),
        'repo_tags': image.attrs.get('RepoTags', []),
        'repo_digests': image.attrs.get('RepoDigests', []),
        'containers': image.attrs.get('Containers', 0)
    }


def container_to_json(container):
    return {
        'id': container.id,
        'name': container.name,
        'image': image_to_json(container.image),
        'created_at': extract_isodate(container.attrs.get('Created', '')),
        'status': container.status,
        'labels': container.labels,
        'size_rw': container.attrs.get('SizeRw', -1),
        'size_rootfs': container.attrs.get('SizeRootFs', -1)
    }


def network_to_json(network):
    return {
        'id': network.id,
        'short_id': network.short_id,
        'name': network.name,
        'containers': list(map(container_to_json, network.containers))
    }


def key_to_file(key):
    """
    The user provides the key_file as a string with inconsistent whitespace
    So this function will extract the core components - header, key, footer
    and stitch them back together to conform to the PEM formatting rules
    that TLSConfig and Docker require to read them correctly
    """
    delimiter = '-' * 5
    _, header, key, footer, _ = key.split(delimiter)
    key_file = (
        delimiter + header + delimiter + '\n'
        + key + '\n'
        + delimiter + footer + delimiter
    )
    with NamedTemporaryFile('w', delete=False) as f:
        f.write(key_file)
        return f.name
