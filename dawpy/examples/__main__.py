import logging
from pathlib import Path
import sox
from dawpy.core.daw import Daw, VstPlugin, MidiPattern


def core_example():
    """ core_example
    an example song
    """
    logging.basicConfig(level=logging.INFO)
    d = Daw("example")
    midi = Path("./data/example.mid").absolute()
    dll = Path("./plugins/generators/GTG-Unit-1/Unit 1 Synth.dll").absolute()
    # dll = Path("./plugins/tools/Wusik VM/Wusik VM.dll").absolute()
    fxp = Path("./plugins/generators/GTG-Unit-1/presets/ClickOrgan.fxp").absolute()
    p = VstPlugin(dll, fxp, True)
    # p.configure()
    # d.register_plugin(p)
    pattern = MidiPattern("exammple", 90, midi, p)
    arr = pattern.render()
    sox.core.play(arr)


def main():
    core_example()


if __name__ == '__main__':
    main()
