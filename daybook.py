import pandas as pd 
# from matplotlib import pyplot as plt

class CovidDataAnalyzer:

    def __init__(self, path: str):
        self.data = []
        self.filtered_data = []
        self.path = path

    def load_data(self) -> None:
        """Load data from a CSV file"""
        import pandas as pd 
        self.data = pd.read_csv(self.path)
        print("The data loaded succesfully.")

    def describe_data(self) -> None:
        """The first view of the Covid 19 Dataset """
        if not self.data:
            print("No data provided")
        
        print(f"The Covid_19 Data have {self.data.shape[0]} rows and {self.data.shape[1]} columns.\n")
        print(f"\nThe names of the columns and some info from the covid 19 Dataset are:\n {self.data.info()}")
        print(f"\nSome statistics from the numeric values of the Covid 19 Dataset:\n {self.data.describe()}")

    # Δεν χρησιμοποιώ το inplace γιατί μου το βγάζει ώς depricated method και στο documentation αναφέρει ως καλή πρακτική να το δηλώνουμε σε καινούργια ή την ίδια μεταβλητή.
    def handle_missing_values(self, column_name: str) :
        """Filling missing values.
           Numbers with zeros.
           Category data with Unknown.
           Boolean with None. 
        """
        if  isinstance(self.data[f"{column_name}"], (int, float)):
            self.data[f"{column_name}"] = self.data[f"{column_name}"].fillna(0)

        elif isinstance(self.data[f"{column_name}"], str):
            self.data[f"{column_name}"] = self.data[f"{column_name}"].fillna("Unknown")

        else:
            "For boolean type"
            self.data[f"{column_name}"] = self.data[f"{column_name}"].fillna(None)

    def filter_high_cases(self):
        """This method filter the dataset for confirmed cases greater than 100.000
           and deaths above 5000 for identified Countries."""
        high_cases = (self.data[self.data["Confirmed"] > 100_000] & self.data[self.data["Deaths"] > 5_000]
                       & self.data[self.data["Country/Region"] != "Unknown"])

        self.filtered_data = high_cases


    from datetime import date
    def filter_by_date_range(self, start_date: date, end_date: date ):
        """ """
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        
    





