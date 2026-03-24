"""Brainlife App for MNE-Python event detection.

This App loads a `.fif` file, finds events, and saves them to a `.tsv` file.
It also generates a report with a plot of the events.
"""

# Copyright (c) 2026 brainlife.io
#
# Authors:
# - Maximilien Chaumon (https://github.com/dnacombo)
# - Kamilya Salibayeva (https://github.com/KSalibay)
# - Guiomar Niso (https://github.com/guiomar)

import mne
import numpy as np
from mne_bids.write import _events_tsv
import sys
import os

# a workaround for matplotlib TclError
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# import brainlife_utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_image_to_product,
    add_info_to_product
)
from brainlife_utils.report import make_report_events


# set up environment
setup_matplotlib_backend()
config = load_config()
ensure_output_dirs('out_dir', 'out_figs', 'out_report')


# load data
data_file = config.pop('mne')
raw = mne.io.read_raw_fif(data_file, verbose=False)


# find events
events = mne.find_events(raw, **config)


# save events to tsv
_events_tsv(events, np.repeat(0., events.shape[0]), raw, 'out_dir/events.tsv',
            trial_type=None, overwrite=True)

# generate report
report = make_report_events(events, raw.info)


# save report
report.save('out_report/report.html', overwrite=True)

# create product.json
product_items = []
fig = mne.viz.plot_events(events, sfreq=raw.info['sfreq'],
                          first_samp=raw.first_samp)
fig_path = "out_figs/events.png"
fig.savefig(fig_path)
add_image_to_product(product_items, "Events", fig_path)
create_product_json(product_items)
