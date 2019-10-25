# This program records audio from an audio input device (like a microphone),
# stores it in a string, splits the string into words, prints the words
# in the specified list format, and copies the list to the clipboard.

import logging
import nltk
import pyperclip
import speech_recognition as sr

logger = logging.getLogger(__name__)


class Record:
    _r1 = sr.Recognizer()
    _r2 = sr.Recognizer()
    _r3 = sr.Recognizer()
    is_numbered = False

    # Records contents of the list from the input device and
    # returns those contents as a string
    # Saves the type of the list in the 'is_ordered' variable
    def record_audio(self):
        with sr.Microphone() as _input:
            print('Wait two seconds, then specify the type of list. \'number\' for '
                  'a numbered list, \'bullet\' for an '
                  'unordered list')
            self._r3.adjust_for_ambient_noise(_input, duration=2)
            _audio = self._r3.listen(_input)

        if 'number' in self._r1.recognize_google(_audio):
            self.is_numbered = True
        if 'bullet' in self._r1.recognize_google(_audio):
            self.is_numbered = False

        with sr.Microphone() as _input:
            if self.is_numbered is True:
                print('Say the words you want to be in the numbered list.')
            else:
                print('Say the words you want to be in the bulleted list.')
            self._r1.adjust_for_ambient_noise(_input, duration=0.7)
            _audio = self._r1.listen(_input)
            try:
                _get = self._r1.recognize_google(_audio)
                return _get
            except sr.UnknownValueError:
                logger.error("Unknown value", exc_info=True)

            except sr.RequestError as e:
                logger.error('failed'.format(e))

    @staticmethod
    def copy_to_clipboard(_list=None):
        if _list is None:
            _list = "1. item1\n2. item2\n3. item3\n"
        pyperclip.copy(str(_list))

    @staticmethod
    def split_into_words(_words="item1 item2 item3"):
        _tokens = nltk.word_tokenize(_words)
        return _tokens

    # Prints the elements of the list separated
    # by newline characters, with the number or
    # bullet point preceding each element.
    def print_list(self, _split_list=None, _ordered=False):
        if _split_list is None:
            _split_list = ['item1', 'item2', 'item3']
        _to_copy = ""
        if _ordered is True:
            _count = 0
            for x in _split_list:
                _count += 1
                _to_copy += str(_count) + ". " + str(x) + "\n"
            self.copy_to_clipboard(_to_copy)
            return _to_copy
        if _ordered is False:
            for x in _split_list:
                _to_copy += "• " + str(x) + "\n"
            self.copy_to_clipboard(_to_copy)
            return _to_copy
