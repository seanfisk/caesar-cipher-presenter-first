""":mod:`caesar_cipher.curses.views` --- curses user interface
"""

import urwid

from caesar_cipher.utils import Event


def field_attr(widget):
    return urwid.AttrMap(widget, 'field')


class ApplicationView(object):
    """Primary application view."""
    submitted = Event()
    text_changed = Event()
    auto_encrypt_toggled = Event()

    palette = [
        ('title', 'white', 'black'),
        ('bg', 'default', 'light blue'),
        ('field', 'black', 'light gray'),
    ]

    def __init__(self):
        self.title_map = urwid.AttrMap(
            urwid.Text('Caesar Cipher', align='center'), 'title')
        self.help_map = urwid.AttrMap(
            urwid.Text('Esc: quit  Up/Down: shift between fields'), 'title')
        self.text_edit = urwid.Edit(caption='Text: ')
        urwid.connect_signal(self.text_edit, 'change',
                             self._text_input_changed)
        self.text_edit_map = field_attr(self.text_edit)
        self.key_edit = urwid.IntEdit(caption='Key: ')
        self.key_edit_map = field_attr(self.key_edit)
        self.auto_encrypt_checkbox = urwid.CheckBox(label='Auto-Encrypt',
                                                    has_mixed=False)
        urwid.connect_signal(self.auto_encrypt_checkbox, 'change',
                             self._auto_encrypt_state_changed)
        self.auto_encrypt_map = field_attr(self.auto_encrypt_checkbox)
        self.result_text = urwid.Text('')
        self.result_text_map = field_attr(self.result_text)
        self.encode_button = urwid.Button('Encode')
        self.encode_button_map = field_attr(self.encode_button)
        urwid.connect_signal(self.encode_button, 'click',
                             self._submit_clicked)
        self.body_content = urwid.SimpleListWalker([self.text_edit_map,
                                                    urwid.Divider(),
                                                    self.key_edit_map,
                                                    urwid.Divider(),
                                                    self.auto_encrypt_map,
                                                    urwid.Divider(),
                                                    self.result_text_map,
                                                    urwid.Divider(),
                                                    self.encode_button_map])
        self.body_listbox = urwid.ListBox(self.body_content)
        self.overlay_bottom = urwid.Frame(urwid.SolidFill(),
                                          header=self.title_map,
                                          footer=self.help_map)
        self.overlay_bottom_map = urwid.AttrMap(self.overlay_bottom, 'bg')
        self.top = urwid.Overlay(self.body_listbox,
                                 self.overlay_bottom_map,
                                 'center',
                                 ('relative', 50),
                                 'middle',
                                 ('relative', 50))

    def start(self):
        """Start the main loop."""
        loop = urwid.MainLoop(self.top,
                              palette=self.palette,
                              unhandled_input=self._exit)
        loop.run()

    def get_text(self):
        """Return the widget's entered text.

        :return: the text
        :rtype: :class:`str`
        """
        return self.text_edit.get_edit_text()

    def get_key(self):
        """Return the widget's entered key.

        :return: the key
        :rtype: :class:`str`
        """
        return self.key_edit.get_edit_text()

    def set_result(self, result):
        """Set encoded text result.

        :param result: the encoded text
        :type result: :class:`str`
        """
        self.result_text.set_text(result)

    def show_error(self, message):
        """Show the user an error message.

        :param message: error message
        :type message: :class:`str`
        """
        self.result_text.set_text('Error: invalid key')

    def _submit_clicked(self, button):
        self.submitted(self.get_text(), self.get_key())

    def _auto_encrypt_state_changed(self, checkbox, state):
        self.auto_encrypt_toggled(state)

    def _text_input_changed(self, edit_field, text):
        self.text_changed(text, self.get_key())

    def _exit(self, input):
        if input == 'esc':
            raise urwid.ExitMainLoop()
