"""
Utility classes that wraps common functionality to interact with 3rd party services or data
"""

from kedro.config import ConfigLoader
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd


class LoadCredentials:
    """class to load all bot credentials"""

    def __init__(self):
        conf_paths = ["conf/base", "conf/local"]
        conf_loader = ConfigLoader(conf_paths)
        self.credentials = conf_loader.get("credentials*", "credentials*/**")


class ConnectDrive(LoadCredentials):
    """class to connect to Google Drive"""

    def __init__(self):
        super().__init__()
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]

        # add credentials to the account
        drive_credentials = self.create_auth_credentials()
        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            drive_credentials, scope
        )

        # authorize the client sheet
        self.client = gspread.authorize(creds)

    def save_leaderboard(self, data):
        """Function to update a google sheet with the MEE6 leaderboard"""
        # get the instance of the Spreadsheet
        sheet = self.client.open("mee6_data")

        # get the first sheet of the Spreadsheet
        worksheet = sheet.get_worksheet(0)

        # read sheet as Pandas DataFrame
        records_df = pd.DataFrame.from_dict(worksheet.get_all_records())

        for player in data["players"]:
            row = {
                "username": player["username"],
                "xp": player["xp"],
                "message_count": player["message_count"],
                "level": player["level"],
            }
            records_df = records_df.append(row, ignore_index=True)

        # Update the spreadsheet in google drive
        worksheet.update(
            [records_df.columns.values.tolist()] + records_df.values.tolist()
        )

    def create_auth_credentials(self):
        cred = {
            "type": self.credentials["drive_key"]["type"],
            "project_id": self.credentials["drive_key"]["project_id"],
            "private_key_id": self.credentials["drive_key"]["private_key_id"],
            "private_key": self.credentials["drive_key"]["private_key"],
            "client_email": self.credentials["drive_key"]["client_email"],
            "client_id": self.credentials["drive_key"]["client_id"],
            "auth_uri": self.credentials["drive_key"]["auth_uri"],
            "token_uri": self.credentials["drive_key"]["token_uri"],
            "auth_provider_x509_cert_url": self.credentials["drive_key"]["auth_provider"],
            "client_x509_cert_url": self.credentials["drive_key"]["client_cert_url"],
        }

        return cred
