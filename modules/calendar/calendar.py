from kivy.uix.widget import Widget
from kivy.properties import StringProperty

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

filepath = 'modules/calendar/'

class CalendarWidget(Widget):
	eventText= StringProperty()


	calendarService = None

	def setUpCalendar(self):
	    """Shows basic usage of the Google Calendar API.
	    Prints the start and name of the next 10 events on the user's calendar.
	    """
	    creds = None
	    # The file token.pickle stores the user's access and refresh tokens, and is
	    # created automatically when the authorization flow completes for the first
	    # time.
	    if os.path.exists(filepath+'token.pickle'):
	        with open(filepath+'token.pickle', 'rb') as token:
	            creds = pickle.load(token)
	    # If there are no (valid) credentials available, let the user log in.
	    if not creds or not creds.valid:
	        if creds and creds.expired and creds.refresh_token:
	            creds.refresh(Request())
	        else:
	            flow = InstalledAppFlow.from_client_secrets_file(
	                filepath+'credentials.json', SCOPES)
	            creds = flow.run_local_server(port=0)
	        # Save the credentials for the next run
	        with open(filepath+'token.pickle', 'wb') as token:
	            pickle.dump(creds, token)

	    self.calendarService = build('calendar', 'v3', credentials=creds)

	def updateCalendar(self, dt):
		n_events = 5

		if self.calendarService is None:
			eventText = "Not Connected!"
			return

		# Call the Calendar API
		now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
		events_result = self.calendarService.events().list(calendarId='primary', timeMin=now,
														maxResults=n_events, singleEvents=True,
														orderBy='startTime').execute()
		events = events_result.get('items', [])

		self.eventText = f'Upcoming {n_events} Calendar Events:\n'
		if not events:
			self.eventText = 'No upcoming events found.'

		for event in events:
			start = event['start'].get('dateTime', event['start'].get('date'))
			print(start)
			summary = event['summary']
			self.eventText += f'{summary}\n'

		print(self.eventText)