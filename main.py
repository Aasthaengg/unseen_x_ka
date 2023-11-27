import streamlit as st
import requests

# Function to request a screening session and get the URL
def request_screening(api_key):
    endpoint = "https://personality-api.unseenidentity.xyz/screeing/create"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()
    screening_url = response_data.get("url")

    return screening_url

# Function to get personality attributes using reference ID
def get_personality_attributes(api_key):
    endpoint = f"https://personality-api.unseenidentity.xyz/screeing/result/"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(endpoint, headers=headers)
    personality_attributes = response.json()

    return personality_attributes

# Function to get similarity between two categories
def get_similarity(api_key, category1, category2):
    endpoint = "https://personality-api.unseenidentity.xyz/screeing/similarities"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"c1": category1, "c2": category2}

    response = requests.post(endpoint, headers=headers, json=data)
    similarity_data = response.json()

    return similarity_data

def main():
    st.title("Personality Screening App")

    # Get API key and reference ID from user input
    api_key = st.text_input("Enter API Key:")

    # Request screening session and display the URL
    if st.button("Request Screening"):
        screening_url = request_screening(api_key)
        st.write("Screening URL:", screening_url)

        # Open the browser with the URL
        st.markdown(f"[Open Screening URL]({screening_url})")

    # Get personality attributes
    if st.button("Get Personality Attributes"):
        personality_attributes = get_personality_attributes(api_key)
        st.write("Personality Attributes:", personality_attributes)

    # Get similarity between two categories
    if st.button("Get Similarity"):
        category1 = st.text_input("Enter Category 1:")
        category2 = st.text_input("Enter Category 2:")

        similarity_data = get_similarity(api_key, category1, category2)
        st.write("Similarity Data:", similarity_data)

if __name__ == "__main__":
    main()
