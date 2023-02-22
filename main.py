import os
import numpy as np
import mne
import json
import helper
from mne_bids import BIDSPath,write_raw_bids
import shutil
import matplotlib.pyplot as plt

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('config.json') as config_json:
    config = helper.convert_parameters_to_None(json.load(config_json))

data_file = config['fif']
raw = mne.io.read_raw_fif(data_file,verbose=False)




events = mne.find_events(raw,stim_channel=config['stim_channel'],
                            output=config['output'],
                            consecutive=config['consecutive'],
                            min_duration=config['min_duration'],
                            shortest_event=config['shortest_event'],
                            mask=config['mask'],
                            uint_cast=config['uint_cast'],
                            mask_type=config['mask_type'],
                            initial_event=config['initial_event'])

events = mne.pick_events(events,include=config['include'],exclude=config['exclude'])

report = mne.Report(title='Events')

report.add_events(events=events, title='Events',sfreq=raw.info['sfreq'])

fig = mne.viz.plot_events(events, sfreq=raw.info['sfreq'],
                          first_samp=raw.first_samp)

# Create a BIDSPath
bids_path = BIDSPath(subject='subject',
                     session=None,
                     task='task',
                     run='01',
                     acquisition=None,
                     processing=None,
                     recording=None,
                     space=None,
                     suffix=None,
                     datatype='meg',
                     root='bids')

event_id = {}
for ev in events[:,2]:
    event_id[str(ev)] = ev
    
# # Write BIDS to create events.tsv BIDS compliant
write_raw_bids(raw, bids_path, events_data=events, event_id=event_id, overwrite=True)
#
# # Extract events.tsv from bids path
events_file = 'bids/sub-subject/meg/sub-subject_task-task_run-01_events.tsv'
#
# # Copy events.tsv in outdir
shutil.copy2(events_file, 'out_dir/events.tsv')


# == SAVE REPORT ==
report.save('out_dir_report/report.html', overwrite=True)
