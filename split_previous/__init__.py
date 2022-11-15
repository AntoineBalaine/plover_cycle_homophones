#!/usr/bin/env python
from typing import *
import itertools
import functools
import re

from plover.engine import StenoEngine
from plover.translation import Translator, Stroke, Translation
from plover.formatting import _Context, _Action, _atom_to_action, _translation_to_actions
from plover.macro.undo import undo


def split_previous(translator: Translator, stroke: Stroke, cmdline: str):
    translation: Translation(
        outline, translation) = translator.get_state().prev()[-1]
    print(translation)
    latest_stroke = translation.rtfcre[-1]
    print(latest_stroke)

    undo(translator, stroke, cmdline)

    translator.translate_stroke(Stroke("*À"))
    translator.translate_stroke(Stroke(latest_stroke))

    newstroke = stroke.steno_keys[0:-1]
    if not "".join(newstroke) == "*":
        translator.translate_stroke(
            Stroke(newstroke))
    else:
        print("found undo")


def space_or_split(translator: Translator, stroke: Stroke, cmdline: str):
    print(len(stroke.steno_keys))
    print(translator.get_state().prev())
    print(stroke.steno_keys)
    if len(stroke.steno_keys) > 1:
        # is a stroke
        split_previous(translator, stroke, cmdline)
    else:
        # is a space
        translator.translate_stroke(Stroke("*À"))
