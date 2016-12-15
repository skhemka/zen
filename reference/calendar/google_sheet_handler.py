from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class GoogleSheetHandler:

    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
        self.CLIENT_SECRET_FILE = 'client_secret.json'
        self.APPLICATION_NAME = 'Google Sheets API Python Quickstart'
        self.content_list = []
        try:
            import argparse
            self.flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            self.flags = None

    def get_credentials(self):
        """Gets valid user credentials from storage.
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if self.flags:
                credentials = tools.run_flow(flow, store, self.flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def read_sheet(self, sheetid):
        """Shows basic usage of the Sheets API.

        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        rangeName = 'Sheet1!A2:F'
        result = service.spreadsheets().values().get(
            spreadsheetId=sheetid, range=rangeName).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            # print('Name, Time, Day:')
            for row in values:
                self.content_list.append(row)
                # Print columns A, C, and D
                # print('%s, %s, %s' % (row[0], row[2], row[3]))

    def get_content_list(self):
        return self.content_list

    def write_sheet(self, sheetid, vals):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        rangeName = 'Sheet1!A2:F'
        body = {
            "includeValuesInResponse": False,
            "data": [
                {
                    "range": rangeName,
                    "values": vals,
                    "majorDimension": "ROWS"
                }
            ],
            "valueInputOption": "USER_ENTERED"
        }
        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=sheetid, body=body).execute()
        # values = result.get('values', [])


def main():
    gh = GoogleSheetHandler()
    gh.read_sheet("1CAqx8xH81opQ1jJsa2a_dY8hzbWPG9kouUIvQWROM3I")
    print(gh.get_content_list())
    gh.write_sheet("1nb5wKk78xEReSKxjw6P0pe_tCRqhwh6-krjqpkuAVX4", [
                        [1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12]
                    ])


if __name__ == '__main__':
    main()
