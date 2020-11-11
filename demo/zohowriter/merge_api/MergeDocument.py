from controllers.APIHelper import APIResponse, FileAPIResponse
from controllers.ClientSideException import ZOIException
from controllers.Operations import MergeAndDownload
from controllers.RestClient import ZOIRestClient


def configure():
    """
    Passing the entire configuration as a dictionary
    """
    try:
        config_obj = ZOIRestClient.get_instance()
        user_config = {
            "apikey": "2ae438cf864488657cc9754a27daa480",
            "writer_api_base_url": "https://api.office-integrator.com/writer/officeapi/",
            "sheet_api_base_url": "https://api.office-integrator.com/sheet/officeapi/",
            "show_api_base_url": "https://api.office-integrator.com/show/officeapi/"
        }
        config_obj.initialize(user_config)
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


def merge_and_download():
    try:
        merge_download = MergeAndDownload.get_instance()

        merge_download.set_output_format("docx")
        merge_download.upload_document("file_content", "../../../files/ZohoWriter_MergeTemplete.docx")
        merge_download.upload_document("merge_data_json_content", "../../../files/mergedata.json")

        response = merge_download.merge_and_download()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "conversion_" + response.file_name
            output_file_name = output_file_name.replace("\"", "")
            with open(output_file_name, "wb") as f:
                f.write(response.file_content)
            print("Merged document stored in output folder with filename : " + output_file_name)
        else:
            print(str(response))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


if __name__ == '__main__':
    configure()
    merge_and_download()
