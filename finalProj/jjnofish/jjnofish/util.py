from sorcery import dict_of
import pandas as pd
import os
import requests
from django import forms

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
step 1. load document
"""
def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

"""
function verify :verify if the input is valid like a string
"""

"""
lets start with input first so at least we can test something out for interface
"""



def get_replacelist():
     if request.method == "POST":
        original_word = request.POST['original_word']
        replacement = request.POST['replacement']
        if re.match(r"\w+",original_word,re.IGNORECASE) and re.match(r"\w*",replacement,re.IGNORECASE):
            replacelist=dict_of(original_word,replacement)
            answer=input("Add more? (Y/N)")
    #starting to add more with a loop
            if answer=='Y':
                newmatch={"avoid":avoid,"preferred":replacement}
                replacelist.update(newmatch)
                print(replacelist)
            elif answer=='N':
                user.add(names,emails.replacelist)
                sys.exit()
            # else:
            #     raise ValueError("Not the right input format")
        else:
            raise ValueError("please input correct block/replacement word")
    # except answer=="N":
    #     break
    #render a new page
        # return render(request, "encyclopedia/entry.html", {
        #     "title": title,
        #     "answer": new_display})

# so many ways to download files
# def download(url: str, dest_folder: str):
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)  # create folder if it does not exist

#     url=input("Document url?")

#     filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
#     file_path = os.path.join(dest_folder, filename)

#     r = requests.get(url, stream=True)
#     if r.ok:
#         print("saving to", os.path.abspath(file_path))
#         with open(file_path, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024 * 8):
#                 if chunk:
#                     f.write(chunk)
#                     f.flush()
#                     os.fsync(f.fileno())
#     else:  # HTTP status code 4XX/5XX
#         print("Download failed: status code {}\n{}".format(r.status_code, r.text))


# os.getcwdb()

# doc_content = body.get('content')
# text = read_strucutural_elements(doc_content)


# with open("my_doc.txt", "w") as text_file:
#     text_file.write(text)

# with open('my_doc.txt', 'w') as f:
#     text = [line for line in f.readlines()]
# df = pd.DataFrame(text,columns=['text'])

"""
scan for potential match of the word and replace them with the matched new value

look thru every line to scan thru every pair of replacements
"""
def scan(text):
    text = df
    for _ in text:
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




# def get_user_profile():

#     name=input("Name: ")
#     email=input("Email: ")
#     if re.fullmatch("[A-Za-z]{2,25}( [A-Za-z]{2,25})?",name,re.IGNORECASE) is False:
#         raise ValueError("Invalid user name")
#     elif re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email,re.IGNORECASE) is False:
#         raise ValueError("Invalid email")
#     else:
#         names=set()
#         names.add(name)
#         emails=set()
#         emails.add(email)
#         user={name:email}
#         print(user)
#         print("User profile generated :)")

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
#