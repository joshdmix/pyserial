from twelve_tone.composer import Composer
import numpy as np
import random
import pretty_midi

main_list = []
c = Composer()
for instance in range(0, 100):
    c.compose()
    tone_row = c.get_melody()
    flats = [s for s in tone_row if ("/" in s)]
    fixed_flats = []
    for s in flats:
        sp = s[-2:]
        fixed_flats.append(sp)
    flat_free_tone_row = [s for s in tone_row if not ("/" in s)]
    flatty_tone_row = fixed_flats + flat_free_tone_row
    random_tone_row = random.sample(flatty_tone_row, len(flatty_tone_row))
    main_list += random_tone_row

numbered_list = [s + str(random.randint(0, 8)) for s in main_list]

print(numbered_list)


compo = pretty_midi.PrettyMIDI()

compo_program = pretty_midi.instrument_name_to_program('Cello')

compo_c = pretty_midi.Instrument(program=compo_program)


start = 0
end = .5

for note_name in numbered_list:
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(
        velocity=random.randint(0, 100), pitch=note_number, start=start, end=end)
    compo_c.notes.append(note)
    start = random.randint(0, 1000) * 0.1
    end = random.randint(1, 20) * 0.1


compo.instruments.append(compo_c)
compo.write('compo.mid')
