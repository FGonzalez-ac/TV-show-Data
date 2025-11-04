This repository makes available the training data and main code described in the following [paper]():

"Climate and Environmental Coverage in Entertainment Television: A Computer-Assisted Approach"

---

### Datasets & Files

The dataset used in the paper is available [here]([https://drive.google.com/file/d/1qWJAjfdX_MmNQqo1V7bjDIbtvgHnbkod/view?usp=sharing](https://zenodo.org/records/17523883?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImQ0YWE1OWEwLTJmODQtNDUzMi04ZDVkLWM1OWEzN2Y4MzFjYSIsImRhdGEiOnt9LCJyYW5kb20iOiI5NDU3MzFjZGE4MTdjYTZiYTdkNjJmMGUwOWRhZWRhYyJ9.MGzc2uIqYrNXnY3915ll7auMjwrigvLD4INmBbwmGjRzxBa1AeUvrzHg-n2ZJ2qYU9g_ANEgY0CD1RS94FuH2A)). After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language'</pre>
The filtered dataset is available [here]([https://drive.google.com/file/d/17rQSS01VLlYUuP3VfmfBMw5_4CZLGvnM/view?usp=drive_link](https://zenodo.org/records/17524099?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjBmZjNjMjY4LTg5MTMtNGUwZC1hZmZhLTdhYjBmM2I3YTk0YyIsImRhdGEiOnt9LCJyYW5kb20iOiJmZWZjNWU1OTAyZGFiMzFkNTI1OTE5Yjg5ZDhhY2RhMSJ9.QEkB7QcCg9PwEDJKNO11liM4NJ1L33q6ueofWKc91TOxSrYOwnewRBTwxT1VonYqsWviP40tv9d-qHfa38wZbQ)). This dataset is the result of filtering the previous dataset with the [`keyword_string`](/keyword_string.py) and piloting some outcomes. After unzipping the file, you will find a CSV file with the following fields:
<pre>'show_title', 'show_description', 'year', 'period', 'script', 'networks', 'production_companies', 'production_countries', 'genres', 'country', 'language', 'keywords', 'text_window', 'topic'</pre>
The results of the [`topic_model`](/topic_model.py) are contained in the 'topic' field.
