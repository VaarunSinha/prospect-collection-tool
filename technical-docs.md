# Setup

1. Get your Apollo API key from Apollo.

To get started with setup, the first step is making sure that your Apollo plan comes with API access. If you aren't sure whether it does, be sure to check the Settings > Integrations page in Apollo. Plans that offer API access will show a Connect button next the the API option at the bottom of the page:

<img src=https://support.apollo.io/hc/article_attachments/360060999771/mceclip6.png >

Click the Connect button so you are brought to a page that shows your API credentials:

<img src=https://support.apollo.io/hc/article_attachments/360060999911/mceclip7.png >

The team-specific API key shown on this page will be needed in order for you to access the API, so be sure to copy it for later use during the setup process.

Now create a .env file at the root of the CLI and the script, and paste the following:

```
API_KEY=<YOUR API KEY>
```

If you are using git for your version control, to hide this sensitive API_KEY add ".env" in your .gitignore.

2. Setting Up Python

Make sure your python version is 3.7+, if python is not installed in your system then install it from: https://www.python.org/downloads/

_Recommendation: We recommend to initialise a virtual environment so that it does not conflict with other python packages in your system, you can setup your virtual env from here: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/_

Then Run:

```
 pip install -r requirements.txt
```

**Congrats You Have Succesfully Setup The Project**

# Use Cases

## CLI

There are two commands in the CLI:

1. getprospects
   Gets prospects from the apollo api and stores it in names.csv file.

   Params: File path for the data configurationof the project. (str)

2. make_json
   Makes Config files to pass to the getprospects command.

   Params: desired filename for the output

## Python Functions

1. getprospects
   Gets prospects from the apollo api and stores it in names.csv file.
   Params: Data(dictionary), Headers

## Another Backend Language

For getting this data programmatically you can run the CLI from the language of your choice!

For example here's how you can run the command from Node.js:

```js
const { exec } = require("child_process");
exec("ls | grep js", (err, stdout, stderr) => {
  if (err) {
    //some err occurred
    console.error(err);
  } else {
    // the *entire* stdout and stderr (buffered)
    console.log(`stdout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
  }
});
```

**Thank You For Reading The Whole Docs**
