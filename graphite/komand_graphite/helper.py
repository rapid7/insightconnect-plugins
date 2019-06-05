import dateutil.parser as dp


def date_to_epoch(date):
  return int(dp.parse(date).strftime('%s'))


def metric_to_json(metric):
    return {
        'name': metric.get('text', ''),
        'path': metric.get('id', ''),
        'is_expandable': bool(metric.get('expandable', 1)),
        'is_leaf': bool(metric.get('leaf', 0)),
        'allow_children': bool(metric.get('allowChildren', 1))
    }
