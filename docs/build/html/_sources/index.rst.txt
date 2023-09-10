.. _transcribe_summarize-app:

.. raw:: html

    <style>
        h1 {
            color: #2c3e50;
            font-size: 36px;
        }

        h2 {
            color: #2980b9;
            font-size: 28px;
        }

        .directory-list {
            font-size: 18px;
        }

        .code-block {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            padding: 10px;
        }

        .instructions {
            color: #7f8c8d;
        }
    </style>

Transcription and Summarization: Streamlit App
============================================

Welcome to the documentation for the "transcribe_summarize" project. This documentation will guide you through using and running the app for various tasks, such as transcribing and summarizing audio or video content.

Directories
-----------

In the project repository, you'll find the following directories:

- **data**: This directory contains sample data files that are useful for testing and experimentation. Feel free to use these data files to get started quickly.

- **Notebooks for Google Colab**: The `Notebooks for Google Colab` directory contains Jupyter notebooks designed for use in Google Colab. It includes the following notebooks:

   1. **exploration.ipynb**: This notebook is tailored for data exploration and provides code examples and tutorials related to "transcribe_summarize." Use it to become familiar with the project's data and functionalities.

   2. **streamlit_in_colab.ipynb**: This notebook demonstrates how to run the "transcribe_summarize" Streamlit app within Google Colab, enabling you to use the app's features in a cloud-based environment.

- **docs**: This directory contains everything related to documentation using Sphinx

- **.streamlit**: This directory contains the specific configurations for Streamlit

- **app.py**: This file contains the Streamlit code and the main function that launches the summarization_utils and audio_utils

- **Others files**: 
   * packages.txt is necessary if you want to deploy on streamlit.io, 
   * config.ini contains the API key, 
   * .nojekyll is necessary to deploy the documentation

Installation
------------

Before running the "transcribe_summarize" Streamlit app, you need to install its required dependencies listed in the `requirements.txt` file. You can do this using pip:

.. code-block:: bash

   pip install -r requirements.txt

This command will install all the necessary Python packages and dependencies needed to run the app.

Running the App
---------------

To run the "transcribe_summarize" Streamlit app, use the following command:

.. code-block:: bash

   streamlit run app.py

This command will start the app and open it in your web browser. You can interact with the app's user interface to transcribe and summarize audio or video content.

Usage
-----

Once you have the app running, follow these steps to use it:

1. **Upload an audio or video file**: Utilize the provided file upload widget to select the file you wish to transcribe.

2. **Transcribe and summarize**: Click the "submit" button to convert the spoken words in the file into a summarized text.

3. **View and Export**: View the transcription and summary on the app interface. Additionally, you may have options to export the results as text files or in other formats.

4. **API Key Configuration**: To use the transcription and summarization features, you must configure your API key. Follow these steps:

   - Open the `config.ini` file located in the project's root directory.
   - Replace the placeholder `YOUR_API_KEY_HERE` in the `[API]` section with your actual ChatGPT API key.
   - Ensure that your API key is kept secure and not shared publicly.

5. **GPU for Improved Performance**: While the app can run on CPU, it is recommended to have access to a GPU, especially when transcribing large audio or video files. A GPU significantly accelerates the transcription process. If you plan to transcribe sizable files, consider using a GPU. Please be aware that using a GPU may involve additional setup and costs, depending on your environment.

Bug Reports and Support
------------------------

If you encounter any issues, have questions, or need support, please [open an issue on GitHub](https://github.com/sbendimerad/transcribe-summarize-app/issues) or contact us for assistance.
