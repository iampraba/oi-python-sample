
from Utility import ZOIConfigUtil, APIConstants, HTTPConnector
from ClientSideException import ZOIException
from Response import APIResponse, FileAPIResponse


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
                    from Utility import CommonUtil
                except ImportError:
                    from .Utility import CommonUtil
                attachments = CommonUtil.create_api_supported_attachments_dictionary(self.request_files)
                connector.set_file(attachments)

            response = connector.trigger_request()
            cont_type = response.headers["Content-Type"]
            if cont_type[:cont_type.index(";")] == "application/json":
                return APIResponse(response, response.status_code, self.url)
            else:
                return FileAPIResponse(response, response.status_code, self.url)
        except ZOIException as ex:
            raise ex
        except Exception as ex:
            try:
                from Utility import CommonUtil
            except ImportError:
                from .Utility import CommonUtil
            import traceback
            CommonUtil.raise_exception(self.url, str(ex), traceback.format_stack())
