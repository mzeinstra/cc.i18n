import pkg_resources
import tempfile

from cc.i18n.tools.compile_mo import compile_mo_files
from cc.i18n.gettext_i18n import ugettext_for_locale


def test_compile_mo_files():
    """
    Test that compile_mo_files compiles translations which actually
    have the appropriate output
    """
    output_dir = tempfile.mkdtemp()
    fake_podir = pkg_resources.resource_filename(
        'cc.i18n.tests', 'fake_podir')

    compile_mo_files(fake_podir, output_dir)

    expected_translations = {
        'en': {
            'New Zealand': 'New Zealand',
            'Sampling': 'Sampling',
            ('%(work_title)s by %(work_author)s is licensed under a '
             '<a rel="license" href="%(license_url)s">Creative Commons '
             '%(license_name)s License</a>.'):
                ('%(work_title)s by %(work_author)s is licensed under a '
                 '<a rel="license" href="%(license_url)s">Creative Commons '
                 '%(license_name)s License</a>.')},
        'pt': {
            'New Zealand': 'Nova Zel\xc3\xa2ndia',
            'Sampling': 'Sampling',
            ('%(work_title)s by %(work_author)s is licensed under a '
             '<a rel="license" href="%(license_url)s">Creative Commons '
             '%(license_name)s License</a>.'):
                ('A obra %(work_title)s de %(work_author)s '
                 'foi licenciada com uma Licen\xc3\xa7a '
                 '<a rel="license" href="%(license_url)s">Creative Commons - '
                 '%(license_name)s</a>.')},
        'es': {
            'New Zealand': 'Nueva Zelanda',
            'Sampling': 'Sampling',
            ('%(work_title)s by %(work_author)s is licensed under a '
             '<a rel="license" href="%(license_url)s">Creative Commons '
             '%(license_name)s License</a>.'):
                ('%(work_title)s por %(work_author)s '
                 'se encuentra bajo una Licencia '
                 '<a rel="license" href="%(license_url)s">Creative Commons '
                 '%(license_name)s</a>.')}}

    for language, expected_translations in expected_translations.iteritems():
        gettext = ugettext_for_locale(language, output_dir)
        for msgid, expected_translation in expected_translations.iteritems():
            assert gettext(msgid) == expected_translation.decode('utf-8')
