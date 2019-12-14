
A local pdf document search engine based on [pmk](https://github.com/dtrckd/pymake) and [Whoosh](https://whoosh.readthedocs.io/en/latest/).

# Install

You may need the following packages: `apt-get install poppler-utils`

Clone the repo and enter inside:

    make setup

# Overview

This repo provide a  **Search Engine** experience which follows the pymake design pattern.

The context of the experiment is as follows:
* **Data**: documents to search-in are pdf documents (like articles for example),
* **Model**: A bm25 model, that assumes a information model of bag of words representation.
* **Script**: There are two scripts:
    + a fit script that builds the index of the *input data*,
    + a search script that returns relevant documents, given a *query*.
* Experiment **Spec** are defined individually for each scripts in the attribute `_default_expe` in the class headers.


Typical usage:

```bash
pmk run --script fit --path path/to/your/pdfs/   # index your pdf documents, take a coffee
pmk run --script search "your text search request"  # show relevant information
```

Or equivalently (aliases):

```bash
pmk -x fit --path path/to/your/pdfs/
pmk -x search "your text search request"
```

Or show only the first match:  `pmk -x search "your text search request" --limit 1`

To add new models, new scripts, or specs,  you need to create it in the dedicated folder following the base class implementations.

Then you can list some information about pymake objects:

* What experiments are there: `pmk -l spec`
* What models are there: `pmk -l model`
* What scripts are there: `pmk -l script`
* Show signatures of methods in scripts ('ir' script)\: `pmk -l --script ir`

