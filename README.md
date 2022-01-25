# Persian Anagrams

> This repository is made for the NLP course project - Mar 2018.

**Dependencies:**
- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)

---

There are two ways to find out if a permutation of an input word is meaningful:
- Use a local dictionary
- Search an online dictionary, 

In this project, an [online Persian Dictionary](https://www.vajehyab.com/) is used.

---

- Input: a Persian word
- Output: for each permutation, two sets of words are printed - `100% Words` and `50/50 Words`

The results of the online dictionary used in this project may not be 100% meaningful in Farsi, since it also searches through some Arabic sentences.
Therefore, in the results we have a set of words that we are almost sure they are meaningful (`100% Words`), and another set of words that the online dictionary was able to find some results for them, but we are not sure if these words are really meaningful in Farsi (`50/50 Words`).
