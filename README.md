Office Integrator implementation code sample for Python language.

## Installing Dependencies

The ```requests``` package is required for this sample to work. To install the dependencies,

```pip3 install -r requirements.txt```

## How to test?

Run the following command in the terminal which will invoke Office Integrator APIs.

```python3 Test.py```

API responses will be printed on the terminal and the same will also be saved as file in ```demo/api_response``` folder.

#### Note:
In ```demo``` folder, the demo code is separately placed in individual files.

This code is added for reference purpose. You are free to make the changes in the code to fit your application's requirements.

## How to use this code in your app?

#### 1. Configuring the app

The app must be configured with your API Key and service's base URLs.

You can configure the app in three ways. Please refer to ```configurations/Configure.py```

The apikey used in the sample code is for demo purposes.
Replace the **apikey** constant's value with your own apikey generated in [OfficeIntegrator Service](http://officeintegrator.zoho.com/).

#### 2. Necessary files

The files in ```controllers``` folder are necessary for the app to function properly.

| File | Description |
| --- | --- |
| RestClient.py | To configure the app |
| Operations.py | Contains setters to input API request parameters  |
| Handler.py | Controllers to format your input parameters along with API defaults |
| APIHelper.py | Creates API request and returns formatted API response |
| Utility.py | Utility methods to handle API constants |
| ClientSideException.py |  |

#### 3. Invoking API

To test the API, you can run ```Test.py``` file.

The ```Test.py``` file contains methods which invokes API only with mandatory parameters.

Please refer to the sample code in ```zohowriter```, ```zohosheet``` and ```zohoshow``` folders in ```demo``` folder to explore various samples of code..
