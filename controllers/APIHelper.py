import json

import requests

from controllers.ClientSideException import ZOIException
from controllers.RestClient import ZOIConfigUtil
from controllers.Utility import APIConstants


class APIRequest(object):

    def __init__(self, api_handler_init):
        self.url = api_handler_init.request_api_end_point
        if not self.url.startswith("http"):
            self.url = "https://" + self.url
        self.request_body = api_handler_init.request_body
        self.request_files = api_handler_init.request_files
        self.request_headers = api_handler_init.request_headers
        self.request_params = api_handler_init.request_params
        self.request_method = api_handler_init.request_method

    def authenticate_request(self):
        apikey = ZOIConfigUtil.get_instance().get_api_key()
        if self.request_headers is None:
            self.request_headers = {
                APIConstants.AUTHORIZATION: APIConstants.OAUTH_HEADER_PREFIX + apikey
            }
        else:
            self.request_headers[APIConstants.AUTHORIZATION] = APIConstants.OAUTH_HEADER_PREFIX + apikey
        self.request_headers['User-Agent'] = 'ZohoOI Python SDK'

    def get_api_response(self):
        try:
            self.authenticate_request()
            connector = HTTPConnector.get_instance(self.url, self.request_params, self.request_headers,
                                                   self.request_body, self.request_method)
            # Attachments are handled here
            if self.request_files is not None:
                try:
                    from controllers.Utility import CommonUtil
                except ImportError:
                    from .Utility import CommonUtil
                attachments = CommonUtil.create_api_supported_attachments_dictionary(self.request_files)
                connector.set_file(attachments)

            response = connector.trigger_request()
            content_type = response.headers["Content-Type"]
            if "application/json" in content_type or "text/" in content_type:
                return APIResponse(response, response.status_code, self.url)
            else:
                return FileAPIResponse(response, response.status_code, self.url)
        except ZOIException as ex:
            raise ex
        except Exception as ex:
            try:
                from controllers.Utility import CommonUtil
            except ImportError:
                from .Utility import CommonUtil
            import traceback
            CommonUtil.raise_exception(self.url, str(ex), traceback.format_stack())


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
        if self.status_code == APIConstants.RESPONSECODE_NO_CONTENT:
            error_msg = APIConstants.INVALID_DATA + "-" + APIConstants.INVALID_ID_MSG
            exception = ZOIException(self.url, self.status_code, error_msg, APIConstants.NO_CONTENT, None, error_msg)
            exception.message = exception.__str__()
            raise exception
        else:
            print(json.dumps(self.response_json, indent=4))
            response_json = self.response_json
            exception = ZOIException(self.url, self.status_code, response_json[APIConstants.MESSAGE],
                                     response_json[APIConstants.CODE], response_json[APIConstants.DETAILS],
                                     response_json[APIConstants.MESSAGE])
            exception.message = exception.__str__()
            raise exception

    def process_response_data(self):
        resp_json = self.response_json
        if isinstance(resp_json, list):
            resp_json = resp_json[0]
        if APIConstants.STATUS in resp_json and (resp_json[APIConstants.STATUS] == APIConstants.STATUS_ERROR):
            exception = ZOIException(self.url, self.status_code, resp_json[APIConstants.MESSAGE],
                                     resp_json[APIConstants.CODE], resp_json[APIConstants.DETAILS],
                                     resp_json[APIConstants.STATUS])
            exception.message = exception.__str__()
            raise exception
        elif APIConstants.STATUS in resp_json and (resp_json[APIConstants.STATUS] == APIConstants.STATUS_SUCCESS):
            self.status = resp_json[APIConstants.STATUS]
            self.code = resp_json[APIConstants.CODE]
            self.message = resp_json[APIConstants.MESSAGE]
            self.details = resp_json[APIConstants.DETAILS]


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
            error_msg = APIConstants.INVALID_DATA + "-" + APIConstants.INVALID_ID_MSG
            exception = ZOIException(self.url, self.status_code, error_msg, APIConstants.NO_CONTENT, None,
                                     error_msg)
            exception.message = exception.__str__()
            raise exception
        else:
            response_json = self.response.json()
            exception = ZOIException(self.url, self.response.status_code, response_json[APIConstants.MESSAGE],
                                     response_json[APIConstants.CODE], response_json[APIConstants.DETAILS],
                                     response_json[APIConstants.MESSAGE])
            exception.message = exception.__str__()
            raise exception


class HTTPConnector(object):

    @staticmethod
    def get_instance(url, params, headers, body, method):
        """
        :param url:
        :param params:
        :param headers:
        :param body:
        :param method:
        :return:
        """
        return HTTPConnector(url, params, headers, body, method)

    def __init__(self, url, params, headers, body, method):
        self.url = url
        self.req_headers = headers
        self.req_method = method
        self.req_params = params
        self.req_body = body
        self.file = None

    def trigger_request(self):
        response = None

        # For Testing these temporary print statements are included!!!
        # print(self.url)
        # print(self.req_headers)
        # print(self.req_method)
        # print(self.req_params)
        # print(self.req_body)
        # print(self.file)

        if self.req_method == APIConstants.REQUEST_METHOD_GET:
            response = requests.get(self.url, headers=self.req_headers, params=self.req_params, allow_redirects=False)
        elif self.req_method == APIConstants.REQUEST_METHOD_PUT:
            response = requests.put(self.url, data=self.req_body, params=self.req_params,
                                    headers=self.req_headers, allow_redirects=False)
        elif self.req_method == APIConstants.REQUEST_METHOD_POST:
            if self.file is None:
                response = requests.post(self.url, data=self.req_body, params=self.req_params,
                                         headers=self.req_headers, allow_redirects=False)
            else:
                response = requests.post(self.url, files=self.file, headers=self.req_headers, allow_redirects=False,
                                         data=self.req_body)
        elif self.req_method == APIConstants.REQUEST_METHOD_DELETE:
            response = requests.delete(self.url, headers=self.req_headers, params=self.req_params,
                                       allow_redirects=False)
        return response

    @staticmethod
    def get_request_params_as_string(params):
        map_as_string = ''
        for key in params:
            map_as_string += key + '=' + params[key]
        return map_as_string

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def add_http_header(self, key, value):
        self.req_headers.put(key, value)

    def get_http_headers(self):
        return self.req_headers

    def set_http_request_method(self, method):
        self.req_method = method

    def get_http_request_method(self):
        return self.req_method

    def set_request_body(self, req_body):
        self.req_body = req_body

    def get_request_body(self):
        return self.req_body

    def add_http_request_params(self, key, value):
        self.req_params.put(key, value)

    def get_http_request_params(self):
        return self.req_params

    def set_file(self, file_content):
        self.file = file_content
