import pandas as pd
from typing import Optional

class DataInspector:
    """A class to handle loading and initial inspection of tabular datasets."""
    
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.df: Optional[pd.DataFrame] = None

    def load_data(self) -> pd.DataFrame:
        """Loads the CSV file into a pandas DataFrame."""
        try:
            self.df = pd.read_csv(self.file_path)
            return self.df
        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset not found: {self.file_path}")

    def show_preview(self, rows: int = 5) -> None:
        """Prints the first few rows of the dataset."""
        self._ensure_data_loaded()
        print(f"--- First {rows} Rows ---")
        print(self.df.head(rows))

    def show_dimensions(self) -> None:
        """Prints the shape and column names of the dataset."""
        self._ensure_data_loaded()
        print(f"\n--- Shape (Rows, Columns) ---")
        print(self.df.shape)
        print(f"\n--- Columns ---")
        print(self.df.columns)

    def show_info(self) -> None:
        """Prints technical information about the DataFrame."""
        self._ensure_data_loaded()
        print(f"\n--- DataFrame Info ---")
        self.df.info()

    def show_missing_data(self) -> None:
        self._ensure_data_loaded()

        missing = pd.DataFrame({
            "Missing_Count": self.df.isnull().sum(),
            "Missing_Percentage": (self.df.isnull().mean() * 100).round(2)
        })

        print("\n--- Missing Value Analysis ---")
        print(missing[missing["Missing_Count"] > 0])
        
    def show_duplicates(self) -> None:
        self._ensure_data_loaded()

        print("\n--- Duplicate Records ---")
        print(self.df.duplicated().sum())

    def run_all_checks(self) -> None:
        """Executes a full profile check of the data."""
        self.load_data()
        self.show_preview()
        self.show_dimensions()
        self.show_info()
        self.show_missing_data()
        self.show_duplicates()

    def _ensure_data_loaded(self) -> None:
        """Internal helper to prevent operations before loading data."""
        if self.df is None:
            raise ValueError("Data has not been loaded yet. Call load_data() first.")


# --- Execution ---
if __name__ == "__main__":
    DATA_PATH = "data/raw/retail_store_daily_sales_regression.csv"
    
    inspector = DataInspector(DATA_PATH)
    inspector.run_all_checks()
