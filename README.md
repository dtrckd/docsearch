
**Docsearch** is a self-hosted search engine for your pdf documents based on [pmk](https://github.com/dtrckd/pymake) and [Whoosh](https://github.com/mchaput/whoosh).

# Install

You may need the following packages: `apt-get install poppler-utils default-jdk`

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


# Usage


First, index your pdf documents (take a coffee)

    pmk -x fit --path path/to/your/pdfs/   
    # To index trying to extract title, authors and more feature from article (see [cermine](cermine.ceon.pl))
    pmk -x fit --path path/to/your/pdfs/ --extract-feature

Then, search documents based on text content

    pmk -x search "your text search request"


Show only the first match:

    pmk -x search "your text search request" --limit 1


List information about the project :

* What experiments are there: `pmk -l spec`
* What models are there: `pmk -l model`
* What scripts are there: `pmk -l script`
* Show signatures of methods in scripts ('ir' script)\: `pmk -l --script ir`

To add new models, new scripts, or specs, you need to create them in the dedicated folder following the base class implementations.

