from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students',
          'https://www.googleapis.com/auth/classroom.rosters', 'https://www.googleapis.com/auth/classroom.courses']
coursework_array = []
studentwork_array = []
student_array = []
courseid_array = []


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)
    # Get courses
    courses = service.courses().list().execute()
    for course in courses["courses"]:
        if "APCS" in course["name"]:
            courseid_array.append(course["id"])

    for id in courseid_array:
        # Get students unique ids
        students = service.courses().students().list(courseId=id).execute()
        for student in students["students"]:
            student_dict = {"id": student["userId"], "name": student["profile"]["name"]["givenName"]}
            student_array.append(student_dict)

        # Get submission link
        courses_work = service.courses().courseWork()
        results = courses_work.list(courseId=id).execute()
        if not results:
            print('No course work found.')
        else:
            for work in results["courseWork"]:
                coursework_dict = {"assignment_name": work["title"], "assignment_id": work["id"]}
                coursework_array.append(coursework_dict)

        if coursework_array[0]["assignment_name"] == "Starfield":
            student_work = courses_work.studentSubmissions().list(courseId=id,
                                                                  courseWorkId=coursework_array[0][
                                                                      "assignment_id"]).execute()
            for person in student_work["studentSubmissions"]:
                submission_dict = person["assignmentSubmission"]["attachments"][0]["link"]
                for student in student_array:
                    if student["id"] == person["userId"]:
                        submission_dict["student"] = student["name"]
                studentwork_array.append(submission_dict)

    f = open("work.md", "a")
    for work in studentwork_array:
        f.write("\n" + "[" + work["student"] + "](" + work["url"] + ")" + " " + " " + " ")

    f.close()


if __name__ == '__main__':
    main()
