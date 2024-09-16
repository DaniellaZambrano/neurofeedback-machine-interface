# NMI Neurofeedback Machine Interface

This project captures brainwave signals using the **NeuroSky MindWave** device and the **NeuroPy** library. It logs data such as **attention** and **theta waves** to a CSV file and visualizes the data in real-time with **matplotlib**. The timestamps are represented as the number of seconds since the start of data collection.

## Features

- **Capture Brainwave Data**: Collect signals like attention and theta in real-time from the MindWave device.
- **CSV Logging**: Automatically save the captured data in a structured CSV file.
- **Real-Time Plotting**: Plot the signals on a time-based graph for easy analysis.
- **Elapsed Time**: The data is logged with time measured in seconds since the capture began, not absolute timestamps.

## Requirements

Before running this project, ensure you have the following installed:

- Python 3.x
- NeuroPy library (`pip install NeuroPy`)
- Matplotlib (`pip install matplotlib`)
- A NeuroSky MindWave device

## Installation

1. Clone the repository or download the script files.

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. Run the script:

    ```bash
    python main.py
    ```

## Troubleshooting

- **Error Connecting**

- **Missing Libraries**: Ensure all required libraries are installed. You can use `pip install -r requirements.txt` if you have a `requirements.txt` file listing the libraries.
