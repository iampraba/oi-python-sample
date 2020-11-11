from controllers.APIHelper import APIResponse, FileAPIResponse
from controllers.ClientSideException import ZOIException
from controllers.Operations import WatermarkDocument
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


def watermark_document():
    try:
        watermark_doc = WatermarkDocument.get_instance()

        watermark_doc.set_watermark_settings("type", "text")
        watermark_doc.set_watermark_settings("opacity", "0.5")
        watermark_doc.set_watermark_settings("text", "Zoho Corp.")
        watermark_doc.upload_document("document", "../../../files/ZohoWriter_Watermark.docx")
        # watermark_doc.set_url("File URL Here")

        response = watermark_doc.watermark_document()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "watermark_" + response.file_name
            with open(output_file_name, "wb") as f:
                f.write(response.file_content)
            print("\nWatermark output file saved in output folder with filename : " + output_file_name)
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
    watermark_document()
