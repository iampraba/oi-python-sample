
from ClientSideException import ZOIException
from Utility import APIConstants


class APIResponse(object):

    def __init__(self, response, status_code, url):
        self.response_json = None
        self.response_headers = None
        self.response = response
        self.status_code = status_code
        self.url = url
        self.status = None
        self.code = None
        self.message = None
        self.details = None
        self.set_response()
        self.process_response()

    def set_response(self):
        if self.status_code != APIConstants.RESPONSECODE_NO_CONTENT and self.status_code != APIConstants.RESPONSECODE_NOT_MODIFIED:
            self.response_json = self.response.json()
        self.response_headers = self.response.headers

    def process_response(self):
        if self.status_code in APIConstants.FAULTY_RESPONSE_CODES:
            self.handle_faulty_responses()
        else:
            self.process_response_data()

    def handle_faulty_responses(self):
        """
        if self.status_code == APIConstants.RESPONSECODE_NO_CONTENT:
            errorMsg = APIConstants.INVALID_DATA + "-" + APIConstants.INVALID_ID_MSG
            exception = ZOIException(self.url, self.status_code, errorMsg, APIConstants.NO_CONTENT, None, errorMsg)
            exception.message = exception.__str__()
            raise exception
        else:
            responseJSON = self.response_json
            exception = ZOIException(self.url, self.status_code, responseJSON[APIConstants.MESSAGE],
                                     responseJSON[APIConstants.CODE], responseJSON[APIConstants.DETAILS],
                                     responseJSON[APIConstants.MESSAGE])
            exception.message = exception.__str__()
            raise exception
        """
        self.response_json = self.response.json()

    def process_response_data(self):
        respJson = self.response_json
        if isinstance(respJson, list):
            respJson = respJson[0]
        if APIConstants.STATUS in respJson and (respJson[APIConstants.STATUS] == APIConstants.STATUS_ERROR):
            exception = ZOIException(self.url, self.status_code, respJson[APIConstants.MESSAGE],
                                     respJson[APIConstants.CODE], respJson[APIConstants.DETAILS],
                                     respJson[APIConstants.STATUS])
            exception.message = exception.__str__()
            raise exception
        elif APIConstants.STATUS in respJson and (respJson[APIConstants.STATUS] == APIConstants.STATUS_SUCCESS):
            self.status = respJson[APIConstants.STATUS]
            self.code = respJson[APIConstants.CODE]
            self.message = respJson[APIConstants.MESSAGE]
            self.details = respJson[APIConstants.DETAILS]


class FileAPIResponse(object):

    def __init__(self, response, status_code, url):
        self.response = response
        self.status_code = status_code
        self.url = url
        self.file_name = None
        self.file_content = None
        self.response_headers = None
        self.status = None
        self.code = None
        self.message = None
        self.details = None
        self.handle_file_response()

    def handle_file_response(self):
        if self.status_code == APIConstants.RESPONSECODE_OK:
            self.status = APIConstants.STATUS_SUCCESS
            content_disposition = self.response.headers['Content-Disposition']
            start_index = content_disposition.rindex("=")
            self.file_name = content_disposition[start_index + 1:]
            self.file_content = self.response.content
            self.response_headers = self.response.headers
        elif self.status_code == APIConstants.RESPONSECODE_NO_CONTENT:
            errorMsg = APIConstants.INVALID_DATA + "-" + APIConstants.INVALID_ID_MSG
            exception = ZOIException(self.url, self.status_code, errorMsg, APIConstants.NO_CONTENT, None,
                                     errorMsg)
            exception.message = exception.__str__()
            raise exception
        else:
            responseJSON = self.response.json()
            exception = ZOIException(self.url, self.response.status_code, responseJSON[APIConstants.MESSAGE],
                                     responseJSON[APIConstants.CODE], responseJSON[APIConstants.DETAILS],
                                     responseJSON[APIConstants.MESSAGE])
            exception.message = exception.__str__()
            raise exception
