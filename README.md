# Language Model Perplexity Predicts Scientific Surprise and Transformative Impact

This repository contains the dataset and code used to produce the main results (Main Figs. 1–4) for the paper "Language Model Perplexity Predicts Scientific Surprise and Transformative Impact".

---

## 📁 Repository Structure
Perplexity_Predicts_Scientific_Surprise_DM/
├── code/                   # Source code scripts for data analysis and visualization
├── data/                   # Main datasets supporting the paper's findings
├── README.md               # Documentation (this file)
└── .DS_Store

---

## 📊 Data Files Overview

All dataset files mentioned below are located under the "data/" directory.

### 1. "ppl_jif_citation_llama3_natural_and_social_sciences.parquet"
* **Description**: Contains paper abstract perplexity calculated via the Llama-3-8B model, 2-year journal impact factor (JIF), and citation count for papers in natural and social sciences.
* **Columns**:
  * "perplexity": Abstract perplexity calculated using Llama-3-8B.
  * `impact_factor_2y`: 2-year journal impact factor of the publishing journal.
  * `citation`: Paper citation count.
* **Used for**: **Fig. 1b**, **Fig. 4c**

---

### 2. `word_ratio_title.csv`
* **Description**: Frequency and ratio analyses of key terms identified in prior literature as indicators of novel, innovative, disruptive, surprising, or important research across high- vs. low-perplexity paper groups.
* **Columns**:
  * `word`: Target novelty/disruptiveness keywords.
  * `frequency_top`: Frequency of the word in the top 50% perplexity group.
  * `frequency_bottom`: Frequency of the word in the bottom 50% perplexity group.
  * `ratio`: Ratio between the higher and lower frequency values for standardized comparison.
* **Used for**: **Fig. 1c**

---

### 3. `doi_delay.parquet`
* **Description**: Metadata recording paper DOIs, abstract token counts, perplexity values, and peer review durations.
* **Columns**:
  * `DOI`: Paper Digital Object Identifier.
  * `num_token`: Number of tokens in the paper abstract.
  * `perplexity`: Abstract perplexity.
  * `days_difference`: Review duration (in days).
* **Used for**: **Fig. 2a**, **Fig. 2g**

---

### 4. OpenReview Multi-Model Datasets
* **Files**:
  * `openreview_olmo1b_ppl_rating_confidence_rating-disparity.parquet`
  * `openreview_olmo7b_ppl_rating_confidence_rating-disparity.parquet`
  * `openreview_llama3_ppl_rating_confidence_rating-disparity.parquet`
  * `openreview_deepseek_ppl_rating_confidence_rating-disparity.parquet`
* **Description**: Peer review metrics collected from OpenReview across four different language models (OLMo-1B, OLMo-7B, Llama-3-8B, and DeepSeek).
* **Columns**:
  * `perplexity`: Abstract perplexity from the respective language model.
  * `review_avg_rating`: Average reviewer score.
  * `review_avg_confidence`: Average reviewer confidence score.
  * `rating_max-min`: Score disparity among reviewers (maximum rating minus minimum rating).
* **Used for**: **Fig. 2b**, **Fig. 2c**, **Fig. 2e**, **Fig. 2f**, **Fig. 3a**, **Fig. 3b**

---

### 5. `uncertainty_word_avg.csv`
* **Description**: Frequency of hedge/uncertainty terms used by authors to state claims across top and bottom perplexity groups across four language models.
* **Columns**:
  * `word`: Words expressing authorial uncertainty/hedging.
  * `frequency_top`: Average word frequency in top-perplexity papers across all 4 models.
  * `frequency_bottom`: Average word frequency in bottom-perplexity papers across all 4 models.
  * `top_olmo1b`, `bottom_olmo1b`: Word frequencies in top/bottom groups for OLMo-1B.
  * `top_olmo7b`, `bottom_olmo7b`: Word frequencies in top/bottom groups for OLMo-7B.
  * `top_llama3`, `bottom_llama3`: Word frequencies in top/bottom groups for Llama-3-8B.
  * `top_deepseek`, `bottom_deepseek`: Word frequencies in top/bottom groups for DeepSeek.
* **Used for**: **Fig. 2d**

---

### 6. Field-Specific Datasets (`data/data_field/`)
* **Description**: Contains paper perplexity and journal 2-year impact factor grouped by academic disciplines under the `data/data_field/` folder.
* **Used for**: **Fig. 2h**, **Fig. 2i**, **Fig. 4a**, **Fig. 4b**, **Fig. 4e**, **Fig. 4f**

---

### 7. Semantic Scholar Award Datasets
* **Files**:
  * `semantic_scholar_ppl_award_olmo1b.parquet`
  * `semantic_scholar_ppl_award_olmo7b.parquet`
  * `semantic_scholar_ppl_award_llama3.parquet`
  * `semantic_scholar_ppl_award_deepseek.parquet`
* **Description**: Pairs paper abstract perplexity values (across 4 models) with award recognition status from Semantic Scholar.
* **Columns**: Perplexity values for the given model and corresponding award indicator status.
* **Used for**: **Fig. 3c**

---

### 8. `4_ppl_funding_institution.parquet`
* **Description**: Multi-model paper perplexity measures paired with funding agency attribution information.
* **Columns**:
  * `perplexity_olmo1b`: Perplexity calculated via OLMo-1B.
  * `perplexity_olmo7b`: Perplexity calculated via OLMo-7B.
  * `perplexity_llama3`: Perplexity calculated via Llama-3-8B.
  * `perplexity_deepseek`: Perplexity calculated via DeepSeek.
  * `funding_institute`: Funding institute / agency supporting the research.
* **Used for**: **Fig. 3d**, **Fig. 3e**

---

### 9. Multi-Model Perplexity & Citation Data (Natural & Social Sciences)
* **Files**:
  * `ppl_jif_citation_olmo1b_natural_and_social_sciences.parquet`
  * `ppl_jif_citation_olmo7b_natural_and_social_sciences.parquet`
  * `ppl_jif_citation_llama3_natural_and_social_sciences.parquet`
  * `ppl_jif_citation_deepseek_natural_and_social_sciences.parquet`
* **Description**: Multi-model comparative datasets for natural and social sciences papers.
* **Columns**:
  * `perplexity`: Abstract perplexity under the specified language model.
  * `impact_factor_2y`: 2-year journal impact factor.
  * `citation`: Citation count.
* **Used for**: **Fig. 4c**

---

### 10. Interdisciplinary Citations & References (Natural & Social Sciences)
* **Files**:
  * `4_ppl_interdisciplinary_reference_natural-and-social-science.parquet`
  * `4_ppl_interdisciplinary_citation_natural-and-social-science.parquet`
* **Description**: Interdisciplinary linkages of focal papers in natural and social sciences via references and forward citations.
* **Columns**:
  * `id`: Focal paper unique identifier (a single ID can appear in multiple rows corresponding to multiple cited/citing papers).
  * `perplexity_olmo1b`, `perplexity_olmo7b`, `perplexity_llama3`, `perplexity_deepseek`: Perplexity scores across the four language models.
  * `interdisciplinary`: Boolean/categorical flag indicating whether the corresponding reference or citation is interdisciplinary.
* **Used for**: **Fig. 4d**

---

### 11. Multi-Model Perplexity & Citation Data (Arts & Humanities)
* **Files**:
  * `ppl_jif_citation_olmo1b_arts_and_humanities.parquet`
  * `ppl_jif_citation_olmo7b_arts_and_humanities.parquet`
  * `ppl_jif_citation_llama3_arts_and_humanities.parquet`
  * `ppl_jif_citation_deepseek_arts_and_humanities.parquet`
* **Description**: Multi-model datasets for arts and humanities papers, structured identically to item #9.
* **Columns**: `perplexity`, `impact_factor_2y`, `citation`
* **Used for**: **Fig. 4g**

---

### 12. Interdisciplinary Citations & References (Arts & Humanities)
* **Files**:
  * `4_ppl_interdisciplinary_reference_art-and-humanities.parquet`
  * `4_ppl_interdisciplinary_citation_art-and-humanities.parquet`
* **Description**: Interdisciplinary linkages of focal papers in arts and humanities via references and forward citations, structured identically to item #10.
* **Columns**: `id`, `perplexity_olmo1b`, `perplexity_olmo7b`, `perplexity_llama3`, `perplexity_deepseek`, `interdisciplinary`
* **Used for**: **Fig. 4h**

---

## 📊 Figure to Data File Mapping Summary

| Figure | Associated Data File(s) |
| :--- | :--- |
| **Fig. 1b** | `ppl_jif_citation_llama3_natural_and_social_sciences.parquet` |
| **Fig. 1c** | `word_ratio_title.csv` |
| **Fig. 2a, 2g** | `doi_delay.parquet` |
| **Fig. 2b, 2c, 2e, 2f** | `openreview_*_ppl_rating_confidence_rating-disparity.parquet` (4 files) |
| **Fig. 2d** | `uncertainty_word_avg.csv` |
| **Fig. 2h, 2i** | Files inside `data_field/` |
| **Fig. 3a, 3b** | `openreview_*_ppl_rating_confidence_rating-disparity.parquet` (4 files) |
| **Fig. 3c** | `semantic_scholar_ppl_award_*.parquet` (4 files) |
| **Fig. 3d, 3e** | `4_ppl_funding_institution.parquet` |
| **Fig. 4a, 4b, 4e, 4f** | Files inside `data_field/` |
| **Fig. 4c** | `ppl_jif_citation_*_natural_and_social_sciences.parquet` (4 files) |
| **Fig. 4d** | `4_ppl_interdisciplinary_reference_natural-and-social-science.parquet`, `4_ppl_interdisciplinary_citation_natural-and-social-science.parquet` |
| **Fig. 4g** | `ppl_jif_citation_*_arts_and_humanities.parquet` (4 files) |
| **Fig. 4h** | `4_ppl_interdisciplinary_reference_art-and-humanities.parquet`, `4_ppl_interdisciplinary_citation_art-and-humanities.parquet` |
