from sorcery import dict_of
import pandas as pd
import os
import requests

"""
scan for doc size and doc type
store replace list as dictionaries
download document to global variable
for texts in dictionary Re.replace texts within the whole string

"""

def main():
    # get_user_profile()
    doc = load_doc()
    replace_list = get_replacelist()
    new_doc = replace(doc, replacelist)
    export(new_doc)


    """
    function verify :verify if the input is valid like a string
    """

    """
    lets start with input first so at least we can test something out for interface
    """


def get_user_profile():

    name=input("Name: ")
    email=input("Email: ")
    if re.fullmatch("[A-Za-z]{2,25}( [A-Za-z]{2,25})?",name,re.IGNORECASE) is False:
        raise ValueError("Invalid user name")
    elif re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email,re.IGNORECASE) is False:
        raise ValueError("Invalid email")
    else:
        names=set()
        names.add(name)
        emails=set()
        emails.add(email)
        user={name:email}
        print(user)
        print("User profile generated :)")


def get_replacelist():
    while True:
        try:
            avoid=input("Word to block?")
            preferred=input("Word to replace with?")
        #again, a typical naming convention check
            if re.match(r"\w+",avoid,re.IGNORECASE) and re.match(r"\w*",preferred,re.IGNORECASE):
                replacelist=dict_of(avoid,preferred)
                answer=input("Add more? (Y/N)")
        #starting to add more with a loop
                if answer=='Y':
                    newmatch={"avoid":avoid,"preferred":preferred}
                    replacelist.update(newmatch)
                    print(replacelist)
                elif answer=='N':
                    user.add(names,emails.replacelist)
                    break
                else:
                    raise ValueError("Not the right input format")
            else:
                raise ValueError("please input correct block/replacement word")
        except answer=="N":
            break


# def get_target_file(url):
#     """
#     load and read designated file
#     Here I'm thinking having file on the local folder is kinda impractical for other users than myself
#     so I want to create 1 version that I can test and load local docs
#     and also available for people to import online docs (primarily google doc)

#     """
#     # local_doc=input("full document name?")
#     # with open(sys.argv[-2]) as before:
#     #             excel = csv.DictReader(before)
#     #             for row in excel:
# """
# reference on Google doc api
# https://towardsdatascience.com/how-to-load-the-content-of-a-google-document-in-python-1d23fd8d8e52
# """

#https://docs.google.com/document/d/1WqlNW7rjKalqSmG1zHXnfeips_4x16Su8Z98c6DSuHc/edit?usp=sharing

#auth key: {"installed":{"client_id":"111557771937-927la7oqn1bj3sgkt486de6qhbpe69md.apps.googleusercontent.com","project_id":"jj-nofish","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["http://localhost"]}}

#now in the backend I'll create a demo goodle doc and download it to my txt file


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    url=input("Document url?")

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


os.getcwdb()

# doc_content = body.get('content')
# text = read_strucutural_elements(doc_content)


# with open("my_doc.txt", "w") as text_file:
#     text_file.write(text)

with open('my_doc.txt', 'w') as f:
    text = [line for line in f.readlines()]
df = pd.DataFrame(text,columns=['text'])

def scan(text):
"""
scan for potential match of the word and replace them with the matched new value

look thru every line to scan thru every pair of replacements
"""
    text = df
    for _in text:
        for dislikeword in avoid:
            my_regex = r".*" + re.escape(dislikeword) + r".*"
            re.sub(my_regex, replacelist[avoid], string, count=0, flags=0)


    return text


def output():
    with open(input("New file name?"),'w',newline='') as newdoc:
                writer = csv.writer(newdoc)
                writer.writerow(fields)


if __name__ == "__main__":
    main()