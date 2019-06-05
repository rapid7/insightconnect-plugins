import komand
from .schema import GeneratePdfInput, GeneratePdfOutput
# Custom imports below
from base64 import b64encode
from textwrap import wrap
from weasyprint import HTML
from cgi import escape


class GeneratePdf(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='generate_pdf',
                description='Generate a PDF from a text input',
                input=GeneratePdfInput(),
                output=GeneratePdfOutput())

    def run(self, params={}):
        text = params.get('text')

        html_template = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title></title></head>
<body><pre>{}</pre></body>
</html>"""
        # Wrap text preserving existing newlines
        text = '\n'.join(
            wrapped for line in text.splitlines() for wrapped in wrap(
                line, width=70, expand_tabs=False,
                replace_whitespace=False, drop_whitespace=False
            )
        )
        text = escape(text)
        html_content = html_template.format(text)
        pdf_content = HTML(string=html_content).write_pdf()

        b64_content = b64encode(pdf_content).decode()

        return {'pdf': b64_content}

    def test(self):
        return {
            'pdf': (
                'JVBERi0xLjMKJeLjz9MKMSAwIG9iago8PC9BdXRob3IgPD4gL0NyZWF0b3IgK'
                'GNhaXJvIDEuMTQuMCAoaHR0cDovL2NhaXJvZ3JhcGhpY3Mub3JnKSkKICAvS2'
                'V5d29yZHMgPD4gL1Byb2R1Y2VyIChXZWFzeVByaW50IDAuNDIuMyBcKGh0dHA'
                '6Ly93ZWFzeXByaW50Lm9yZy9cKSkKICAvVGl0bGUgPD4+PgplbmRvYmoKMiAw'
                'IG9iago8PC9QYWdlcyAzIDAgUiAvVHlwZSAvQ2F0YWxvZz4+CmVuZG9iagozI'
                'DAgb2JqCjw8L0NvdW50IDEgL0tpZHMgWzQgMCBSXSAvVHlwZSAvUGFnZXM+Pg'
                'plbmRvYmoKNCAwIG9iago8PC9CbGVlZEJveCBbMCAwIDU5NSA4NDFdIC9Db25'
                '0ZW50cyA1IDAgUiAvR3JvdXAKICA8PC9DUyAvRGV2aWNlUkdCIC9JIHRydWUg'
                'L1MgL1RyYW5zcGFyZW5jeSAvVHlwZSAvR3JvdXA+PiAvTWVkaWFCb3gKICBbM'
                'CAwIDU5NSA4NDFdIC9QYXJlbnQgMyAwIFIgL1Jlc291cmNlcyA2IDAgUiAvVH'
                'JpbUJveCBbMCAwIDU5NSA4NDFdCiAgL1R5cGUgL1BhZ2U+PgplbmRvYmoKNSA'
                'wIG9iago8PC9GaWx0ZXIgL0ZsYXRlRGVjb2RlIC9MZW5ndGggMjEgMCBSPj4K'
                'c3RyZWFtCnicNYyxCsJAEET7/YoptUhub8mephUES4UtbUK4C0iM5i7/j0fAa'
                'ob3hllphbsP2xbzgrHAfRVlXOAGxlSIwdBece48ckSix44YefpPLkZedlYjSC'
                'uKU/BtYO1CD3uTSw031cISHZ4i/hbn+VOLHO1FV6ufP7cSH6UKZW5kc3RyZWF'
                'tCmVuZG9iago2IDAgb2JqCjw8L0V4dEdTdGF0ZSA8PC9hMCA8PC9DQSAxIC9j'
                'YSAxPj4+PiAvRm9udCA8PC9mLTAtMCA3IDAgUj4+IC9QYXR0ZXJuCiAgPDwvc'
                'DUgOCAwIFI+Pj4+CmVuZG9iago3IDAgb2JqCjw8L0Jhc2VGb250IC9YTVpMSl'
                'ErRGVqYVZ1U2Fuc01vbm8gL0VuY29kaW5nIC9XaW5BbnNpRW5jb2RpbmcgL0Z'
                'pcnN0Q2hhcgogIDMyIC9Gb250RGVzY3JpcHRvciAxNiAwIFIgL0xhc3RDaGFy'
                'IDE0NiAvU3VidHlwZSAvVHJ1ZVR5cGUgL1RvVW5pY29kZQogIDE3IDAgUiAvV'
                'HlwZSAvRm9udCAvV2lkdGhzCiAgWzAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwID'
                'AgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMAo'
                'gIDAgMCAwIDAgMCA2MDIgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAg'
                'MCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMAogIDYwMiAwIDAgMCAwIDAgMCA2M'
                'DIgMCAwIDYwMiAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMC'
                'AwIDAgMAogIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDYwMiA2MDJdPj4KZW5'
                'kb2JqCjggMCBvYmoKPDwvQkJveCBbMCAxMTIzIDc5NCAyMjQ2XSAvTGVuZ3Ro'
                'IDkgMCBSIC9NYXRyaXggWzAuNzUgMCAwIDAuNzUgMCAtODQzLjVdCiAgL1Bha'
                'W50VHlwZSAxIC9QYXR0ZXJuVHlwZSAxIC9SZXNvdXJjZXMgPDwvWE9iamVjdC'
                'A8PC94OCAxMCAwIFI+Pj4+CiAgL1RpbGluZ1R5cGUgMSAvWFN0ZXAgMTU4OCA'
                'vWVN0ZXAgMjI0Nj4+CnN0cmVhbQogL3g4IERvCiAKCmVuZHN0cmVhbQplbmRv'
                'YmoKOSAwIG9iagoxMAplbmRvYmoKMTAgMCBvYmoKPDwvQkJveCBbMCAxMTIzI'
                'Dc5NCAyMjQ2XSAvRmlsdGVyIC9GbGF0ZURlY29kZSAvTGVuZ3RoIDExIDAgUi'
                'AvUmVzb3VyY2VzCiAgMTIgMCBSIC9TdWJ0eXBlIC9Gb3JtIC9UeXBlIC9YT2J'
                'qZWN0Pj4Kc3RyZWFtCnicK+QKVCjkMlAwMjIxUzC3NNYzs7RU0DU0NDLSMzVS'
                'KEpVCFfI4yrkMlQwAEIQCZQyVkjO5dJPNFBIL1bQrzA0UnDJ5woEQgBg+RASC'
                'mVuZHN0cmVhbQplbmRvYmoKMTEgMCBvYmoKNzcKZW5kb2JqCjEyIDAgb2JqCj'
                'w8L0V4dEdTdGF0ZSA8PC9hMCA8PC9DQSAxIC9jYSAxPj4+PiAvWE9iamVjdCA'
                '8PC94MTIgMTMgMCBSPj4+PgplbmRvYmoKMTMgMCBvYmoKPDwvQkJveCBbMCAx'
                'MTIzIDAgMTEyM10gL0ZpbHRlciAvRmxhdGVEZWNvZGUgL0xlbmd0aCAxNCAwI'
                'FIgL1Jlc291cmNlcwogIDE1IDAgUiAvU3VidHlwZSAvRm9ybSAvVHlwZSAvWE'
                '9iamVjdD4+CnN0cmVhbQp4nCvkCuQCAAKSANcKZW5kc3RyZWFtCmVuZG9iago'
                'xNCAwIG9iagoxMgplbmRvYmoKMTUgMCBvYmoKPDw+PgplbmRvYmoKMTYgMCBv'
                'YmoKPDwvQXNjZW50IDkyOCAvQ2FwSGVpZ2h0IDEwNDEgL0Rlc2NlbnQgLTIzN'
                'SAvRmxhZ3MgMzIgL0ZvbnRCQm94CiAgWy01NTcgLTM3NCA3MTcgMTA0MV0gL0'
                'ZvbnRGYW1pbHkgKERlamFWdSBTYW5zIE1vbm8pIC9Gb250RmlsZTIgMTkgMCB'
                'SCiAgL0ZvbnROYW1lIC9YTVpMSlErRGVqYVZ1U2Fuc01vbm8gL0l0YWxpY0Fu'
                'Z2xlIDAgL1N0ZW1IIDgwIC9TdGVtViA4MAogIC9UeXBlIC9Gb250RGVzY3Jpc'
                'HRvcj4+CmVuZG9iagoxNyAwIG9iago8PC9GaWx0ZXIgL0ZsYXRlRGVjb2RlIC'
                '9MZW5ndGggMTggMCBSPj4Kc3RyZWFtCnicXZDJbsMgEIbvPMUc00MEttIolpC'
                'lKr340EV1+wAYBhepBoTxwW9fliiVegC+YeafjV6H58GaCPQ9ODliBG2sCri6'
                'LUiECWdjSdOCMjLerHLLRXhCk3jc14jLYLUjnAP9SM41hh0OT8pN+EAAgL4Fh'
                'cHYGQ5f17F+jZv3P7igjcBI34NCndK9CP8qFgRaxMdBJb+J+zHJ/iI+d4/QFr'
                'upLUmncPVCYhB2RsIZ64Fr3RO06p/vXBWTlt8iEN41KbJlzaUn/HRJzNgp8/m'
                'xcHoSy8oys66ccvOurdqu1LllzBXzau6jyC2ENEXZX2k/N24s3lfsnc+qcn4B'
                't297UQplbmRzdHJlYW0KZW5kb2JqCjE4IDAgb2JqCjI1NQplbmRvYmoKMTkgM'
                'CBvYmoKPDwvRmlsdGVyIC9GbGF0ZURlY29kZSAvTGVuZ3RoIDIwIDAgUiAvTG'
                'VuZ3RoMSA0MTcyPj4Kc3RyZWFtCnic3VZ7WJRVGn/P9/vODAzDMDPMIMjFGWl'
                'Qg1EuqUGZA97TzLQ21CwvSJQRllq2hFKu5QVCS8dLVK6ZlWsttaZTKFlq2qK5'
                'JlipZZblUqy5pliIh31nsO3Z3ad99qk/9tk9Z773vL/3nPd6zvm+IUFEJionk'
                'GtK8aTph795ajoRfETauCn3zXQ1rTCaiWQ14/TC6bcXj9emHSMy7mWtjbff9U'
                'DhJ9cnjgryPL+saOqkgotpi9cQhc1mWZ8iFoQFNBPjGsaXFRXPnO3eYshi3MA'
                '44a6SKZPYeRjj04xdxZNmT5cv6d2Iwq1BPP3eqdNzdm83Mk5nn/GkUZHy60Vy'
                'HUdrpC5bSRcOXmgQjs0iTM7TdOq1s6E5g6wNzQ3N6dE2t83jtrmLdGqbgfi2L'
                '5TfaPnuzL2GHqxDQuzHbngNDpIU64ugZ/GaATolCoO1oa1hLxtpa04Xyb2js6'
                'DVt+1cPRm794s56uGQLi0k0ofKRoqgFJ8jbIX2ik4LTAYjkmRGuEiidDNrZ/I'
                'vg3pdfYKZ9OgsjibLlsw0eWG91qO+/uIH9bLxYrVW0Jqq7b6YHbSrUWn753q+'
                'XkpOSqBBvhSKgTAtDq80xGwWhopI8VZcRXRd5KpEaAnW8BgDDUuwW4cmWs82t'
                'zXvtNmzsznqE2ebT1hPcT97yp5ty04XTrfTEZOV2aev0yKSXWSzUlam3dhTJH'
                'c1GPX8ts/ffDl/e/EdO8arC+qwcJ0+dD6gL10wf6NVu3WcYcueK7O3pKaKbBE'
                'tzMKnPtm19sWaas6f91g3GbpQJOcfHU4wbTbvwmYJg06GiBHhFt6Btr3BeHpx'
                'aLZsDsMRc5VwJndN6W1z93Zrc8eP/aDpudfUR+KY8D84p7rhbXy/hPNfyPkP5'
                'fwjqBMl+6INFXaqMNfZV8WG26MGwu68JjaUbEee1lPpoquhI7veV6R0y7TbrF'
                'pyV81mtWtFFUuWVFQuWVLZdL7lq6aWFhw7fKjxyJHGQ4er1fvqM3VcHRRe0UU'
                'kiZ7/chbwLAXPgkgkQ/Ak/XAWspxIjtYy2natmmxwvKceEnOJOk4DKHiLzKRr'
                'I3lMIitLLDSX2sUYMUnMFnPE49o72lFXiivdlePa6O7a3h4837RGjBYTeb7s0'
                'nw0z2f/ff6nm2AfR8VqUS2e5r7mUn+H+x6x599q/rym/WxN/APSQ1T+olj+95'
                'sgw3+4MkD1oWeDWMpjYUjyqDaX9+OHHqAdPK+F1gVEvVgo3mB+PbUxnUdnhAm'
                '7RV/m6lg3X3eztIqqQ5pVOEmzsJUO0rt0hLmTIhusKw6SWxxjawt/9II6RjuY'
                'lqIO+XxpimmdeJktlrLPEpqr8aiNZsv79AMs3UePcn+C1lEJ88HI5nH8H9MmW'
                'kxnaaXWROOYf4N2cTyK70nIh2ikFra0QeunFfK6XWxtNa0W86iRZugkTLzyuG'
                'zUUtnqJs6AaDJVy0a5MlgPHhvlaZ4hSjQEDA5jMmcRrNt6sVVk8J08yPqldCN'
                'uwT04Iubryfr9aKIqjTCR7qT9spFvfpUxmaoMheIBfWKolwbz0+7XJ4oN1MQ2'
                'J+M7xm6OrDqUMdEmbbQcKUdyzoUsqw7Rqg5qsNI+tHLdl2pKDNUHoz/PlOoja'
                'CWtZc1uXBmiEvRm7yVUKis7Om3g7pWV8LP9UDVEltaPqrVCsZijbeFqlmAg9W'
                'UfifIUzRebOG4yltEM/hKRg7YYDVKHJijNZa3RPMMKanw35Lv2jHV70/4Juqx'
                'GVw2Nqol8wBVobx+Vr8fLsTUyoQaesBrdk3z8pyaPe9OGj8p3BUSnQQMvmR00'
                'cSALx+QzG0QsZvmggaG5oNca6eHfsIk1rilFrkXWRck5i6xTc7yhN6Z2s2nf4'
                '4a1t0VdfY66hIWO/Hv559w/jBcWXRSyLuwmhmGhe9Nxe8hYrBL5ZXLgwqJ2h6'
                'y7JP+xGXlHivQDYj+PC/kp5WdNBy/2X1ozgp8F/HzKBnkUPGr5wf8wIWtGzUy'
                'pNI3vqcbv8lVB7/JmYeM3l/66Vi6cry6bIHMThJP8BKblof8hivnoELWTnakt'
                'xFtDNIoPM4QlxEe++vUQmesRkVTGyEwephGUydQUshceWhXGFwPCGOINoTUyx'
                'OshOUISLSQRvrEKSuFiGdoULii0ZuL7WnxXhvMtFfK8wvntesu5sbKlAi3l+r'
                'mzKfLcWJzz6WdT8O2ZXvLbVpzphb8qnFb4JhOnHPiLH80cYrNCc6D9gK9d/3o'
                'IvmoqkF/50VSAPyuc/DJenlT4Mh5fKJyYhs8VPqvF8U/j5PFWfBqHY358ovCx'
                'wtEjTnlU4YgTh/346EOn/Ejhw8oI+aETH5ThUA4aGTTmoEHh4PsmeVDhfRMOK'
                'PxJYf8im9yfgPdisE9hrx/1iz2yXuGPCu+WYY/CboV3FHatjpQ7FXYovK3wls'
                'J2trfdgTfNqNtWK+sUtm2dILfVYlu5vrXWI7dOwFafXuvBGwqv+xGoypVbFDb'
                'zsLkVr7GtTQp/KMCrBXjFgho7fq/wsvJdxEsKGxV+Z8cGhRdfsMgXM/GCBc+v'
                't8nnu2O9Dc+t88rnyrDOi2cV1ir8VmHNM3FyTQGeedoqn4nD01Y8ZUK1wpPs5'
                'EmF1ZFYtbKnXKWwsidWsP8VfviX10q/wnI+W8trsbxcX7bEI5dNwDKf/oTC4w'
                'pLGS+txRIPqrgYVbl4jLN9zIHKCFSwoKIAi7loiz1YZMNChQUKjyo8Mt8mH1G'
                'Yb8NvFOYpPGzLkw+PwUMK5bMxd06ZnKswpwxlSXhQodSCXyvcr3CfwqyZZjkr'
                'CrMCgnyH9ZlmzNyuz7Bjhk+/V+EehekKJXePkSV+3F3cXd49BsXdcZfCtEzcq'
                'XBHJopacXstChWmKhQoTJmcJKcoTCarnJyESQoTFW5TuHVchLzVggkFuGUPxj'
                'MY78C4CPCJznfgZoVfKdwUHydvysSNCmMURivcUIZRCtc7MFLhOuGV1ymMqMX'
                'w7rh2WKy8ti+GDbDLYbEYOihWDlUYwmhIAQYzGlyLQbEYyIKBfTEgzyYH2DEg'
                'oPl84XpebpTMsyEvoBGjXJ9F5kYhNyC2M/L1N0ufBb6AKGfU3xwu+5vRPyB8v'
                'gL9GoV+HEK/VlytcFV35Chkc4GzC3BlRmd55XD0Vejjdcg+Cr2H44r0zvKK4c'
                'jiIUshkxdmKmTwdEZnpHdGL+Z6xaJneIzsWQtvWrT0OuANaEG3aVabTItGWjB'
                'cv556uUemKlzOKy/3oIeWI3sodFfoppASBU9MnvQMwmVRSFboGhUluyq4XV7p'
                'LoPLiy7DkcSekxQSFRK4tgkK8bwr8XHorBCnEKvQiS10GowYp1fG5MHpsEqnF'
                'w4ronldtAN21rcr2DhzWx6s7MFqg7WjdlEWs4yKQlRH7SyRJmkxw9JRu0iuXa'
                'QJkVy7Tbo5HObg2eqrRyiYOBOTQngMwqwwKhjYtEFBOgBODq38UfNKLQeCAxB'
                'ekBUiIArmV4rU/59G/+0AfmFLpL8B9eHe4wplbmRzdHJlYW0KZW5kb2JqCjIw'
                'IDAgb2JqCjI2MTMKZW5kb2JqCjIxIDAgb2JqCjEyMQplbmRvYmoKeHJlZgowI'
                'DIyCjAwMDAwMDAwMDAgNjU1MzUgZg0KMDAwMDAwMDAxNSAwMDAwMCBuDQowMD'
                'AwMDAwMTgwIDAwMDAwIG4NCjAwMDAwMDAyMjcgMDAwMDAgbg0KMDAwMDAwMDI'
                '4MiAwMDAwMCBuDQowMDAwMDAwNTAxIDAwMDAwIG4NCjAwMDAwMDA2OTUgMDAw'
                'MDAgbg0KMDAwMDAwMDc5NyAwMDAwMCBuDQowMDAwMDAxMjQwIDAwMDAwIG4NC'
                'jAwMDAwMDE0NjcgMDAwMDAgbg0KMDAwMDAwMTQ4NSAwMDAwMCBuDQowMDAwMD'
                'AxNzEwIDAwMDAwIG4NCjAwMDAwMDE3MjkgMDAwMDAgbg0KMDAwMDAwMTgwOSA'
                'wMDAwMCBuDQowMDAwMDAxOTY3IDAwMDAwIG4NCjAwMDAwMDE5ODYgMDAwMDAg'
                'bg0KMDAwMDAwMjAwNyAwMDAwMCBuDQowMDAwMDAyMjU1IDAwMDAwIG4NCjAwM'
                'DAwMDI1ODQgMDAwMDAgbg0KMDAwMDAwMjYwNCAwMDAwMCBuDQowMDAwMDA1Mz'
                'A1IDAwMDAwIG4NCjAwMDAwMDUzMjYgMDAwMDAgbg0KdHJhaWxlcgoKPDwvSW5'
                'mbyAxIDAgUiAvUm9vdCAyIDAgUiAvU2l6ZSAyMj4+CnN0YXJ0eHJlZgo1MzQ2'
                'CiUlRU9GCg=='
            )
        }
