# Scripts for Processing the Digital Second Edition of Judaica Americana

This repository contains various Python scripts used in the creation of the [Dataset for Judaica Americana: A Bibliography of Publications to 1900](https://repository.upenn.edu/judaica_americana/2/). 
- extract_singerman.py: for extracting the data from the JA draft and writing into a csv 
- flip-index-headers.py: for creating a csv of Singerman IDs and corresponding index headers
- extract_singerman_serials.py: for extracting the data from the JA draft and writing into a csv re: serials

This repository has been forked from [tess](https://github.com/senderle/tess), written by [Jonathan Scott Enderle](https://github.com/senderle). tess was used to create the JA2 index.

## tess

An extremely basic python script for converting PDFs to TIFFs and 
performing OCR with tesseract.

To run the script, first ensure that ImageMagick 7 and Tesseract 4 are 
installed and can be run from the command line. (Later versions may work but
this has only been tested with the above versions.)

You'll also need to ensure that the correct language models are installed.
[The tesseract wiki](https://github.com/tesseract-ocr/tesseract/wiki)
has installation instructions for various operating systems.

Once you have the software installed, you can run the script:

    tess.py [--language LANGUAGE] files [files ...]

    ---------

    files:          One or more PDF files to process
    --language:     The tesseract language ID code for the language model
                        to use. E.g. eng (English), deu (German) or 
                        ita (Italian). The default is eng.

An Italian-language sample file is provided in the `testdata` folder. To 
process it, run the below command:

    tess.py --language ita testdata/1961_Alessandria.pdf

# This is a Judaica Digital Humanities at the Penn Libraries repository.
Judaica Digital Humanities at the <a href="http://library.upenn.edu">Penn Libraries</a> (also referred to as Judaica DH) is a robust program of projects and tools for experimental digital scholarship with Judaica collections, informed by digital humanities, Jewish studies, and cultural heritage approaches. Visit our [website](judaicadh.github.io).
