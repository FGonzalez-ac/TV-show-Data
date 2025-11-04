This repository makes available the training data and main code described in the following [paper]():

"Climate and Environmental Coverage in Entertainment Television: A Computer-Assisted Approach"

---

### Datasets & Files

The dataset used in the paper is available [here]([https://doi.org/10.5281/zenodo.17524247]). After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language'</pre>
The filtered dataset is available [here]([https://doi.org/10.5281/zenodo.17524247]). This dataset is the result of filtering the previous dataset with the [`keyword_string`](/keyword_string.py) and piloting some outcomes. After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language', 'keywords', 'text_window', 'topic'</pre>
The results of the [`topic_model`](/topic_model.py) are contained in the 'topic' field.
