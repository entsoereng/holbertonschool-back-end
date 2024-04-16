""" Script """
import requests
import sys

if __name__== "__main__":
    url = "https//jsonplaceholder.tyipcode.com/"

    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()
