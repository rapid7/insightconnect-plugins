import komand
import base64


# Specify path for unix utils grep and wc:
awk = "gawk"

# Preprocess expression
def preprocess_expression(log, expression):
    if expression[0].isalnum()\
       or expression.startswith('=')\
       or expression.endswith('='):
        expression = base64.b64decode(expression)
    return expression

# Run awk on text for pattern, return stdout
def process_lines(log, text, expression):
    cmd = 'echo "%s" | %s %s' % (text, awk, expression)
    log.info('ProcessLines: awk %s', expression)
    r = komand.helper.exec_command(cmd)
    return r['stdout']
