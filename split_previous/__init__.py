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

    translator.translate_stroke(Stroke("ß"))
    translator.translate_stroke(Stroke(latest_stroke))

    index = stroke.steno_keys.index("ß")

    newstroke = stroke.steno_keys[0:-1]
    if not "".join(newstroke) == "*":
        translator.translate_stroke(
            Stroke(newstroke))
    else:
        print("found undo")


"""     if stroke.steno_keys.length > 0:
        translator.translate_stroke(
            stroke)
 """
