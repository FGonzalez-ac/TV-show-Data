This repository makes available the training data and main code described in the following [paper]:

"Greening the Small Screen: Environmental and Climate Coverage in Global Entertainment Television" by Francisco Gonzalez, Chico Camargo, and Saffron O'Neill.

### Datasets

The dataset used in the paper is available [here](https://drive.google.com/file/d/1qWJAjfdX_MmNQqo1V7bjDIbtvgHnbkod/view?usp=sharing). After unzipping the file, you will find a CSV file with the following fields:

'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language'

The filtered dataset containing the [topic modeling]() results ('topic' field) is available [here](https://drive.google.com/file/d/17rQSS01VLlYUuP3VfmfBMw5_4CZLGvnM/view?usp=drive_link). This dataset is the result of filtering the previous dataset with the [scoping keyword string](/keyword_string.py) and piloting some outcomes. After unzipping the file, you will find a CSV file with the following fields:

'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language', 'keywords', 'text_window', 'topic'

