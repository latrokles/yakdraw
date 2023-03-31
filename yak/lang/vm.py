from __future__ import annotations

import os

from dataclasses import dataclass, field

from yak.lang.primitives import Vocabulary, Word, WordRef
from yak.lang.primitives.task import Task
from yak.lang.primitives.syntax import SYNTAX
from yak.util import LOG


@dataclass
class YakVirtualMachine:
    running: bool = False
    tasks: list[Task] = field(default_factory=list)
    vocabularies: dict[str, Vocabulary] = field(default_factory=dict)

    def start(self) -> int:
        self.init()
        self.run()
        return self.shut_down()

    def init(self) -> None:
        LOG.info('booting up...')
        self.init_builtins()
        self.bootstrap()
        self.run()

    def init_builtins(self):
        LOG.info('initializing builtins...')
        self.vocabularies[SYNTAX.name] = SYNTAX

    def bootstrap(self) -> None:
        self.running = True
        pass

    def run(self) -> None:
        iter_count = int(os.getenv('ITERCOUNT', '5'))
        for i in range(iter_count):
            LOG.info(f'executing: {i}!')

    def shut_down(self) -> int:
        LOG.info('shutting down...')
        return 0


    def fetch_word(self, ref: WordRef|str, vocabulary_name: str|None = None) -> Word|None:
        # TODO implement vocabulary lookup
        word = None
        for vocab in self.vocabularies.values():
            if (word := vocab.fetch(str(ref))) is None:
                continue
        return word
