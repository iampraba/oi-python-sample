from controllers.ClientSideException import ZOIException
from controllers.Operations import MergeAndDeliver
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


def merge_and_deliver_via_webhook():
    try:
        merge_deliver = MergeAndDeliver.get_instance()

        merge_deliver.set_output_format("pdf")
        merge_deliver.set_webhook("invoke_url", "https://domain.com/xyz.php")
        merge_deliver.set_webhook("invoke_period", "oncomplete")
        merge_deliver.set_merge_to("separatedoc")
        merge_deliver.upload_document("file_content", "../../../files/ZohoWriter_MergeTemplete.docx")
        # merge_deliver.set_file_url("File URL Here")
        merge_deliver.upload_document("merge_data_json_content", "../../../files/mergedata.json")

        response = merge_deliver.merge_and_deliver()
        response_json = response.response_json
        for key in response_json:
            print("{0}: {1}".format(key, response_json[key]))
    except ZOIException as ex:
        print(ex.status_code)
        print(ex.error_code)
        print(ex.error_message)
        print(ex.error_details)
        print(ex.error_content)


if __name__ == '__main__':
    configure()
    merge_and_deliver_via_webhook()
