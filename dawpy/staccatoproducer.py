import logging


class Staccatoproducer:
    def __init__(
        self,
        root_notes: str = "C | CD | CDA | CDAF",
        rhythm_notes: str = "qqqq | qqh | hh | w",
        chord_extensions: str = "",
        tempo: int = 90,
    ):
        self.root_notes = root_notes
        self.rhythm_notes = rhythm_notes
        self.chord_extensions = chord_extensions
        self.tempo = tempo

    def get_staccato_header(self):
        return "TODO HEADER LUL "

    def merge_root_rhythm(self, root: str, rhythm: str) -> str:
        logging.info(f"root: {root} | rhythm: {rhythm}")
        notes = []
        for i, c in enumerate(rhythm):
            index = i
            if i >= len(root):
                index %= len(root)
            note = root[index] + c
            notes.append(note)
        return " ".join(notes)

    def merge_root_rhythm_bars(self):
        rhythm_bars = [x.strip() for x in self.rhythm_notes.split("|")]
        root_bars = [x.strip() for x in self.root_notes.split("|")]
        bars = []
        for rhythm, root in zip(rhythm_bars, root_bars):
            bar = self.merge_root_rhythm(root, rhythm)
            bars.append(bar)
            bars.append("|")

        ret = " ".join(bars)
        return ret

    def produce_staccato(self) -> str:
        header = self.get_staccato_header()
        pattern = self.merge_root_rhythm_bars()
        return header + pattern


def main():
    logging.basicConfig(level=logging.INFO)
    s = Staccatoproducer()
    pt = s.produce_staccato()
    print(f"pattern: {pt}")


if __name__ == "__main__":
    main()
