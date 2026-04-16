This repository makes available the data and main code described in the following paper:

"Climate and Environmental Coverage in Popular Entertainment Television: A Computer-Assisted Text Analysis"

---

### Datasets & Files

The dataset used in the paper is available [here](https://doi.org/10.5281/zenodo.17523882) (shows_dataset in Version v2). After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language'</pre>
The filtered dataset is available [here](https://doi.org/10.5281/zenodo.19186125) (filtered_dataset in Version v3). This dataset is the result of filtering the previous dataset with the [`keyword_string`](/keyword_string.py) and piloting some outcomes. After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'genres', 'country', 'language', 'keywords', 'excerpt', 'topic', 'sampled', 'narrative'</pre>
The results of the [`topic_model`](/topic_model.py) are contained in the 'topic' field. The 'sampled' field indicates whether the excerpt was sampled (True) for the validation and interpretation process or not (False). The 'narrative' field contains the labels of the narratives identified in a particular excerpt.
