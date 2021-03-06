import re

import mistune

from django.conf import settings

# python -c 'from django_mistune.utils import markdown, sample_md; print markdown(sample_md)'
# python -c 'from django_mistune.utils import markdown_pdfcommand, sample_md; print markdown_pdfcommand(sample_md)'
# python -c 'from django_mistune.utils import markdown_rtfcommand, sample_md; print markdown_rtfcommand(sample_md)'
sample_md = '''
- 1
    - 2

 | A | B
--- | ---
x | y | z
'''
sample_md = '''
- 1

 | A | B
--- | ---
x | y | z
'''

sample_md = '''
## Hello

- one
- two
  - and a half

Lalala
'''

def markdown(text, renderer=None, inline=None, block=None):

    my_settings = settings.MISTUNE_STYLES if hasattr(settings, 'MISTUNE_STYLES') else {}
    if not renderer:
        renderer = MyRenderer(**my_settings)
    else:
        renderer.options.update(my_settings)

    md = MyMarkdown(renderer, inline, block)
    result = md.render(text)
    return result


class Flattener(object):
    list_level = 0
    supported_tags = ['sub', 'sup', 'br']

    def parse(self, tree):
        return self._parse(tree)[0]

    def _parse(self, tree):
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4)

        rules = []
        value = self.inline()
        for item in tree:
            name = item[0]
            contents = item[1]

            if name == 'paragraph':
                # text
                myrules, myval = self._parse(contents[0])
                rules += [(name, myval)]
                rules += myrules  # this will accomodate to images

            elif name == 'list':
                # body, ordered
                self.list_level += 1
                myrules, myval = self._parse(contents[0])
                rules += myrules
                self.list_level -= 1

            elif name == 'list_item':
                # text
                myrules, myval = self._parse(contents[0])
                if not myval and len(myrules) > 0 and myrules[0][0] == 'paragraph':
                    myval = myrules[0][1]
                    del myrules[0]
                rules += [(name + '_%d' % self.list_level, myval)]
                rules += myrules

            elif name == 'header':
                # text, level, raw
                level = contents[1]
                myrules, myval = self._parse(contents[0])
                rules += [(name + '_%d' % level, myval)]

            elif name == 'table':
                # header, body
                table_data = []
                for table_row in contents:
                    myrules, myval = self._parse(table_row)
                    table_data += myrules
                rules += [('table', table_data)]

            elif name == 'table_row':
                # content
                myrules, myval = self._parse(contents[0])
                rules += [myrules]

            elif name == 'table_cell':
                # content, **flags
                myrules, myval = self._parse(contents[0])
                fmt = item[2]
                rules += [(myval, fmt)]

            elif name == 'hrule':
                rules += [('paragraph', '')]

            elif name in ['block_code', 'block_quote', 'block_html']:
                print('Found %s in markdown' % name, _snippet(contents[0]))


            elif name == 'image':
                # src, title, alt_text
                src = contents[0]
                rules += [(name, src)]  # rules are block-level in the PDF


            elif name == 'autolink':
                # link, is_email
                link = contents[0]
                is_email = item[1][1]
                if is_email:
                    link = 'mailto:%s' % link
                value += self.link(link, contents[0])

            elif name == 'codespan':
                # text
                print('Found codespan in markdown: ',  _snippet(contents[0]))
                # value += ''

            elif name == 'double_emphasis':
                # text
                value += self.double_emphasis(self._parse(contents[0])[1])

            elif name == 'emphasis':
                # text
                value += self.emphasis(self._parse(contents[0])[1])

            elif name == 'linebreak':
                # print 'Found linebreak in markdown'
                value += self.inline('<br/>')

            elif name == 'newline':
                # print 'Found newline in markdown'
                value += self.inline('')

            elif name == 'link':
                # link, title, content
                link = contents[0]
                text = item[1][2]
                value += self.link(link, self._parse(text)[1])

            elif name == 'tag':
                # html
                html = contents[0]
                if re.search('</?(.*?)/?>', html).group(1) in self.supported_tags:
                    value += self.inline(str(html))
                else:
                    print('Found unsupported tag in markdown: ', html)

            elif name == 'strikethrough':
                # text
                value += self.strikethrough(self._parse(contents[0])[1])

            elif name == 'text':
                # text
                value += self.inline(contents[0])

            else:
                print('Found unexpected element in parse tree: %s' % name)
                raise Error(name)

        return rules, value


def _snippet(text):
    default_cutoff = 40
    cutoff = text.find('\n')
    if cutoff == -1:
        cutoff = default_cutoff
    else:
        cutoff = min(cutoff, default_cutoff)
    result = text[:cutoff]
    if len(result) < len(text):
        result += '...'
    return result


class MyMarkdown(mistune.Markdown):
    '''Fix for uneven tables; can be removed in next version of mistune (0.5+)'''

    def output_table(self):
        aligns = self.token['align']
        aligns_length = len(aligns)
        cell = self.renderer.placeholder()

        # header part
        header = self.renderer.placeholder()
        for i, value in enumerate(self.token['header']):
            align = aligns[i] if i < aligns_length else None
            flags = {'header': True, 'align': align}
            cell += self.renderer.table_cell(self.inline(value), **flags)

        header += self.renderer.table_row(cell)

        # body part
        body = self.renderer.placeholder()
        for i, row in enumerate(self.token['cells']):
            cell = self.renderer.placeholder()
            for j, value in enumerate(row):
                align = aligns[j] if j < aligns_length else None
                flags = {'header': False, 'align': align}
                cell += self.renderer.table_cell(self.inline(value), **flags)
            body += self.renderer.table_row(cell)

        return self.renderer.table(header, body)


class MyRenderer(mistune.Renderer):
    '''Markdown HTML rederer that adds target="blank" to links.'''

    def _link_add_target(self, text):
        return text.replace('<a ', '<a target="blank" ')

    def autolink(self, link, is_email=False):
        text = super().autolink(link, is_email)
        result = self._link_add_target(text)
        return result

    def link(self, link, title, content):
        text = super().link(link, title, content)
        result = self._link_add_target(text)
        return result


class TreeRenderer(mistune.Renderer):
    options = {}

    def placeholder(self):
        return []

    def __getattribute__(self, name):
        '''Saves the arguments to each Markdown handling method.'''
        found = name in TreeRenderer.__dict__
        if found:
            return object.__getattribute__(self, name)
        def fake_method(*args, **kwargs):
            # print name, args, kwargs
            return [(name, args, kwargs)]
        return fake_method
