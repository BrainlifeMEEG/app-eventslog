# Show events log found in an MEG/EEG file

Brainlife App to display events using MNE-Python [mne.viz.plot_events](https://mne.tools/stable/generated/mne.viz.show_events).

# Documentation

#### Input files are:
* a MEG file in `.fif` format,

#### Input parameters are:
* `stim_channel`: `None` | `str` | `list of str` Name of the stim channel or all the stim channels affected by triggers. If None, the config variables ‘MNE_STIM_CHANNEL’, ‘MNE_STIM_CHANNEL_1’, ‘MNE_STIM_CHANNEL_2’, etc. are read. If these are not found, it will fall back to ‘STI 014’ if present, then fall back to the first channel of type ‘stim’, if present. If multiple channels are provided then the returned events are the union of all the events extracted from individual stim channels. 
* `output`: ‘onset’ | ‘offset’ | ‘step’ Whether to report when events start, when events end, or both. 
* `consecutive`: `bool` | ‘increasing’ If True, consider instances where the value of the events channel changes without first returning to zero as multiple events. If False, report only instances where the value of the events channel changes from/to zero. If ‘increasing’, report adjacent events only when the second event code is greater than the first. 
* `min_duration`: `float` The minimum duration of a change in the events channel required to consider it as an event (in seconds). 
* `shortest_event`: `int` Minimum number of samples an event must last (default is 2). If the duration is less than this an exception will be raised. 
* `mask`: `int` | `None` The value of the digital mask to apply to the stim channel values. If None (default), no masking is performed. 
* `uint_cast`: `bool` If True (default False), do a cast to uint16 on the channel data. This can be used to fix a bug with STI101 and STI014 in Neuromag acquisition setups that use channel STI016 (channel 16 turns data into e.g. -32768), similar to mne_fix_stim14 --32 in MNE-C.   
* `mask_type`: ‘and’ | ‘not_and’ The type of operation between the mask and the trigger. Choose ‘and’ (default) for MNE-C masking behavior.   
* `initial_event`: `bool` If True (default False), an event is created if the stim channel has a value different from 0 as its first sample. This is useful if an event at t=0s is present.   

#### Ouput files are:
* `event.tsv` file, 
* a plot of the events
   

## Authors
- [Maximilien Chaumon](maximilien.chaumon@icm-institute.org)

### Contributors
- [Maximilien Chaumon](maximilien.chaumon@icm-institute.org)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your code and publications. Copy and past the following lines into your repository when using this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
