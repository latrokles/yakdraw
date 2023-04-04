from yak.primitives.quotation import Quotation
from yak.primitives.vocabulary import def_vocabulary
from yak.primitives.word import def_primitive
from yak.vocab.combinators import call
from yak.vocab.kernel import swap


__VOCAB__ = 'syntax'


def true(interpreter):
    """( -- t )"""
    interpreter.datastack.push(True)


def false(interpreter):
    """( -- f )"""
    interpreter.datastack.push(False)


def nil(interpreter):
    """( -- nil )"""
    interpreter.datastack.push(None)


def IN(interpreter):
    """( -- )"""
    parser = interpreter.get_global('*parser*')
    with parser.raw() as p:
        vocab_name = p.next_value()
        interpreter.set_current_vocabulary(vocab_name)


def DEFINE(interpreter):
    """( -- name definer-quot quot )"""
    parser = interpreter.get_global('*parser*')

    with parser.raw() as p:
        word_name = p.next_value()
        definer = interpreter.fetch_word('define-word')
        interpreter.datastack.push(word_name)
        interpreter.datastack.push(definer)
        interpreter.datastack.push(Quotation())
        parser.push_exclusive_state(';')


def ENDDEF(interpreter):
    """( word definer -- )"""
    parser = interpreter.get_global('*parser*')
    swap(interpreter)
    definer = interpreter.datastack.pop()
    definer.eval(interpreter)
    parser.pop_exclusive_state(';')


SYNTAX = (def_vocabulary('syntax')
          .store(def_primitive(__VOCAB__, 't', true))
          .store(def_primitive(__VOCAB__, 'f', false))
          .store(def_primitive(__VOCAB__, 'nil', nil))
          .store(def_primitive(__VOCAB__, 'IN:', IN, parse=True))
          .store(def_primitive(__VOCAB__, ':', DEFINE, parse=True))
          .store(def_primitive(__VOCAB__, ';', ENDDEF, parse=True)))
