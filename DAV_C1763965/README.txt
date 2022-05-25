To run the files 3DPlot.py and RadarPlot.py the data (dnd_monsters.csv) needs to be cleaned up

Run CleanData.py first to clear unnecessary columns
This will create a new .csv file called updated_dnd_monsters.csv which will be used in plotting the data

Both 3DPlot.py and RadarPlot.py can be run from the console using:

    py 3DPlot.py

or

    pt RadarPlot.py

This will open a link to your browser in which the visualisations will be displayed

Use of pip install maybe required for pandas and plotly using:

    pip install pandas
    pip install plotly